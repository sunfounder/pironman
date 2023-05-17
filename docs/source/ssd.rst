.. _ssd:

M.2 SATA SSD
=====================================

.. note::
    The M.2 SSD hard drive interface only supports SATA protocol, not NVME/PCIe.

**About the Model**

M.2 SSD (M.2 solid-state drive) comes in various models, depending on their specifications and performance characteristics. Here are some common M.2 SSD models:

* **SATA M.2 SSD**: This is the most common type of M.2 SSD, using the SATA interface. They typically offer lower read/write speeds and lower prices, suitable for general computing tasks.
* **NVMe M.2 SSD**: This is a higher-performance type of M.2 SSD, utilizing the NVMe (Non-Volatile Memory Express) interface. NVMe SSDs provide faster transfer speeds and lower latency, suitable for tasks that require high-speed data transfer, such as gaming and large file processing.
* **PCIe M.2 SSD**: This type of M.2 SSD uses the PCI Express (PCIe) interface, offering higher bandwidth and faster speeds. They are typically more expensive than SATA and NVMe SSDs and are suitable for professional users who require the highest performance, such as video editing and scientific computing.

M.2 SSDs come in three key types: B key, M key, and B+M key. However, later on, the B+M key was introduced, combining the functionalities of the B key and M key. As a result, it replaced the standalone B key. Please refer to the image below.

.. image:: img/ssd_key.png


In general, M.2 SATA SSDs are B+M-keyed (can fit in sockets for B-keyed and M-keyed modules), while M.2 NVMe SSDs for PCIe 3.0 x4 lane are M-keyed.

.. image:: img/ssd_model2.png

**About the Length**

M.2 modules come in different sizes and can also be utilized for Wi-Fi, WWAN, Bluetooth, GPS, and NFC.

M.2 SSDs typically come in four dimensions, which may be deduced from the card name —2230, 2242, 2260, and 2280 — "22" represents the width in millimeters (mm), while the next two digits represent the length, also in mm. The longer the drive, the more NAND flash chips can be mounted; hence, more capacity.


.. image:: img/m2_ssd_size.png
    :width: 600


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


    .. code-block:: shell

        sudo apt update
        sudo apt full-upgrade
        sudo rpi-update
        sudo rpi-eeprom-update -d -a

    After setting, reboot to take effect.


#. Use the following command to view the name of the storage device.


    .. code-block:: shell

        sudo fdisk -l

    .. image:: img/ssd16.png

#. Now, clone the system from the Micro SD card to the M.2 SATA SSD. Where ``if`` is followed by the sd card name and ``of`` is followed by the M.2 SSD name.


    .. code-block:: shell

        sudo dd if=/dev/mmcblk0 of=/dev/sda bs=4M

#. Pull out the Micro SD card, connect the M.2 SATA SSD and then power on the Pironman.