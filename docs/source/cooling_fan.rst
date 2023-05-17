Cooling Fan
=====================

.. note::
    The Cooling Fan  is connected to GPIO6 (BCM).

The working status of the Cooling Fan is decided by the CPU temperature. When the CPU temperature reaches the set threshold, the fan spins, and if it is 2 degrees Celsius below the threshold, the fan is stopped.

* Set the temperature unit, ``C``: Celsius, ``F``: Fahrenheit.

.. code-block:: shell

    pironman  -u C


* Set the temperature at which the fan starts, for example, 40 degrees Celsius (the unit is set by you).

.. code-block:: shell

    pironman  -f 40