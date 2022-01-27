import os
import pwd
import grp
from sys import path


App_name = 'raspi-case'
Version = '0.0.2'

# # user and User home directory 
# User = os.popen('echo ${SUDO_USER:-$LOGNAME}').readline().strip()
# UserHome = os.popen('getent passwd %s | cut -d: -f 6'%User).readline().strip()
# print('[app_info] User: %s'%User)  # pi
# print('[app_info] UserHome: %s'%UserHome)  # /home/pi
# Config_file = '%s/.config/%s/config.txt'%(UserHome, App_name)

# user and User home directory
abspath = os.path.abspath(__file__)
statinfo = os.stat(abspath)
uid = statinfo.st_uid
gid = statinfo.st_gid

User = pwd.getpwuid(uid)[0]
Group = grp.getgrgid(gid)[0]

UserHome = os.popen('getent passwd %s | cut -d: -f 6'%User).readline().strip()
Config_file = '%s/.config/%s/config.txt'%(UserHome, App_name)

print('[app_info] abspath: %s'%abspath) 
print('[app_info] User: %s'%User)  
print('[app_info] UserHome: %s'%UserHome)  
print('[app_info] Config: %s'%Config_file) 
