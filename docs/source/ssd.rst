M.2 SATA SSD
=====================================

.. note::
    The M.2 SSD hard drive interface only supports SATA protocol, not NVME/PCIe.

In the Pironman's mainboard, there is an M.2 SSD connector for installing your M.2 SATA SSD.

Various lengths of M.2 SATA SSD can be mounted: 22mm x 30mm, 42mm, 60mm, and 80mm, supporting SSD TRIM function.

**Assemble the SSD**

#. Take off the base plate of the Pironman.

    .. image:: img/ssd1.jpg
        :width: 600

#.  Remove the screw for the M.2 SATA SSD.

    .. image:: img/ssd2.jpg


#. Insert your M.2 SATA SSD.

    .. image:: img/ssd3.jpg

#. Screwed in place.

    .. image:: img/ssd4.jpg

#. Put the base plate back on.

    .. image:: img/ssd5.jpg

#. Plug in SSD Bridge and 5V/3V power supply.

    .. image:: img/ssd18.jpg
        

**Booting from SSD**


#. Updating the Bootloader

    .. raw:: html

        <run></run>

    .. code-block::

        sudo apt update
        sudo apt full-upgrade
        sudo rpi-update
        sudo rpi-eeprom-update -d -a

    After setting, reboot to take effect.


#. Use the following command to view the name of the storage device.

    .. raw:: html

        <run></run>

    .. code-block::

        sudo fdisk -l

    .. image:: img/ssd16.png

#. Now, clone the system from the Micro SD card to the M.2 SATA SSD. Where ``if`` is followed by the sd card name and ``of`` is followed by the M.2 SSD name.

    .. raw:: html

        <run></run>

    .. code-block::

        sudo dd if=/dev/mmcblk0 of=/dev/sda bs=4M

#. Pull out the Micro SD card, connect the M.2 SATA SSD and then power on the Pironman.