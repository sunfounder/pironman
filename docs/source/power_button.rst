Ein/Aus-Taste
==================================

.. note::
    Die Ein/Aus-Taste ist an GPIO26 angeschlossen. Wenn Sie sie an einen anderen Pin anschließen möchten, beziehen Sie sich bitte auf :ref:`change_config`.

Die Ein/Aus-Taste kann verwendet werden, um den OLED-Bildschirm zu wecken oder den Pironman auszuschalten.

* Nach dem Einschalten wird der OLED-Bildschirm für 60 Sekunden angezeigt, bevor er in den Schlafmodus wechselt. Mit der Ein/Aus-Taste können Sie den OLED-Bildschirm später wieder aufwecken.

* Es gibt 2 Möglichkeiten, den Pironman herunterzufahren.

    #. Erzwungener Shutdown

        Wenn Sie die Ein/Aus-Taste 10 Sekunden lang gedrückt halten, wird die Stromversorgung des Pironman unterbrochen. Diese Methode kann jedoch Dateien des Raspberry Pi beschädigen oder einige Änderungen nicht speichern.

    #. Sicherer Shutdown

        Es gibt auch eine Möglichkeit, den Pironman sicher auszuschalten, indem Sie die Ein/Aus-Taste nach der Konfiguration 2 Sekunden lang gedrückt halten.

