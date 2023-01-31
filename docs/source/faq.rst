FAQ
============

Pironman's LED lights up but Raspberry Pi won't boot when power button is pressed?
-------------------------------------------------------------------------------------------

Please check the following conditions.

#. Is there a separate power supply for the Raspberry Pi?

    Please do not do this, for the following reasons.

    Since the Raspberry Pi itself has no on/off control, it can only be powered on by powering up the Raspberry Pi. 
    So Pironman will power off the Raspberry Pi after it is turned off, and power on the Raspberry Pi to start the Raspberry Pi. 
    If you power on both the Raspberry Pi and Pironman, after shutdown, the Pironman has no way to start the Raspberry Pi by powering on the Raspberry Pi because the Raspberry Pi is externally plugged in and always powered on.

#. Is the Micro SD card already inserted into the Pironman slot?
#. Are there any systems installed on Micro SD card?
#. The most important point to note is that the FFC cable of the GPIO Bridge is connected correctly?

    .. image:: img/gpio_bridge1.gif
    .. image:: img/gpio_bridge2.gif