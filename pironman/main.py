import os
import sys
import time
import threading
import RPi.GPIO as GPIO
from configparser import ConfigParser
from PIL import Image,ImageDraw,ImageFont
from oled import SSD1306_128_64
from system_status import *
from utils import log, run_command
from app_info import __app_name__, __version__, username, config_file
from ws2812_RGB import WS2812, RGB_styles

from ha_api import HomeAssistantSupervisorAPI

NORMAL = 0
HOME_ASSISTANT_ADDON = 1

mode = NORMAL

if 'SUPERVISOR_TOKEN' in os.environ:
    mode = HOME_ASSISTANT_ADDON
    ha = HomeAssistantSupervisorAPI(
        "http://supervisor/",
        os.environ['SUPERVISOR_TOKEN']
    )
    log('Home Assistant Addon mode')

# print info
line = '-'*24
_time = time.strftime("%y/%m/%d %H:%M:%S", time.localtime())
log('\n%s%s%s'%(line,_time,line), timestamp=False)
log('%s version: %s'%(__app_name__, __version__), timestamp=False)
log('username: %s'%username, timestamp=False)
log('config_file: %s'%config_file, timestamp=False)
# Kernel Version
status, result = run_command("uname -a")
if status == 0:
    log("\nKernel Version:", timestamp=False)
    log(f"{result}", timestamp=False)
# OS Version
status, result = run_command("lsb_release -a|grep Description")
if status == 0:
    log("OS Version:", timestamp=False)
    log(f"{result}", timestamp=False)
# PCB information
status, result = run_command("cat /proc/cpuinfo|grep -E \'Revision|Model\'")
if status == 0:
    log("PCB info:", timestamp=False)
    log(f"{result}", timestamp=False)

# region: config
power_key_pin = 16
fan_pin = 6
rgb_pin = 10
update_frequency = 0.5  # second

temp_unit = 'C' # 'C' or 'F'
fan_temp = 50 # celsius
screen_always_on = False
screen_off_time = 60
rgb_enable = True
rgb_switch = True
rgb_style = 'breath'  # 'breath', 'leap', 'flow', 'raise_up', 'colorful', 'colorful_leap'
rgb_color = '0a1aff'
rgb_blink_speed = 50
rgb_pwm_freq = 1000 # kHz

temp_lower_set = 2 # celsius, lower the fan temperature setting ( fan_temp ), the fan will turn off

config = ConfigParser()
# check config_file
if not os.path.exists(config_file):
    log('Configuration file does not exist, recreating ...')
    # create config_file
    status, result = run_command(cmd=f'sudo touch {config_file}'
        + f' && sudo chmod 774 {config_file}'
    )
    if status != 0:
        log('create config_file failed:\n%s'%result)
        raise Exception(result)

# read config_file
try:
    config.read(config_file)
    temp_unit = config['all']['temp_unit']
    fan_temp = float(config['all']['fan_temp'])
    screen_always_on = config['all']['screen_always_on']
    if screen_always_on == 'True':
        screen_always_on = True
    else:
        screen_always_on = False
    screen_off_time = int(config['all']['screen_off_time'])
    rgb_enable = (config['all']['rgb_enable'])
    if rgb_enable == 'False':
        rgb_enable = False
    else:
        rgb_enable = True
    rgb_switch = (config['all']['rgb_switch'])
    if rgb_switch == 'False':
        rgb_switch = False
    else:
        rgb_switch = True
    rgb_style = str(config['all']['rgb_style'])
    rgb_color = str(config['all']['rgb_color'])
    rgb_blink_speed = int(config['all']['rgb_blink_speed'])
    rgb_pwm_freq = int(config['all']['rgb_pwm_freq'])
    rgb_pin = int(config['all']['rgb_pin'])
except Exception as e:
    log(f"read config error: {e}")
    config['all'] ={
                    'temp_unit':temp_unit,
                    'fan_temp':fan_temp,
                    'screen_always_on':screen_always_on,
                    'screen_off_time':screen_off_time,
                    'rgb_enable':rgb_enable,
                    'rgb_switch':rgb_switch,
                    'rgb_style':rgb_style,
                    'rgb_color':rgb_color,
                    'rgb_blink_speed':rgb_blink_speed,
                    'rgb_pwm_freq':rgb_pwm_freq,
                    'rgb_pin':rgb_pin,
                    }
    with open(config_file, 'w') as f:
        config.write(f)

log("power_key_pin : %s"%power_key_pin)
log("fan_pin : %s"%fan_pin)
log("update_frequency : %s"%update_frequency)
log("temp_unit : %s"%temp_unit)
log("fan_temp : %s"%fan_temp)
log("screen_always_on : %s"%screen_always_on)
log("screen_off_time : %s"%screen_off_time)
log("rgb_enable : %s"%rgb_enable)
log("rgb_switch: %s"%rgb_switch)
log("rgb_style : %s"%rgb_style)
log("rgb_color : %s"%rgb_color)
log("rgb_blink_speed : %s"%rgb_blink_speed)
log("rgb_pwm_freq : %s"%rgb_pwm_freq)
log("rgb_pin : %s"%rgb_pin)
log("\n")
# endregion: config

