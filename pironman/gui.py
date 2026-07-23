#!/usr/bin/env python3
import os
import sys
import time
import subprocess
import configparser
from pathlib import Path

# Fallback/Import CustomTkinter
try:
    import customtkinter as ctk
except ImportError:
    print("Installing customtkinter...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "customtkinter"])
    import customtkinter as ctk

# Add parent directory to path to import pironman modules
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from app_info import __app_name__, __version__, config_file
from gui_components import MetricCard, ColorPickerWidget, LogViewerWidget

# Import system_status if available
try:
    from system_status import getCPUtemperature, getRAMinfo, getCPUuse, getDiskSpace, getIP
except Exception:
    # Dummy fallbacks for non-pi development testing
    def getCPUtemperature(): return 42.5
    def getRAMinfo(): return ["8000000", "2500000", "5500000"]
    def getCPUuse(): return 15.4
    def getDiskSpace(): return (32.0, 12.5, 19.5, 39)
    def getIP(): return {"wlan0": "192.168.1.100", "eth0": ""}

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")


class PironmanGUI(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title(f"SunFounder {__app_name__.title()} Dashboard v{__version__}")
        self.geometry("900x620")
        self.minsize(750, 500)

        # Config file path
        self.config_path = config_file if os.path.exists(config_file) else "/opt/pironman/config.txt"
        self.load_config()

        # Build UI layout
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self._create_sidebar()
        self._create_main_content()

        # Select initial tab
        self.select_tab("dashboard")

        # Start metric update timer (every 2000 ms)
        self.update_metrics_loop()

    # -------------------------------------------------------------
    # Config File Helpers
    # -------------------------------------------------------------
    def load_config(self):
        self.config = configparser.ConfigParser()
        self.cfg_data = {
            "temp_unit": "C",
            "fan_temp": 50.0,
            "screen_always_on": "False",
            "screen_off_time": 60,
            "rgb_enable": "True",
            "rgb_style": "breath",
            "rgb_color": "0a1aff",
            "rgb_blink_speed": 50,
            "rgb_pwm_freq": 1000,
            "rgb_pin": 10,
        }

        if os.path.exists(self.config_path):
            try:
                self.config.read(self.config_path)
                if "all" in self.config:
                    for k in self.cfg_data.keys():
                        if k in self.config["all"]:
                            self.cfg_data[k] = self.config["all"][k]
            except Exception as e:
                print(f"Error reading config file: {e}")

    def save_config(self):
        if "all" not in self.config:
            self.config["all"] = {}

        for k, v in self.cfg_data.items():
            self.config["all"][k] = str(v)

        try:
            # Use sudo if permission denied when writing to /opt/pironman/config.txt
            if os.path.exists(self.config_path) and not os.access(self.config_path, os.W_OK):
                temp_file = "/tmp/pironman_gui_cfg.tmp"
                with open(temp_file, "w") as f:
                    self.config.write(f)
                subprocess.run(f"sudo cp {temp_file} {self.config_path}", shell=True, check=True)
            else:
                os.makedirs(os.path.dirname(self.config_path), exist_ok=True)
                with open(self.config_path, "w") as f:
                    self.config.write(f)
            return True
        except Exception as e:
            print(f"Failed to save config: {e}")
            return False

    # -------------------------------------------------------------
    # Navigation Sidebar
    # -------------------------------------------------------------
    def _create_sidebar(self):
        self.sidebar = ctk.CTkFrame(self, width=200, corner_radius=0)
        self.sidebar.grid(row=0, column=0, sticky="nsew")
        self.sidebar.grid_rowconfigure(6, weight=1)

        # App Logo/Title
        self.logo_label = ctk.CTkLabel(
            self.sidebar,
            text="PIRONMAN",
            font=ctk.CTkFont(size=22, weight="bold"),
            text_color="#3B8ED0"
        )
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 5))

        self.sub_label = ctk.CTkLabel(
            self.sidebar,
            text=f"v{__version__} Control Center",
            font=ctk.CTkFont(size=12),
            text_color="gray60"
        )
        self.sub_label.grid(row=1, column=0, padx=20, pady=(0, 20))

        # Nav Buttons
        self.btn_dashboard = ctk.CTkButton(
            self.sidebar, text="📊  Dashboard", anchor="w", command=lambda: self.select_tab("dashboard")
        )
        self.btn_dashboard.grid(row=2, column=0, padx=15, pady=5, sticky="ew")

        self.btn_fan = ctk.CTkButton(
            self.sidebar, text="🌡️  Fan Control", anchor="w", command=lambda: self.select_tab("fan")
        )
        self.btn_fan.grid(row=3, column=0, padx=15, pady=5, sticky="ew")

        self.btn_rgb = ctk.CTkButton(
            self.sidebar, text="🎨  RGB Lighting", anchor="w", command=lambda: self.select_tab("rgb")
        )
        self.btn_rgb.grid(row=4, column=0, padx=15, pady=5, sticky="ew")

        self.btn_oled = ctk.CTkButton(
            self.sidebar, text="🖥️  OLED Display", anchor="w", command=lambda: self.select_tab("oled")
        )
        self.btn_oled.grid(row=5, column=0, padx=15, pady=5, sticky="ew")

        self.btn_service = ctk.CTkButton(
            self.sidebar, text="⚙️  Service & Logs", anchor="w", command=lambda: self.select_tab("service")
        )
        self.btn_service.grid(row=6, column=0, padx=15, pady=5, sticky="ew")

        # Sidebar Footer
        self.restart_service_btn = ctk.CTkButton(
            self.sidebar,
            text="🔄 Restart Service",
            fg_color="#D32F2F",
            hover_color="#9A0007",
            command=self._restart_daemon_service
        )
        self.restart_service_btn.grid(row=7, column=0, padx=15, pady=(10, 20), sticky="ew")

    # -------------------------------------------------------------
    # Main Content Views
    # -------------------------------------------------------------
    def _create_main_content(self):
        self.content_container = ctk.CTkFrame(self, fg_color="transparent")
        self.content_container.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)
        self.content_container.grid_rowconfigure(0, weight=1)
        self.content_container.grid_columnconfigure(0, weight=1)

        # Tab Views
        self.tab_frames = {}
        self.tab_frames["dashboard"] = self._build_dashboard_view()
        self.tab_frames["fan"] = self._build_fan_view()
        self.tab_frames["rgb"] = self._build_rgb_view()
        self.tab_frames["oled"] = self._build_oled_view()
        self.tab_frames["service"] = self._build_service_view()

    def select_tab(self, tab_name):
        for name, frame in self.tab_frames.items():
            frame.grid_forget()

        self.tab_frames[tab_name].grid(row=0, column=0, sticky="nsew")

        # Update button highlighting
        nav_btns = {
            "dashboard": self.btn_dashboard,
            "fan": self.btn_fan,
            "rgb": self.btn_rgb,
            "oled": self.btn_oled,
            "service": self.btn_service,
        }
        for name, btn in nav_btns.items():
            btn.configure(fg_color=("#3B8ED0", "#1F6AA5") if name == tab_name else "transparent")

    # -------------------------------------------------------------
    # View 1: Dashboard
    # -------------------------------------------------------------
    def _build_dashboard_view(self):
        frame = ctk.CTkFrame(self.content_container, fg_color="transparent")
        frame.grid_columnconfigure((0, 1), weight=1)

        ctk.CTkLabel(frame, text="System Monitor & Live Hardware Metrics", font=ctk.CTkFont(size=18, weight="bold")).grid(
            row=0, column=0, columnspan=2, sticky="w", pady=(0, 15)
        )

        # Metric Cards Grid
        self.card_cpu_temp = MetricCard(frame, title="CPU Temperature", value="--", unit="°C", color="#26A69A")
        self.card_cpu_temp.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        self.card_cpu_usage = MetricCard(frame, title="CPU Load", value="--", unit="%", color="#42A5F5")
        self.card_cpu_usage.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

        self.card_ram = MetricCard(frame, title="RAM Usage", value="--", unit="", color="#AB47BC")
        self.card_ram.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

        self.card_disk = MetricCard(frame, title="Storage Space", value="--", unit="", color="#FFA726")
        self.card_disk.grid(row=2, column=1, padx=10, pady=10, sticky="nsew")

        self.card_ip = MetricCard(frame, title="Network IP Address", value="--", unit="", color="#66BB6A")
        self.card_ip.grid(row=3, column=0, padx=10, pady=10, sticky="nsew")

        self.card_fan = MetricCard(frame, title="Cooling Fan Status", value="--", unit="", color="#FF7043")
        self.card_fan.grid(row=3, column=1, padx=10, pady=10, sticky="nsew")

        return frame

    # -------------------------------------------------------------
    # View 2: Fan Control
    # -------------------------------------------------------------
    def _build_fan_view(self):
        frame = ctk.CTkFrame(self.content_container, fg_color="transparent")

        ctk.CTkLabel(frame, text="Cooling Fan Settings", font=ctk.CTkFont(size=18, weight="bold")).pack(anchor="w", pady=(0, 15))

        card = ctk.CTkFrame(frame)
        card.pack(fill="x", padx=10, pady=10)

        # Unit switcher
        unit_frame = ctk.CTkFrame(card, fg_color="transparent")
        unit_frame.pack(fill="x", padx=15, pady=15)

        ctk.CTkLabel(unit_frame, text="Temperature Unit:", font=ctk.CTkFont(size=14, weight="bold")).pack(side="left")
        self.unit_segmented = ctk.CTkSegmentedButton(
            unit_frame,
            values=["C", "F"],
            command=self._on_unit_change
        )
        self.unit_segmented.set(self.cfg_data["temp_unit"])
        self.unit_segmented.pack(side="right")

        # Threshold slider
        thresh_frame = ctk.CTkFrame(card, fg_color="transparent")
        thresh_frame.pack(fill="x", padx=15, pady=15)

        ctk.CTkLabel(thresh_frame, text="Fan Start Temperature Threshold:", font=ctk.CTkFont(size=14, weight="bold")).pack(anchor="w")

        val = float(self.cfg_data["fan_temp"])
        self.fan_thresh_lbl = ctk.CTkLabel(thresh_frame, text=f"{val:.1f} °{self.cfg_data['temp_unit']}", font=ctk.CTkFont(size=16, weight="bold"), text_color="#3B8ED0")
        self.fan_thresh_lbl.pack(anchor="w", pady=5)

        self.fan_slider = ctk.CTkSlider(
            thresh_frame,
            from_=30,
            to=80,
            number_of_steps=50,
            command=self._on_fan_slider_move
        )
        self.fan_slider.set(val)
        self.fan_slider.pack(fill="x", pady=5)

        # Save Button
        ctk.CTkButton(card, text="Save Fan Settings", command=self._save_fan_settings).pack(anchor="e", padx=15, pady=15)

        return frame

    def _on_unit_change(self, value):
        self.cfg_data["temp_unit"] = value
        curr_val = self.fan_slider.get()
        self.fan_thresh_lbl.configure(text=f"{curr_val:.1f} °{value}")

    def _on_fan_slider_move(self, value):
        unit = self.unit_segmented.get()
        self.fan_thresh_lbl.configure(text=f"{value:.1f} °{unit}")

    def _save_fan_settings(self):
        self.cfg_data["temp_unit"] = self.unit_segmented.get()
        self.cfg_data["fan_temp"] = str(round(self.fan_slider.get(), 1))
        if self.save_config():
            self._restart_daemon_service()

    # -------------------------------------------------------------
    # View 3: RGB Lighting
    # -------------------------------------------------------------
    def _build_rgb_view(self):
        frame = ctk.CTkFrame(self.content_container, fg_color="transparent")

        ctk.CTkLabel(frame, text="WS2812 RGB LED Control Center", font=ctk.CTkFont(size=18, weight="bold")).pack(anchor="w", pady=(0, 15))

        card = ctk.CTkFrame(frame)
        card.pack(fill="x", padx=10, pady=10)

        # RGB Switch
        switch_frame = ctk.CTkFrame(card, fg_color="transparent")
        switch_frame.pack(fill="x", padx=15, pady=10)

        ctk.CTkLabel(switch_frame, text="Enable RGB LED Strip:", font=ctk.CTkFont(size=14, weight="bold")).pack(side="left")
        self.rgb_enable_switch = ctk.CTkSwitch(switch_frame, text="")
        if self.cfg_data["rgb_enable"] in ["True", "on", True]:
            self.rgb_enable_switch.select()
        else:
            self.rgb_enable_switch.deselect()
        self.rgb_enable_switch.pack(side="right")

        # RGB Style Dropdown
        style_frame = ctk.CTkFrame(card, fg_color="transparent")
        style_frame.pack(fill="x", padx=15, pady=10)

        ctk.CTkLabel(style_frame, text="Lighting Animation Style:", font=ctk.CTkFont(size=14, weight="bold")).pack(side="left")
        styles = ["breath", "static", "leap", "flow", "raise_up", "colorful", "colorful_static", "colorful_leap"]
        self.rgb_style_opt = ctk.CTkOptionMenu(style_frame, values=styles)
        if self.cfg_data["rgb_style"] in styles:
            self.rgb_style_opt.set(self.cfg_data["rgb_style"])
        self.rgb_style_opt.pack(side="right")

        # RGB Color Picker
        self.color_picker = ColorPickerWidget(card, current_hex=self.cfg_data["rgb_color"])
        self.color_picker.pack(fill="x", padx=15, pady=10)

        # Speed slider
        speed_frame = ctk.CTkFrame(card, fg_color="transparent")
        speed_frame.pack(fill="x", padx=15, pady=10)

        ctk.CTkLabel(speed_frame, text="Animation Speed (0 - 100):", font=ctk.CTkFont(size=14, weight="bold")).pack(anchor="w")
        self.speed_slider = ctk.CTkSlider(speed_frame, from_=0, to=100, number_of_steps=100)
        self.speed_slider.set(float(self.cfg_data.get("rgb_blink_speed", 50)))
        self.speed_slider.pack(fill="x", pady=5)

        # Save Button
        ctk.CTkButton(card, text="Apply RGB Settings", command=self._save_rgb_settings).pack(anchor="e", padx=15, pady=15)

        return frame

    def _save_rgb_settings(self):
        self.cfg_data["rgb_enable"] = "True" if self.rgb_enable_switch.get() == 1 else "False"
        self.cfg_data["rgb_style"] = self.rgb_style_opt.get()
        self.cfg_data["rgb_color"] = self.color_picker.get_color()
        self.cfg_data["rgb_blink_speed"] = str(int(self.speed_slider.get()))
        if self.save_config():
            self._restart_daemon_service()

    # -------------------------------------------------------------
    # View 4: OLED Display
    # -------------------------------------------------------------
    def _build_oled_view(self):
        frame = ctk.CTkFrame(self.content_container, fg_color="transparent")

        ctk.CTkLabel(frame, text="OLED Display Manager", font=ctk.CTkFont(size=18, weight="bold")).pack(anchor="w", pady=(0, 15))

        card = ctk.CTkFrame(frame)
        card.pack(fill="x", padx=10, pady=10)

        # Always On Switch
        ao_frame = ctk.CTkFrame(card, fg_color="transparent")
        ao_frame.pack(fill="x", padx=15, pady=15)

        ctk.CTkLabel(ao_frame, text="Keep Display Always On:", font=ctk.CTkFont(size=14, weight="bold")).pack(side="left")
        self.always_on_switch = ctk.CTkSwitch(ao_frame, text="")
        if self.cfg_data["screen_always_on"] in ["True", "on", True]:
            self.always_on_switch.select()
        else:
            self.always_on_switch.deselect()
        self.always_on_switch.pack(side="right")

        # Off Time Slider
        off_frame = ctk.CTkFrame(card, fg_color="transparent")
        off_frame.pack(fill="x", padx=15, pady=15)

        ctk.CTkLabel(off_frame, text="Screen Sleep Timeout (seconds):", font=ctk.CTkFont(size=14, weight="bold")).pack(anchor="w")

        curr_off = float(self.cfg_data.get("screen_off_time", 60))
        self.off_time_lbl = ctk.CTkLabel(off_frame, text=f"{int(curr_off)} seconds", font=ctk.CTkFont(size=15, weight="bold"))
        self.off_time_lbl.pack(anchor="w", pady=2)

        self.off_time_slider = ctk.CTkSlider(
            off_frame,
            from_=10,
            to=300,
            number_of_steps=29,
            command=lambda v: self.off_time_lbl.configure(text=f"{int(v)} seconds")
        )
        self.off_time_slider.set(curr_off)
        self.off_time_slider.pack(fill="x", pady=5)

        # Save Button
        ctk.CTkButton(card, text="Save Display Settings", command=self._save_oled_settings).pack(anchor="e", padx=15, pady=15)

        return frame

    def _save_oled_settings(self):
        self.cfg_data["screen_always_on"] = "True" if self.always_on_switch.get() == 1 else "False"
        self.cfg_data["screen_off_time"] = str(int(self.off_time_slider.get()))
        if self.save_config():
            self._restart_daemon_service()

    # -------------------------------------------------------------
    # View 5: Service & Logs
    # -------------------------------------------------------------
    def _build_service_view(self):
        frame = ctk.CTkFrame(self.content_container, fg_color="transparent")
        frame.grid_rowconfigure(1, weight=1)
        frame.grid_columnconfigure(0, weight=1)

        # Header controls
        top_card = ctk.CTkFrame(frame)
        top_card.grid(row=0, column=0, sticky="ew", padx=10, pady=(0, 10))

        ctk.CTkLabel(top_card, text="Systemd Service Controls", font=ctk.CTkFont(size=16, weight="bold")).pack(anchor="w", padx=15, pady=(10, 5))

        btn_box = ctk.CTkFrame(top_card, fg_color="transparent")
        btn_box.pack(fill="x", padx=15, pady=10)

        ctk.CTkButton(btn_box, text="Start Service", fg_color="#2E7D32", command=lambda: self._exec_service_cmd("start")).pack(side="left", padx=5)
        ctk.CTkButton(btn_box, text="Stop Service", fg_color="#C62828", command=lambda: self._exec_service_cmd("stop")).pack(side="left", padx=5)
        ctk.CTkButton(btn_box, text="Restart Service", fg_color="#1565C0", command=lambda: self._exec_service_cmd("restart")).pack(side="left", padx=5)

        # Log viewer
        self.log_viewer = LogViewerWidget(frame)
        self.log_viewer.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

        return frame

    def _exec_service_cmd(self, action):
        cmd = f"sudo pironman {action}"
        try:
            subprocess.run(cmd, shell=True, check=True)
            if hasattr(self, "log_viewer"):
                self.log_viewer.refresh_logs()
        except Exception as e:
            print(f"Service action failed: {e}")

    def _restart_daemon_service(self):
        self._exec_service_cmd("restart")

    # -------------------------------------------------------------
    # Periodic Metrics Refresh Loop
    # -------------------------------------------------------------
    def update_metrics_loop(self):
        try:
            # Temp
            cpu_c = float(getCPUtemperature())
            unit = self.cfg_data.get("temp_unit", "C")
            temp_val = cpu_c if unit == "C" else (cpu_c * 1.8 + 32)
            color = "#26A69A" if cpu_c < 45 else ("#FFA726" if cpu_c < 60 else "#EF5350")
            self.card_cpu_temp.update_metric(f"{temp_val:.1f} °{unit}", progress_val=cpu_c / 80.0, color=color)

            # CPU Usage
            cpu_u = float(getCPUuse())
            self.card_cpu_usage.update_metric(f"{cpu_u:.1f} %", progress_val=cpu_u / 100.0)

            # RAM Usage
            ram = getRAMinfo()
            if len(ram) >= 2:
                total_mb = round(int(ram[0]) / 1024, 1)
                used_mb = round(int(ram[1]) / 1024, 1)
                ram_perc = round(used_mb / total_mb * 100, 1) if total_mb > 0 else 0
                self.card_ram.update_metric(f"{used_mb}/{total_mb} MB ({ram_perc}%)", progress_val=ram_perc / 100.0)

            # Disk Usage
            d_total, d_used, d_free, d_perc = getDiskSpace()
            self.card_disk.update_metric(f"{d_used}/{d_total} GB ({d_perc}%)", progress_val=d_perc / 100.0)

            # IP Address
            ips = getIP()
            active_ip = ips.get("wlan0") or ips.get("eth0") or "Disconnected"
            self.card_ip.update_metric(active_ip, progress_val=1.0 if active_ip != "Disconnected" else 0.0)

            # Fan Status
            fan_threshold = float(self.cfg_data.get("fan_temp", 50))
            is_fan_on = cpu_c > fan_threshold
            self.card_fan.update_metric(
                "ON (Active Cooling)" if is_fan_on else "OFF (Idle)",
                progress_val=1.0 if is_fan_on else 0.0,
                color="#EF5350" if is_fan_on else "#78909C"
            )
        except Exception as e:
            print(f"Metrics update error: {e}")

        # Re-trigger loop every 2 seconds
        self.after(2000, self.update_metrics_loop)


def main():
    app = PironmanGUI()
    app.mainloop()


if __name__ == "__main__":
    main()
