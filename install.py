#!/usr/bin/env python3
import os
import sys
import time
sys.path.append('./pironman')
from app_info import __app_name__, __version__, username, user_home, config_file

# user and username home directory

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
    'rpi-ws281x',
    'pillow',
]


def run_command(cmd=""):
    import subprocess
    p = subprocess.Popen(
        cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
    result = p.stdout.read()
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

def set_config(msg="", name="", value=""):
    print(" - %s... " % (msg), end='', flush=True)
    try:
        Config().set(name, value)
        print('Done')
    except Exception as e:
        print('\033[1;35mError\033[0m')
        errors.append("%s error:\n Error:%s" %(msg, e))       

class Config(object):
    '''
        To setup /boot/config.txt
    '''

    def __init__(self, file="/boot/config.txt"):
        self.file = file
        with open(self.file, 'r') as f:
            self.configs = f.read()
        self.configs = self.configs.split('\n')

    def remove(self, expected):
        for config in self.configs:
            if expected in config:
                self.configs.remove(config)
        return self.write_file()

    def set(self, name, value=None):
        have_excepted = False
        for i in range(len(self.configs)):
            config = self.configs[i]
            if name in config:
                have_excepted = True
                tmp = name
                if value != None:
                    tmp += '=' + value
                self.configs[i] = tmp
                break

        if not have_excepted:
            tmp = name
            if value != None:
                tmp += '=' + value
            self.configs.append(tmp)
        return self.write_file()

    def write_file(self):
        try:
            config = '\n'.join(self.configs)
            with open(self.file, 'w') as f:
                f.write(config)
            return 0, config
        except Exception as e:
            return -1, e


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
    print(f"{__app_name__} {__version__} install process starts:")
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
    # do(msg="enable i2c",
    #     cmd='sudo raspi-config nonint do_i2c 0'
    # )
    set_config(msg="enable i2c",
        name="dtparam=i2c_arm",
        value="on"
    )
    set_config(msg="disable audio",
        name="dtparam=audio",
        value="off"
    )
    # dtoverlay=gpio-poweroff,gpio_pin=26,active_low=0
    # dtoverlay=gpio-ir,gpio_pin=13
    set_config(msg="config gpio-poweroff",
        name="dtoverlay=gpio-poweroff,gpio_pin",
        value="26,active_low=0\n"
    )
    set_config(msg="config gpio-ir",
        name="dtoverlay=gpio-ir,gpio_pin",
        value="13\n"
    )
    #
    print('create WorkingDirectory')
    do(msg="create /opt",
        cmd='sudo mkdir -p /opt'
        +' && sudo chmod -R 774 /opt'
        +' && sudo chown -R %s:%s /opt'%(username, username)
    )
    do(msg="create dir",
        cmd='sudo mkdir -p /opt/%s'%__app_name__
        +' && sudo chmod -R 774 /opt/%s'%__app_name__
        +' && sudo chown %s:%s /opt/%s'%(username, username, __app_name__)
    )
    #
    do(msg='copy service file',
        cmd='sudo cp -rpf ./bin/%s.service /usr/lib/systemd/system/%s.service '%(__app_name__, __app_name__)
        +' && sudo cp -rpf ./bin/%s /usr/local/bin/%s'%(__app_name__, __app_name__)
        +' && sudo cp -rpf ./%s/* /opt/%s/'%(__app_name__, __app_name__)
    )
    do(msg="add excutable mode for service file",
        cmd='sudo chmod +x /usr/lib/systemd/system/%s.service'%__app_name__
        +' && sudo chmod +x /usr/local/bin/%s'%__app_name__
        +' && sudo chmod -R 774 /opt/%s'%__app_name__
        +' && sudo chown -R %s:%s /opt/%s'%(username, username, __app_name__)
    )
    #
    print('create config file')
    if not os.path.exists('%s/.config'%user_home):
        os.mkdir('%s/.config'%user_home)
        os.popen('sudo chmod 774 %s/.config'%user_home)
        run_command('sudo  chown %s:%s %s/.config'%(username, username, user_home))
    do(msg='copy config file',
        cmd='sudo mkdir -p %s/.config/%s '%(user_home, __app_name__)
        +' && sudo cp -rpf ./config.txt %s/.config/%s/config.txt '%(user_home, __app_name__)
        +' && sudo chown  -R %s:%s %s/.config/%s'%(username, username, user_home, __app_name__)
    )
    #
    print('check startup files')
    run_command('sudo systemctl daemon-reload')
    status, result = run_command('sudo systemctl list-unit-files|grep %s'%__app_name__)
    if status==0 or status==None and result.find('%s.service'%__app_name__) != -1:
        do(msg='enable the service to auto-start at boot',
            cmd='sudo systemctl enable %s.service'%__app_name__
        )
    else:
        errors.append("%s error:\n  Status:%s\n  Error:%s" %
                      ('check startup files ', status, result))
    #
    time.sleep(0.1)
    do(msg='run the service',
        cmd='sudo pironman restart'
    )

    if len(errors) == 0:
        print("Finished.")
        print("\033[1;32mWhether to restart for the changes to take effect(Y/N):\033[0m")
        while True:
            key = input()
            # print(f'key: {key}')
            if key == 'Y' or key == 'y':
                # print(f'reboot')
                run_command('sudo reboot')
            elif key == 'N' or key == 'n':
                print(f'exit')
                sys.exit(0)
            else:
                continue
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