# region: oled init
oled_ok = False
oled_stat = False

if rgb_enable:
    from ws2812_RGB import WS2812, RGB_styles

try:
    run_command("sudo modprobe i2c-dev")
    oled = SSD1306_128_64()
    width = oled.width
    height = oled.height
    oled.begin()
    oled.clear()
    oled.on()

    image = Image.new('1', (width, height))
    draw = ImageDraw.Draw(image)
    font_8 = ImageFont.truetype('/opt/%s/Minecraftia-Regular.ttf'%__app_name__, 8)
    font_12 = ImageFont.truetype('/opt/%s/Minecraftia-Regular.ttf'%__app_name__, 12)

    def draw_text(text,x,y,fill=1):
        text = str(text)
        draw.text((x, y), text=text, font=font_8, fill=fill)

    oled_ok = True
    oled_stat = True
    log('oled init success')
except Exception as e:
    log('oled init failed:\n%s'%e)
    oled_ok = False
    oled_stat = False

#endregion: oled init

# region: io control
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

def set_io(pin,val:bool):
    GPIO.setup(pin,GPIO.OUT)
    GPIO.output(pin,val)

def get_io(pin):
    GPIO.setup(pin,GPIO.IN)
    return GPIO.input(pin)

def fan_on():
    global fan_pin
    set_io(fan_pin,1)

def fan_off():
    global fan_pin
    set_io(fan_pin,0)

# endregion: io control

# region: rgb_strip init
try:
    strip = WS2812(LED_COUNT=16, LED_PIN=rgb_pin, LED_FREQ_HZ=rgb_pwm_freq*1000)
except Exception as e:
    log('rgb_strip init failed:\n%s'%e)
    rgb_switch = False

def rgb_show():
    log('rgb_show')
    try:
        if rgb_style in RGB_styles:
            log('rgb_show: %s'%rgb_style)
            strip.display(rgb_style, rgb_color, rgb_blink_speed, 255)
        else:
            log('rgb_style not in RGB_styles')
    except Exception as e:
        log(e,level='rgb_strip')

# endregion: rgb_strip init

def getIPAddress():
    ip = None
    if mode == NORMAL:
        IPs = getIP()
    elif mode == HOME_ASSISTANT_ADDON:
        IPs = ha.get_ip()
        if len(IPs) == 0:
            IPs = getIP()
    log("Got IPs: %s" %IPs)
    if 'wlan0' in IPs and IPs['wlan0'] != None and IPs['wlan0'] != '':
        ip = IPs['wlan0']
    elif 'eth0' in IPs and IPs['eth0'] != None and IPs['eth0'] != '':
        ip = IPs['eth0']
    elif len(IPs.keys()) > 0:
        interface = list(IPs.keys())[0]
        if IPs[interface] != None and IPs[interface] != '':
            ip = IPs[list(IPs.keys())[0]]
        else:
            ip = 'DISCONNECT'
    else:
        ip = 'DISCONNECT'

    return ip


