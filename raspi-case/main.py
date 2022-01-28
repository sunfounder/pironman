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
from app_info import App_name, Version, User, UserHome, Config_file
from ws2812 import WS2812

line = '-'*24
_time = time.strftime("%y/%m/%d %H:%M:%S", time.localtime())
log('\n%s%s%s'%(line,_time,line), timestamp=False)
log('%s version: %s'%(App_name, Version), timestamp=False)
log('User: %s'%User, timestamp=False)
log('Config_file: %s \n'%Config_file, timestamp=False)


# region: config 
power_key_pin = 16
fan_pin = 6
rgb_pin = 12
update_frequency = 0.5  # second

fan_temp = 50 # celsius
screen_always_on = False
screen_off_time = 30
rgb_switch = True
rgb_blink_speed = 50
rgb_color = '#0000FF'

config = ConfigParser()
# check Config_file
if not os.path.exists(Config_file):
    log('Configuration file does not exist, recreating ...')
    # check $UserHome/.config
    if not os.path.exists('%s/.config'%UserHome):
        os.mkdir('%s/.config'%UserHome)
        os.popen('sudo chmod 774 %s/.config'%UserHome)  
        run_command('sudo  chown %s %s/.config'%(User, UserHome))  
    # create Config_file
    status, result = run_command(cmd='sudo mkdir -p  %s/.config/%s'%(UserHome, App_name)
        +' && sudo touch %s'%Config_file
        +' && sudo chmod -R 774 %s/.config/%s'%(UserHome, App_name)
        +' && sudo chown -R %s %s/.config/%s'%(User, UserHome, App_name)    
    ) 
    if status != 0:
        log('create Config_file failed:\n%s'%result)
        raise Exception(result)

# read Config_file
try:
    config.read(Config_file)
    fan_temp = float(config['all']['fan_temp'])
    screen_always_on = config['all']['screen_always_on']
    if screen_always_on == 'True':
        screen_always_on = True
    else:
        screen_always_on = False
    screen_off_time = int(config['all']['screen_off_time'])
    rgb_switch = (config['all']['rgb_switch'])
    if rgb_switch == 'False':
        rgb_switch = False
    else:
        rgb_switch = True
    rgb_blink_speed = int(config['all']['rgb_blink_speed'])
    rgb_color = str(config['all']['rgb_color'])
except:
    config['all'] ={
                    'fan_temp':fan_temp,
                    'screen_always_on':screen_always_on,
                    'screen_off_time':screen_off_time,
                    'rgb_switch':rgb_switch,
                    'rgb_blink_speed':rgb_blink_speed,
                    'rgb_color':rgb_color,
                    }
    with open(Config_file, 'w') as f:
        config.write(f)

log("power_key_pin : %s"%power_key_pin) 
log("fan_pin : %s"%fan_pin) 
log("rgb_pin : %s"%rgb_pin) 
log("update_frequency : %s"%update_frequency) 
log("fan_temp : %s"%fan_temp) 
log("screen_always_on : %s"%screen_always_on) 
log("screen_off_time : %s"%screen_off_time) 
log("rgb_switch: %s"%rgb_switch)
log("rgb_blink_speed : %s"%rgb_blink_speed) 
log("rgb_color : %s"%rgb_color) 

# endregion: config

# region: oled init
oled = SSD1306_128_64()
width = oled.width
height = oled.height
oled.begin()
oled.clear()
oled.on()

image = Image.new('1', (width, height))
draw = ImageDraw.Draw(image)
font_8 = ImageFont.truetype('/opt/%s/Minecraftia-Regular.ttf'%App_name, 8)
font_12 = ImageFont.truetype('/opt/%s/Minecraftia-Regular.ttf'%App_name, 12) 

def draw_text(text,x,y,fill=1):
    text = str(text)
    draw.text((x, y), text=text, font=font_8, fill=fill)

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


def main():
    global fan_temp, power_key_pin, screen_off_time, rgb_color, rgb_pin          
    time_start = time.time()
    oled_stat = True
    power_key_flag = False
    power_timer = 0
    strip = WS2812(LED_COUNT=16, LED_PIN=rgb_pin)

    def rgb_show():
        log('rgb_show')
        try:
            strip.display('breath', rgb_color, rgb_blink_speed, 255)
        except Exception as e:
            log(e,level='rgb_strip')
            

    # rgb_strip thread
    if rgb_switch == True:
        rgb_thread = threading.Thread(target=rgb_show)
        rgb_thread.setDaemon(True)
        rgb_thread.start()
    else:
        strip.clear()


    while True:

        # CPU temp
        CPU_temp = float(getCPUtemperature())
         

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
            DISK_perc = float(DISK_stats[3][:-1])  
            # ip address
            # ip = '0.0.0.0'
            wlan0,eth0 = getIP()
            if wlan0 != None:
                ip = wlan0
            elif eth0 != None:
                ip = eth0
            else:
                ip = 'DISCONNECT'
        # display info 
            ip_rect = Rect(48, 0, 81, 10)
            ram_info_rect = Rect(46, 17, 81, 10)
            ram_rect = Rect(46, 29, 81, 10)
            rom_info_rect = Rect(46, 41, 81, 10)
            rom_rect = Rect(46, 53, 81, 10)

            draw_text('CPU',6,0)
            draw.pieslice((0, 12, 30, 42), start=180, end=0, fill=0, outline=1)
            draw.pieslice((0, 12, 30, 42), start=180, end=int(180+180*CPU_usage*0.01), fill=1, outline=1)
            draw_text('{:^5.1f} %'.format(CPU_usage),2,27)
            # Temp
            draw_text('{:>4.1f} \'C'.format(CPU_temp),2,38)
            draw.pieslice((0, 33, 30, 63), start=0, end=180, fill=0, outline=1)
            draw.pieslice((0, 33, 30, 63), start=int(180-180*CPU_temp*0.01), end=180, fill=1, outline=1)
            # RAM
            draw_text('RAM: {}/{} GB'.format(RAM_used,RAM_total),*ram_info_rect.coord())
            # draw_text('{:>5.1f}'.format(RAM_usage)+' %',92,0)
            draw.rectangle(ram_rect.rect(), outline=1, fill=0)
            draw.rectangle(ram_rect.rect(RAM_usage), outline=1, fill=1)
            # Disk 
            draw_text('ROM: {}/{} GB'.format(DISK_used[:-1],DISK_total[:-1]), *rom_info_rect.coord())
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


    # fan control 
        if CPU_temp > fan_temp:
            fan_on()
        elif CPU_temp < fan_temp-10:
            fan_off()

    # power key event
        if get_io(power_key_pin) == 0:
            # screen on
            if oled_stat == False:
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
                text_width, text_height = font_12.getsize('POWER OFF')
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
                os.system('sudo poweroff')
                sys.exit(1)
        else:
            power_key_flag = False    

        time.sleep(0.2)


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

    
