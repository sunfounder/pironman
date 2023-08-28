Windows-Benutzer
=======================

Wenn Sie ein Windows-Benutzer sind, können Sie Windows PowerShell verwenden, um sich remote beim Raspberry Pi anzumelden.

#. Drücken Sie die Tastenkombination ``windows`` + ``R`` auf Ihrer Tastatur, um das Programm **Run** zu öffnen. Geben Sie dann **powershell** in das Eingabefeld ein.

    .. image:: img/sp221221_135900.png
        :align: center

#. Überprüfen Sie, ob Ihr Raspberry Pi im selben Netzwerk ist, indem Sie ``ping <hostname>.local`` eingeben.

    .. code-block:: shell

        ping raspberrypi.local

    .. image:: img/sp221221_145225.png
        :width: 550
        :align: center

    * Wenn das Terminal ``Ping request could not find host <hostname>.local`` anzeigt, ist es möglich, dass der Raspberry Pi keine Verbindung zum Netzwerk herstellen konnte. Bitte überprüfen Sie das Netzwerk.
    * Wenn Sie wirklich nicht ``<hostname>.local`` pingen können, versuchen Sie, :ref:`get_ip` zu verwenden und stattdessen ``ping <IP-Adresse>`` einzugeben (z.B. ``ping 192.168.6.116``).
    * Wenn mehrere Meldungen wie "Reply from <IP-Adresse>: bytes=32 time<1ms TTL=64" angezeigt werden, bedeutet dies, dass Ihr Computer auf den Raspberry Pi zugreifen kann.

#. Geben Sie ``ssh <benutzername>@<hostname>.local`` (oder ``ssh <benutzername>@<IP-Adresse>``) ein.

    .. code-block:: shell

        ssh pi@raspberrypi.local

#. Die folgende Meldung könnte erscheinen:

    .. code-block::

        The authenticity of host 'raspberrypi.local (192.168.6.116)' can't be established.
        ECDSA key fingerprint is SHA256:7ggckKZ2EEgS76a557cddfxFNDOBBuzcJsgaqA/igz4.
        Are you sure you want to continue connecting (yes/no/[fingerprint])? 

    Geben Sie \"yes\" ein.

#. Geben Sie das zuvor festgelegte Passwort ein. (Meins ist ``raspberry``.)

    .. note::
        Beim Eingeben des Passworts werden die Zeichen nicht im
        Fenster angezeigt, was normal ist. Wichtig ist nur, dass
        Sie das korrekte Passwort eingeben.

#. Nun ist der Raspberry Pi verbunden und wir können zum nächsten Schritt übergehen.

    .. image:: img/sp221221_140628.png
        :width: 550
        :align: center

Remote-Desktop
------------------

Wenn Sie mit dem Befehlsfenster für den Zugriff auf Ihren Raspberry Pi nicht zufrieden sind, können Sie auch die Remote-Desktop-Funktion verwenden, um Dateien auf Ihrem Raspberry Pi mit einer GUI einfach zu verwalten.

Hier verwenden wir den `VNC® Viewer <https://www.realvnc.com/en/connect/download/viewer/>`_.

**VNC-Dienst aktivieren**

Der VNC-Dienst ist im System installiert. Standardmäßig ist VNC deaktiviert. Sie müssen ihn in der Konfiguration aktivieren.

#. Geben Sie den folgenden Befehl ein:

    .. raw:: html

        <run></run>

    .. code-block:: shell 

        sudo raspi-config

#. Wählen Sie mit den Pfeiltasten Ihrer Tastatur **3 Interfacing Options** und drücken Sie die **Enter**-Taste.

    .. image:: img/image282.png
        :align: center

#. Wählen Sie anschließend **P3 VNC**.

    .. image:: img/image288.png
        :align: center

#. Nutzen Sie die Pfeiltasten auf der Tastatur, um **<Yes>** -> **<OK>** -> **<Finish>** auszuwählen und die Einrichtung abzuschließen.

    .. image:: img/mac_vnc8.png
        :align: center

**Anmeldung bei VNC**

#. Sie müssen den `VNC Viewer <https://www.realvnc.com/en/connect/download/viewer/>`_ auf Ihrem Computer herunterladen und installieren.

#. Öffnen Sie ihn, sobald die Installation abgeschlossen ist. Geben Sie dann den Hostnamen oder die IP-Adresse ein und drücken Sie Enter.

    .. image:: img/vnc_viewer1.png
        :align: center

#. Nach Eingabe Ihres Raspberry Pi-Namens und Passworts klicken Sie auf **OK**.

    .. image:: img/vnc_viewer2.png
        :align: center

#. Nun können Sie den Desktop des Raspberry Pi sehen.

    .. image:: img/login1.png
        :align: center

