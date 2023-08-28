IR-Empfänger
================

.. note::
    Der IR-Empfänger ist an GPIO13 angeschlossen. Wenn Sie ihn an einen anderen Pin anschließen möchten, beziehen Sie sich bitte auf :ref:`change_config`.

Bevor Sie den IR-Empfänger verwenden können, müssen Sie seine Verbindung testen und das relevante Modul installieren.

#. Verwenden Sie den folgenden Befehl zum Testen. Wenn ein Anzeigegerät vorhanden ist, war die Konfiguration erfolgreich.

    .. code-block:: shell

        sudo ls /dev |grep lirc

#. Installieren Sie das ``lirc`` Modul.

    .. code-block:: shell

        sudo apt-get install lirc -y

#. Führen Sie den folgenden Befehl aus, und wenn Sie eine Taste auf der Fernbedienung drücken, wird der Code der entsprechenden Taste angezeigt.

    .. code-block:: shell

        mode2 -d /dev/lirc0

.. note::
    Wenn Sie Kodi auf dem Raspberry Pi verwenden möchten, beziehen Sie sich bitte auf: :ref:`kodi_osmc`.
