# Change Log

## [2.2.8] - 2024-3-27

### Added

- Add rgb styles : static, colorful_static

## [2.2.7] - 2024-3-15

### Changed

- Change the default path of boot config to '/boot/firmware/config.txt'

## [2.2.6] - 2024-2-20

### Optimized

- Optimize the exit handler
- Optimize the getting of the system status

## [2.2.5] - 2024-2-19

### Fixed

- Fix the bug that the shutdown button is invalid when OLED initialization fails
- Fix the bug of getting CPU usage on bookworm system

### Optimized

- Optimize the exit handler (clean oled, close rgb strip)

## [2.2.4] - 2023-12-20

### Fixed

- Fix bug of get CPU temperature on bookworm system
- Fix bug of not error info returned when running installation

## [2.2.3] - 2023-9-4

### Fixed

- Fix bug of determining whether the run_command is executed successfully in the install.py

## [2.2.2] - 2023-8-31

### Fixed

- Fix the bug that the pironman script did not kill the process correctly
- Fix the bug of print input parameters

### Added

- Add rgb style ：'colorful_leap'

## [2.2.1] - 2023-7-28

### Changed

- merge with test branch with hassio pluggin support

### Fixed

- Fix bug of reset config file

## [2.2.0] - 2023-7-28

### Changed

- Change config.txt path to '/opt/pironman/config.txt' to solve
the problem that the user name cannot be obtained correctly

### Fixed

- Fix bug of reset config file

## [2.1.2] - 2023-7-14

### Fixed

- Fix the bug of rgb flashing in confusion when use pwm io and the
"dtparam=audio=on"

## [2.1.1] - 2023-7-12

### Fixed

- Fix the bug of the cursor does not display when the program terminates

## [2.1.0] - 2023-7-10

### Changed

Add the option "--break-system-packages" for "pip3" to "install.py" to compatibile the Ubuntu 23.0 PEP668 restrictions
Add tip "Run with sudo" for "install.py"

## [2.0.1] - 2023-7-6

### Changed

- Remove control of the "dtparam=audio" in /boot/config.txt

## [2.0.0] - 2023-6-1

### Optimized

- Compatible with python 3.10
- Optimize option command

### Added

- Add settings of rgb pin
- Add colorful_leap style

## [1.5.0] - 2023-4-7

### Modified

- Now the program is compatible with multiple systems based on debian, including Ubuntu, Kali, OSMC, RetroPie, OctoPi, Homebridge

### Optimized

- Add working_tip while installing

### Changed

- Change getCPUtemperature() fuction to compatible some othee systems

## [1.4.0] - 2023-3-23

### Changed

- Change rgb pwm default frequency to 1000 kHz, to compatible different LED components
- Now the oled initialization fails and the program won't terminate

### Added

- Add command to set pwm frequency

## [1.3.0] - 2023-2-24

### Changed

- Disable "dtparam=audio" in the /boot/config.txt
- Auto config "gpio-poweroff" and "gpio-ir" in the /boot/config.txt
- Cancel reinit for ws2812

### Added

- Add Kernel info, OS version, PCB info in the log

## [1.2.8] - 2023-2-21

### Changed

- Change ws2812 Adafruit_NeoPixel to PixelStrip

## [1.2.7] - 2023-2-14

### Fixed

- Fix the bug of showing ip address when docker is installed on the system

## [1.2.6] - 2023-1-29

### Fixed

- Fix the bug of install process and get system status in different system languages

## [1.2.4] - 2023-1-6

### Fixed

- Fix the bug of getting CPU useage rate when the system language is French

## [1.2.3] - 2022-12-27

### Fixed

- Fix the bug that the number of files overflowed when reinitializing the ws2812_rgb object

## [1.2.2] - 2022-12-22

### Fixed

- Fix the bug of rgb wrongly flash when running "pironman start"

## [1.2.1] - 2022-12-21

### Fixed

- Fix the bug of rgb init

## [1.2.0] - 2022-12-15

### Fixed

- Fix the problem of rgb wrongly flash caused by occupied rgb pwm pin

### Added

- Add "colorful" style of rgb LEDs

## [1.1.0] - 2022-5-12

### Changed

- Change the project name to "Pironman"

### Fixed

- Fix the data disorder of ws2812 RGB lights after startup

## [1.0.0] - 2022-3-23

### Added

- Add changelog.md
- Add Fahrenheit temperature unit
- Add get more network card ips, not just wlan0 or eth0
- Add shell command to view all configuration parameters
- Add shell command to change temperature unit

### Fixed

- Fix bug of shell command

### Optimized

- Optimize code redundancy
- Catch more error messages

## [0.0.3] - 2022-1-28

### Fixed

- Fix bug of log
- Fix bug of get system cpu usage

### Optimized

- Optimize code redundancy

## [0.0.2] - 2022-1-27

### Fixed

- Fix bug of auto_start at boot
- Fix bug of temperature controlled fan
- Fix bug of wrong username obtained

### Optimized

- Optimize code redundancy

## [0.0.1] - 2022-1-18

### Basic function

- Oled system status display
- Auto start at boot
- Shell commands interaction
- RGB strip control
- Cooling Fan Control
- ...
