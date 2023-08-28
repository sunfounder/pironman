FAQ
============

Pironmans LED leuchtet, aber der Raspberry Pi bootet nicht, wenn der Anschaltknopf gedrückt wird?
---------------------------------------------------------------------------------------------------

Bitte überprüfen Sie die folgenden Bedingungen.

#. Verfügt der Raspberry Pi über eine separate Stromversorgung?

    Dies sollten Sie vermeiden, aus folgenden Gründen:

    Da der Raspberry Pi selbst keine Ein/Aus-Steuerung besitzt, kann er nur durch das Einschalten der Stromversorgung aktiviert werden. 
    Pironman schaltet den Raspberry Pi also nach dem Ausschalten ab und startet ihn durch Einschalten der Stromversorgung wieder.
    Wenn sowohl der Raspberry Pi als auch der Pironman eingeschaltet sind, kann Pironman nach dem Herunterfahren den Raspberry Pi nicht durch Einschalten der Stromversorgung starten, da der Raspberry Pi extern angeschlossen und ständig eingeschaltet ist.

#. Ist die Micro-SD-Karte bereits im Pironman-Slot eingelegt?
#. Sind auf der Micro-SD-Karte bereits Systeme installiert?
#. Ist besonders darauf zu achten, dass das FFC-Kabel der GPIO-Brücke korrekt angeschlossen ist?

    .. image:: img/gpio_bridge1.gif
    .. image:: img/gpio_bridge2.gif

.. _copy_lite:

Wie kopiert man Raspberry Pi OS Lite von der Micro-SD-Karte auf die SSD?
----------------------------------------------------------------------------

#. Aktualisierung des Bootloaders

    .. code-block:: shell

        sudo apt update
        sudo apt full-upgrade
        sudo rpi-update
        sudo rpi-eeprom-update -d -a

    Nach der Einstellung ist ein Neustart erforderlich.

#. Verwenden Sie den folgenden Befehl, um den Namen des Speichergeräts anzuzeigen.

    .. code-block:: shell

        sudo fdisk -l

#. Sie werden eine Liste aller Laufwerke sehen, die an Ihren Raspberry Pi angeschlossen sind. In den meisten Fällen bezieht sich ``/dev/mmcxxx`` auf Ihre Micro-SD-Karte und ``/dev/sda/`` auf Ihre SSD.

    .. image:: img/ssd16.png

#. Nutzen Sie nun den folgenden Befehl, um das System von der Micro-SD-Karte auf die SATA M.2 SSD zu klonen.

    .. note::
        Ersetzen Sie ``/dev/mmcblk0`` durch den Namen Ihrer Micro-SD-Karte und ändern Sie auch ``/dev/sda``, wenn Ihre SSD einen anderen Namen hat.

    .. code-block:: shell

        sudo dd if=/dev/mmcblk0 of=/dev/sda bs=4M

#. Entfernen Sie die Micro-SD-Karte, schließen Sie die M.2 SATA SSD an und schalten Sie dann den Pironman ein.
