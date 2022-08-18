#!/usr/bin/env python3
import sys
import time
from app_info import __app_name__

def log(msg:str=None,level='DEBUG',end='\n',flush=False,timestamp=True):
    with open('/opt/%s/log'%__app_name__,'a+') as log_file:
        if timestamp == True:
            _time = time.strftime("%y/%m/%d %H:%M:%S", time.localtime())
            ct = time.time()
            _msecs = '%03d '%((ct - int(ct)) * 1000)
            print('%s,%s[%s] %s'%(_time,_msecs,level,msg), end=end, flush=flush, file=log_file)
            print('%s,%s[%s] %s'%(_time,_msecs,level,msg), end=end, flush=flush, file=sys.stdout)
        else:
            print('%s'%msg, end=end, flush=flush, file=log_file)
            print('%s'%msg, end=end, flush=flush, file=sys.stdout) 

def run_command(cmd):
    import subprocess
    p = subprocess.Popen(
        cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    result = p.stdout.read().decode('utf-8')
    status = p.poll()
    return status, result