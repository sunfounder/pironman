WS2812 RGB Strip
=======================

.. note::
    The IR receiver is connected to GPIO12.

The WS1812 RGB Strip is a light strip with 8 RGB LEDs that can be used to display Pironman's status. You can use commands to make it turn on or off, or to modify its color (default is blue), display mode and change rate.

* Turn on the WS2812 RGB Strip.

.. raw:: html

    <run></run>

.. code-block::

    pironman  -rw on

* Turn it off.

.. raw:: html

    <run></run>

.. code-block::

    pironman  -rw off

* Change its color, using hexadecimal color values.

.. raw:: html

    <run></run>

.. code-block::

    pironman  -rc fe1a1a

* Changing the display mode, there are four modes to choose from: ``breath``, ``leap``, ``flow``, ``raise_up``.

.. raw:: html

    <run></run>

.. code-block::

    pironman  -rs leap

* Change the speed of change (0 ~ 100%).

.. raw:: html

    <run></run>

.. code-block::

    pironman  -rb 80

* Above are the effects we preset for WS2812 RGB Strip, if you want it to display other effects, you can open ``/opt/pironman/ws2812_RGB.py`` to modify and run it.

    Open this python script and modify its contents.

    .. raw:: html

        <run></run>

    .. code-block::

        sudo nano /opt/pironman/ws2812_RGB.py

    Press ``Ctrl+X`` -> ``Y`` -> ``Enter`` to save and exit editing.

    Run it.

    .. raw:: html

        <run></run>

    .. code-block::

        sudo python3 /opt/pironman/ws2812_RGB.py