def main():
    global fan_temp, power_key_pin, screen_off_time, rgb_color, rgb_pin
    global oled_stat
    time_start = time.time()
    power_key_flag = False
    power_timer = 0
    if rgb_enable:
        # rgb_strip thread
        if rgb_switch == True:
            rgb_thread = threading.Thread(target=rgb_show)
            rgb_thread.daemon = True
            rgb_thread.start()
        else:
            strip.clear()


    ip = 'DISCONNECT'

    while True:

        # CPU temp
        CPU_temp_C = float(getCPUtemperature()) # celcius
        CPU_temp_F = float(CPU_temp_C * 1.8 + 32) # fahrenheit

        # fan control
        if temp_unit == 'C':
            if CPU_temp_C > fan_temp:
                fan_on()
            elif CPU_temp_C < fan_temp - temp_lower_set:
                fan_off()
        elif temp_unit == 'F':
            if CPU_temp_F > fan_temp:
                fan_on()
            elif CPU_temp_F < fan_temp - temp_lower_set*1.8:
                fan_off()
        else:
            log('temp_unit error, use defalut value: 50\'C')
            if CPU_temp_C > 50:
                fan_on()
            elif CPU_temp_C < 40:
                fan_off()

        # oled control
        if oled_ok:
            if oled_stat == True:
                # CPU usage
                CPU_usage = float(getCPUuse())
                # clear draw buffer
                draw.rectangle((0,0,width,height), outline=0, fill=0)
                # get info
                # RAM
                RAM_stats = getRAMinfo()
                RAM_total = round(int(RAM_stats[0]) / 1024/1024,1)
                RAM_used = round(int(RAM_stats[1]) / 1024/1024,1)
                RAM_usage = round(RAM_used/RAM_total*100,1)
                # Disk information
                DISK_stats = getDiskSpace()
                DISK_total = str(DISK_stats[0])
                DISK_used = str(DISK_stats[1])
                DISK_perc = float(DISK_stats[3])

                # display info
                ip_rect = Rect(48, 0, 81, 10)
                ram_info_rect = Rect(46, 17, 81, 10)
                ram_rect = Rect(46, 29, 81, 10)
                rom_info_rect = Rect(46, 41, 81, 10)
                rom_rect = Rect(46, 53, 81, 10)

                # get ip if disconnected
                if ip == 'DISCONNECT':
                    ip = getIPAddress()

                draw_text('CPU',6,0)
                draw.pieslice((0, 12, 30, 42), start=180, end=0, fill=0, outline=1)
                draw.pieslice((0, 12, 30, 42), start=180, end=int(180+180*CPU_usage*0.01), fill=1, outline=1)
                draw_text('{:^5.1f} %'.format(CPU_usage),2,27)
                # Temp
                if temp_unit == 'C':
                    draw_text('{:>4.1f} \'C'.format(CPU_temp_C),2,38)
                    draw.pieslice((0, 33, 30, 63), start=0, end=180, fill=0, outline=1)
                    draw.pieslice((0, 33, 30, 63), start=int(180-180*CPU_temp_C*0.01), end=180, fill=1, outline=1)
                elif temp_unit == 'F':
                    draw_text('{:>4.1f} \'F'.format(CPU_temp_F),2,38)
                    draw.pieslice((0, 33, 30, 63), start=0, end=180, fill=0, outline=1)
                    pcent = (CPU_temp_F-32)/1.8
                    draw.pieslice((0, 33, 30, 63), start=int(180-180*pcent*0.01), end=180, fill=1, outline=1)
                # RAM
                draw_text('RAM: {}/{} GB'.format(RAM_used,RAM_total),*ram_info_rect.coord())
                # draw_text('{:>5.1f}'.format(RAM_usage)+' %',92,0)
                draw.rectangle(ram_rect.rect(), outline=1, fill=0)
                draw.rectangle(ram_rect.rect(RAM_usage), outline=1, fill=1)
                # Disk
                draw_text('ROM: {}/{} GB'.format(DISK_used ,DISK_total), *rom_info_rect.coord())
                # draw_text('     ',72,32)
                # draw_text(''+' G',72,32)
                draw.rectangle(rom_rect.rect(), outline=1, fill=0)
                draw.rectangle(rom_rect.rect(DISK_perc), outline=1, fill=1)
                # IP
                draw.rectangle((ip_rect.x-13,ip_rect.y,ip_rect.x+ip_rect.width,ip_rect.height), outline=1, fill=1)
                draw.pieslice((ip_rect.x-25,ip_rect.y,ip_rect.x-3,ip_rect.height+10), start=270, end=0, fill=0, outline=0)
                draw_text(ip,*ip_rect.coord(),0)
                # draw the image buffer.
                oled.image(image)
                oled.display()

            # screen off timer
            if screen_always_on == False and (time.time()-time_start) > screen_off_time:
                oled.off()
                oled_stat = False

            # power key event
            if get_io(power_key_pin) == 0:
                # screen on
                if oled_ok and oled_stat == False:
                    oled.on()
                    oled_stat = True
                    time_start = time.time()
                # power off
                if power_key_flag == False:
                    power_key_flag = True
                    power_timer = time.time()
                elif (time.time()-power_timer) > 2:
                    oled.on()
                    draw.rectangle((0,0,width,height), outline=0, fill=0)
                    # draw_text('POWER OFF',36,24)
                    left, top, right, bottom = font_12.getbbox('POWER OFF')
                    text_width = right - left
                    text_height = bottom - top
                    text_x = int((width - text_width)/2-1)
                    text_y = int((height - text_height)/2-1)
                    draw.text((text_x, text_y), text='POWER OFF', font=font_12, fill=1)
                    oled.image(image)
                    oled.display()
                    while not get_io(power_key_pin):
                        time.sleep(0.01)
                    log("POWER OFF")
                    oled_stat = False
                    oled.off()
                    if mode == HOME_ASSISTANT_ADDON:
                        ha.shutdown() # shutdown homeassistant host
                    else:
                        os.system('poweroff')
                        sys.exit(1)
            else:
                power_key_flag = False

        time.sleep(update_frequency)


class Rect:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.x2 = self.x + self.width
        self.y2 = self.y + self.height

    def coord(self):
        return (self.x, self.y)
    def rect(self, pecent=100):
        return (self.x, self.y, self.x + int(self.width*pecent/100.0), self.y2)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        log('error')
        log(e)
    finally:
        GPIO.cleanup()


