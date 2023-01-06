import os
import pwd
import grp
from sys import path


__app_name__ = 'pironman'
__version__ = '1.2.4'

# # user and User home directory
# User = os.popen('echo ${SUDO_USER:-$LOGNAME}').readline().strip()
# UserHome = os.popen('getent passwd %s | cut -d: -f 6'%User).readline().strip()
# print('[app_info] User: %s'%User)  # pi
# print('[app_info] UserHome: %s'%UserHome)  # /home/pi
# Config_file = '%s/.config/%s/config.txt'%(UserHome, App_name)

# import os, sys
# import time
# import pwd
# import grp

# username = os.getlogin()
# gid = pwd.getpwnam(username).pw_gid
# group_name = grp.getgrgid(gid)[0]
# user_home = os.popen('getent passwd %s | cut -d: -f 6'%username).readline().strip()

# user and User home directory
abspath = os.path.abspath(__file__)
statinfo = os.stat(abspath)
uid = statinfo.st_uid
gid = statinfo.st_gid

username = pwd.getpwuid(uid)[0]
group_name = grp.getgrgid(gid)[0]

user_home = os.popen('getent passwd %s | cut -d: -f 6'%username).readline().strip()

config_file = '%s/.config/%s/config.txt'%(user_home, __app_name__)

# print('[app_info] abspath: %s'%abspath)
# print('[app_info] User: %s'%User)
# print('[app_info] UserHome: %s'%UserHome)
# print('[app_info] Config: %s'%Config_file)
