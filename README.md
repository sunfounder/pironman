# SunFounder Pironman for Raspberry Pi
This repository is for SunFounder Pironman - A PC case for Raspberry Pi. you can buy it on [our website](https://www.sunfounder.com/products/raspberry-pi-4-case), or search sunfounder in Amazon.

Quick Links:

- [SunFounder Pironman for Raspberry Pi](#sunfounder-pironman-for-raspberry-pi)
  - [About pironman](#about-pironman)
  - [Install](#install)
  - [Usage](#usage)
  - [Update](#update)
  - [Compatible Systems](#compatible-systems)
  - [About SunFounder](#about-sunfounder)
  - [License](#license)
  - [Contact us](#contact-us)

<a id="about_pironman"></a>
## About pironman:
<div align="center">
    <img src="https://github.com/sunfounder/pironman/blob/docs/docs/source/img/pironman.png" width="50%"  align="center" title="pironman"/>
    &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
    <!-- <img src="./img/Nano_Sloth_V2.png" width="212" height="261" align="center" title="Nano_Sloth_V2"/> -->
</div>
The pironman is used on Raspberry Pi to control OLED to display system status information, control cooling fan and RGB light strip and so on.


<a id="update"></a>

## Install
- For systems that don't have git, python3 and pip pre-installed you need to install them first
  ```bash
  sudo apt-get update
  sudo apt-get install git -y
  sudo apt-get install python3 python3-pip python3-setuptools -y
  ```
- Execute the installation script
  ```bash
  cd ~
  git clone https://github.com/sunfounder/pironman.git
  cd ~/pironman
  sudo python3 install.py
  ```

## Usage
```bash
Usage:
  pironman <OPTION> <input>

Options:
  start            start pironman service
  stop             stop pironman service
  restart          restart pironman service
  -h,--help        help, show this help
  -c,--check       show all configurations
  -a,--auto        [ on ],enable auto-start at boot
                   [ off ], disable auto-start at boot
  -u,--unit        [ C/F ], set the unit of temperature,
                       C or F (Celsius/Fahrenheit)
  -f,--fan         [ temp ], Temperature at which the fan switches on,
                   in celsius (default 50),in range (30 ~ 80)
  -al,--always_on  [on/off], whether the screen is always on,
                   default False
  -s,--staty_time  [time], screen display duration in second,
                   in second, default 30
  -rw,--rgb_sw     [on/off], rgb strip switch
  -rs,--rgb_style  rgb strip display style, default: breath,
                   in [breath / leap / flow / raise_up / colorful]
  -rc,--rgb_color  [(HEX)color], set the color of rgb strip,
                   default: 0a1aff
  -rb,--rgb_speed  [speed], rgb blink speed (0 ~ 100, default 50)
  -pwm,--rgb_pwm   [frequency], rgb signal frequency (400 ~ 1600, default 1000 kHz)

```
## Update
https://github.com/sunfounder/pironman/blob/master/CHANGELOG.md

## Compatible Systems
Systems that passed the test on the Raspberry Pi 4B:
<font size=1>
<!-- https://apps.timwhitlock.info/emoji/tables/unicode#block-6c-other-additional-symbols -->
  | system |   is compatible ? |
  | :---   | :---:   |
  | Raspberry Pi OS - Bullseye (32/64 bit) | &#x2705; |
  | Raspberry Pi OS lite - Bullseye (32/64 bit) | &#x2705; |
  | Raspberry Pi OS - Buster (32 bit) | &#x2705; |
  | Raspberry Pi OS lite - Buster (32 bit) | &#x2705; |
  | Ubuntu Server 22.10 (32/64 bit) | &#x2705; |
  | Ubuntu Desktop 22.10 (64 bit) | &#x2705; |
  | Kali Linux (32/64 bit) | &#x2705; |
  | OSMC | &#x2705; |
  | RetroPie | &#x2705; |
  | OctoPi | &#x2705; |
  | Homebridge | &#x2705; |
  | LibreELEC | &#x274C; |
  | HassOS | &#x274C; |
</font>

<a id="about_sunfounder"></a>
## About SunFounder
SunFounder is a company focused on STEAM education with products like open source robots, development boards, STEAM kit, modules, tools and other smart devices distributed globally. In SunFounder, we strive to help elementary and middle school students as well as hobbyists, through STEAM education, strengthen their hands-on practices and problem-solving abilities. In this way, we hope to disseminate knowledge and provide skill training in a full-of-joy way, thus fostering your interest in programming and making, and exposing you to a fascinating world of science and engineering. To embrace the future of artificial intelligence, it is urgent and meaningful to learn abundant STEAM knowledge.

<a id="license"></a>
## License
This is the code for SunFounder PiArm.
This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program; if not, write to the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

piarm comes with ABSOLUTELY NO WARRANTY; for details run ./show w. This is free software, and you are welcome to redistribute it under certain conditions; run ./show c for details.

SunFounder, Inc., hereby disclaims all copyright interest in the program 'piarm' (which makes passes at compilers).

Mike Huang, 21 August 2020

Mike Huang, Chief Executive Officer

Email: service@sunfounder.com

<a id="contact_us"></a>
## Contact us
website:
    www.sunfounder.com

E-mail:
    service@sunfounder.com
