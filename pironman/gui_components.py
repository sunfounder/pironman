import tkinter as tk
from tkinter import ttk
import configparser
import os
import subprocess

try:
    import customtkinter as ctk
except ImportError:
    import sys
    print("customtkinter is required. Installing customtkinter...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "customtkinter"])
    import customtkinter as ctk


class MetricCard(ctk.CTkFrame):
    """Card widget for displaying real-time system metrics (CPU, RAM, Temp, etc.)"""
    def __init__(self, master, title="Metric", value="--", unit="", progress=0.0, color="#1f538d", **kwargs):
        super().__init__(master, **kwargs)

        self.title_label = ctk.CTkLabel(self, text=title, font=ctk.CTkFont(size=13, weight="bold"), text_color="gray70")
        self.title_label.pack(anchor="w", padx=15, pady=(10, 2))

        self.value_label = ctk.CTkLabel(self, text=f"{value} {unit}".strip(), font=ctk.CTkFont(size=22, weight="bold"))
        self.value_label.pack(anchor="w", padx=15, pady=(0, 8))

        self.progress_bar = ctk.CTkProgressBar(self, height=8, progress_color=color)
        self.progress_bar.set(progress)
        self.progress_bar.pack(fill="x", padx=15, pady=(0, 12))

    def update_metric(self, value_str, progress_val=None, color=None):
        self.value_label.configure(text=value_str)
        if progress_val is not None:
            self.progress_bar.set(max(0.0, min(1.0, progress_val)))
        if color:
            self.progress_bar.configure(progress_color=color)


class ColorPickerWidget(ctk.CTkFrame):
    """RGB Color palette selector with preset buttons and custom hex input"""
    PRESET_COLORS = [
        ("#0a1aff", "Royal Blue"),
        ("#ff0000", "Red"),
        ("#00ff00", "Green"),
        ("#ffff00", "Yellow"),
        ("#ff00ff", "Magenta"),
        ("#00ffff", "Cyan"),
        ("#ff8800", "Orange"),
        ("#ffffff", "White"),
    ]

    def __init__(self, master, current_hex="0a1aff", on_color_change=None, **kwargs):
        super().__init__(master, **kwargs)
        self.on_color_change = on_color_change

        self.label = ctk.CTkLabel(self, text="RGB Color Selection", font=ctk.CTkFont(size=14, weight="bold"))
        self.label.pack(anchor="w", padx=10, pady=5)

        # Preset buttons container
        self.presets_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.presets_frame.pack(fill="x", padx=10, pady=5)

        for hex_code, name in self.PRESET_COLORS:
            btn = ctk.CTkButton(
                self.presets_frame,
                text="",
                width=28,
                height=28,
                fg_color=hex_code,
                hover_color=hex_code,
                command=lambda h=hex_code: self.set_color(h)
            )
            btn.pack(side="left", padx=3)

        # Custom HEX entry
        self.entry_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.entry_frame.pack(fill="x", padx=10, pady=10)

        ctk.CTkLabel(self.entry_frame, text="HEX Code: #").pack(side="left", padx=(0, 2))
        
        clean_hex = current_hex.replace("#", "")
        self.hex_entry = ctk.CTkEntry(self.entry_frame, width=90)
        self.hex_entry.insert(0, clean_hex)
        self.hex_entry.pack(side="left", padx=5)

        self.preview_box = ctk.CTkButton(
            self.entry_frame,
            text="",
            width=32,
            height=32,
            fg_color=f"#{clean_hex}",
            state="disabled"
        )
        self.preview_box.pack(side="left", padx=10)

        self.apply_btn = ctk.CTkButton(
            self.entry_frame,
            text="Apply Hex",
            width=80,
            command=self._apply_from_entry
        )
        self.apply_btn.pack(side="left", padx=5)

    def set_color(self, hex_code):
        clean_hex = hex_code.replace("#", "")
        self.hex_entry.delete(0, "end")
        self.hex_entry.insert(0, clean_hex)
        self.preview_box.configure(fg_color=f"#{clean_hex}")
        if self.on_color_change:
            self.on_color_change(clean_hex)

    def _apply_from_entry(self):
        val = self.hex_entry.get().strip().replace("#", "")
        if len(val) == 6:
            self.set_color(val)

    def get_color(self):
        return self.hex_entry.get().strip().replace("#", "")


class LogViewerWidget(ctk.CTkFrame):
    """Real-time log file stream viewer"""
    def __init__(self, master, log_path="/opt/pironman/log", **kwargs):
        super().__init__(master, **kwargs)
        self.log_path = log_path

        self.header = ctk.CTkFrame(self, fg_color="transparent")
        self.header.pack(fill="x", padx=10, pady=5)

        ctk.CTkLabel(self.header, text="System Log (/opt/pironman/log)", font=ctk.CTkFont(size=14, weight="bold")).pack(side="left")
        ctk.CTkButton(self.header, text="Refresh Logs", width=100, command=self.refresh_logs).pack(side="right")

        self.textbox = ctk.CTkTextbox(self, font=ctk.CTkFont(family="Courier", size=11))
        self.textbox.pack(fill="both", expand=True, padx=10, pady=10)

        self.refresh_logs()

    def refresh_logs(self):
        self.textbox.configure(state="normal")
        self.textbox.delete("1.0", "end")
        if os.path.exists(self.log_path):
            try:
                with open(self.log_path, "r", errors="ignore") as f:
                    lines = f.readlines()[-150:]  # Last 150 lines
                    self.textbox.insert("1.0", "".join(lines))
            except Exception as e:
                self.textbox.insert("1.0", f"Error reading log file: {e}")
        else:
            self.textbox.insert("1.0", "Log file /opt/pironman/log does not exist yet.")
        self.textbox.see("end")
        self.textbox.configure(state="disabled")
