IR Receiver
================

.. note::
    The IR receiver is connected to GPIO13, if you want to change it to another pin, please refer to :ref:`change_config`.

Before you can use IR receiver, you need to test its connection and install the relevant module.

#. Use the following command to test, if there is a display device then the configuration is successful.

    .. code-block::

        sudo ls /dev |grep lirc

#. Install the ``lirc`` module.

    .. code-block::

        sudo apt-get install lirc -y

#. Run the following command, and if you press a key on the remote controller, the code of the corresponding key will be printed.

    .. code-block::

        mode2 -d /dev/lirc0

.. note::
    If you want to play Kodi on Raspberry Pi, please refer to: :ref:`kodi_osmc`.