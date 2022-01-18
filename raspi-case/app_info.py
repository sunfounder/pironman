import os
import sys

App_name = 'raspi-case'
Version = '0.0.2'

# user and User home directory
User = os.popen('echo ${SUDO_USER:-$LOGNAME}').readline().strip()
UserHome = os.popen('getent passwd %s | cut -d: -f 6'%User).readline().strip()
print('[app_info] User: %s'%User)  # pi
print('[app_info] UserHome: %s'%UserHome)  # /home/pi
Config_file = '%s/.config/%s/config'%(UserHome, App_name)