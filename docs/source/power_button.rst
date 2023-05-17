Power Button
==================================

.. note::
    The power button is connected to GPIO26, if you want to change it to another pin, please refer to :ref:`change_config`.

The power button can be used to wake up the OLED screen or to turn the Pironman off.

* Upon power-up, the OLED screen displays for 60 seconds before going into sleep mode. Using the power button, you can wake up the OLED screen again later.

* You have 2 ways to get the Pironman to shut down.

    #. Force Shutdown

        Pressing and holding the power button for 10 seconds will let the Pironman power cut, but this method may damage the Raspberry Pi's files or leave some changes unsaved.

    #. Safe Shutdown

        There is also a way to safely turn off the Pironman by pressing and holding the power button for 2 seconds after configuring it.
