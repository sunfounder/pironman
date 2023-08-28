Kühlventilator
=====================

.. note::
    Der Kühlventilator ist an GPIO6 (BCM) angeschlossen.

Der Betriebsstatus des Kühlventilators wird durch die CPU-Temperatur bestimmt. Wenn die CPU-Temperatur den eingestellten Schwellenwert erreicht, beginnt der Ventilator zu laufen. Liegt sie 2 Grad Celsius unter dem Schwellenwert, wird der Ventilator gestoppt.

* Temperatureinheit festlegen, ``C``: Celsius, ``F``: Fahrenheit.

.. code-block:: shell

    pironman  -u C


* Die Temperatur festlegen, bei der der Ventilator startet, z.B. 40 Grad Celsius (die Einheit wird von Ihnen bestimmt).

.. code-block:: shell

    pironman  -f 40