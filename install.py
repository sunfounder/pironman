#!/usr/bin/env python3
import os
import sys
import time

# user and User home directory
User = os.popen('echo ${SUDO_USER:-$LOGNAME}').readline().strip()
UserHome = os.popen('getent passwd %s | cut -d: -f 6'%User).readline().strip()
# print(User)  # pi
# print(UserHome) # /home/pi
app_name  =  'raspi-case'

errors = []

avaiable_options = ['-h', '--help', '--no-dep']

usage = '''
Usage:
    sudo python3 install.py [option]

Options:
               --no-dep    Do not download dependencies
    -h         --help      Show this help text and exit
'''


APT_INSTALL_LIST = [ 
    # 'python3-pip',
    'python3-smbus',
    'i2c-tools',
    'libopenjp2-7 ',
    'libtiff5',

]


PIP_INSTALL_LIST = [
    'rpi_ws281x',
    'pillow',
]


def run_command(cmd=""):
    import subprocess
    p = subprocess.Popen(
        cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    result = p.stdout.read().decode('utf-8')
    status = p.poll()
    return status, result


def do(msg="", cmd=""):
    print(" - %s... " % (msg), end='', flush=True)
    status, result = run_command(cmd)
    if status == 0 or status == None or result == "":
        print('Done')
    else:   
        print('\033[1;35mError\033[0m')
        errors.append("%s error:\n  Status:%s\n  Error:%s" %
                      (msg, status, result))


def install(): 

    options = []
    if len(sys.argv) > 1:
        options = sys.argv[1:]
        for opt in options:
            if opt not in avaiable_options:
                print("Option {} is not found.".format(opt))
                print(usage)
                quit()
        if "-h" in options or "--help" in options:
            print(usage)
            quit()
    #  
    print("%s install process starts"%app_name)
    if "--no-dep" not in options:    
        do(msg="update apt",
            cmd='sudo apt update -y'
        )
        do(msg="update pip3",
            cmd='python3 -m pip install --upgrade pip'
        )
        print("Install dependency")
        for dep in APT_INSTALL_LIST:
            do(msg="install %s"%dep,
                cmd='sudo apt install %s -y'%dep)
        for dep in PIP_INSTALL_LIST:
            do(msg="install %s"%dep,
                cmd='sudo pip3 install %s'%dep)
    #
    do(msg="enable i2c",
        cmd='sudo raspi-config nonint do_i2c 0'
    )   
    #
    print('create WorkingDirectory')    
    if not os.path.exists('/opt'):
        os.mkdir('/opt')
        os.popen('sudo chmod 774 /opt')       
    do(msg="create dir",
        cmd='sudo mkdir -p /opt/%s'%app_name
        +' && sudo chmod 774 /opt/%s'%app_name  
        +' && sudo chown %s:%s /opt/%s'%(User, User, app_name) 
    )
    #
    do(msg='copy service file',
        cmd='sudo cp -rpf ./bin/%s.service /usr/lib/systemd/system/%s.service '%(app_name, app_name)
        +' && sudo cp -rpf ./bin/%s /usr/local/bin/%s'%(app_name, app_name)
        +' && sudo cp -rpf ./%s/* /opt/%s/'%(app_name, app_name)
    ) 
    do(msg="add excutable mode for service file",
        cmd='sudo chmod +x /usr/lib/systemd/system/%s.service'%app_name
        +' && sudo chmod +x /usr/local/bin/%s'%app_name
        +' && sudo chmod -R 774 /opt/%s'%app_name
        +' && sudo chown -R %s:%s /opt/%s'%(User, User, app_name)
    ) 
    #
    print('create config file')
    if not os.path.exists('%s/.config'%UserHome):
        os.mkdir('%s/.config'%UserHome)
        os.popen('sudo chmod 774 %s/.config'%UserHome)  
        run_command('sudo  chown %s:%s %s/.config'%(User, User, UserHome))    
    do(msg='copy config file',
        cmd='sudo mkdir -p %s/.config/%s '%(UserHome, app_name)
        +' && sudo cp -rpf ./config.txt %s/.config/%s/config.txt '%(UserHome, app_name)
        +' && sudo chown  -R %s:%s %s/.config/%s'%(User, User, UserHome, app_name)
    )
    #     
    print('check startup files')
    run_command('sudo systemctl daemon-reload')
    status, result = run_command('sudo systemctl list-unit-files|grep %s'%app_name)
    if status==0 and result.find('%s.service'%app_name) != -1:
        do(msg='enable the service to auto-start at boot',
            cmd='sudo systemctl enable %s.service'%app_name
        )
    else:
        errors.append("%s error:\n  Status:%s\n  Error:%s" %
                      ('check startup files ', status, result))                  
    #
    # do(msg='run the service',
    #     cmd='sudo systemctl restart %s.service'%app_name
    # )
    do(msg='run the service',
        cmd='sudo raspi-case restart'
    )

    if len(errors) == 0:
        print("Finished.")
        print("You can manually clear the installation files now.")
    else:
        print('\n\n\033[1;35mError happened in install process:\033[0m')
        for error in errors:
            print(error)
        print("Try to fix it yourself, or contact service@sunfounder.com with this message")
        sys.exit(1)    

    
if __name__ == "__main__":
    try:
       install() 
    except KeyboardInterrupt:
        print("\n\nCanceled.")
