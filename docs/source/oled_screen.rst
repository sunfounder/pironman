OLED Screen
===================

After installation, the script will start automatically and the OLED screen will display the CPU, RAM and ROM Usage, CPU Temperature and IP Address of the Raspberry Pi.


In order to extend the life of OLED screen, OLED will turn off after 60 seconds by default, and will light up by pressing the power button shortly. You can enable/disable this feature with the following command.

* set to sleep mode:  "al" means to "always on".

.. raw:: html

    <run></run>

.. code-block::

    pironman  -al off

* set to always on mode:

.. raw:: html

    <run></run>

.. code-block::

    pironman  -al on

* Set the duration in seconds.

.. raw:: html

    <run></run>

.. code-block::

    pironman  -s 60

* The above are what we set for OLED screen, if you want to make OLED screen display other information and effects, you can open ``/opt/pironman/main.py`` to modify and run it.

    Open this python script and modify its contents.

    .. raw:: html

        <run></run>

    .. code-block::

        sudo nano /opt/pironman/main.py


    Press ``Ctrl+X`` -> ``Y`` -> ``Enter`` to save and exit editing.

    Run it.

    .. raw:: html

        <run></run>

    .. code-block::

        sudo python3 /opt/pironman/main.py