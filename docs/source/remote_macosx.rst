
Mac OS X Benutzer
==========================

Für Mac-Benutzer ist der direkte Zugriff auf den Raspberry Pi Desktop über VNC bequemer als über die Befehlszeile. Mit dem Finder können Sie darauf zugreifen, nachdem Sie VNC auf der Raspberry Pi-Seite aktiviert und das festgelegte Kontopasswort eingegeben haben.

Beachten Sie, dass diese Methode die Kommunikation zwischen dem Mac und dem Raspberry Pi nicht verschlüsselt. 
Die Kommunikation erfolgt innerhalb Ihres Heim- oder Firmennetzwerks. Daher sollte es auch ungeschützt kein Problem sein.
Wenn Sie jedoch Bedenken haben, können Sie eine VNC-Anwendung wie `VNC® Viewer <https://www.realvnc.com/en/connect/download/viewer/>`_ installieren.

Alternativ könnten Sie einen temporären Monitor (TV), Maus und Tastatur verwenden, um den Raspberry Pi Desktop direkt zu öffnen und VNC einzurichten. 
Wenn nicht, ist das kein Problem. Sie können auch den SSH-Befehl verwenden, um die Bash-Shell des Raspberry Pi zu öffnen und dann den Befehl zur Einrichtung von VNC zu verwenden.

* :ref:`have_temp_monitor`
* :ref:`no_temp_monitor`

.. _have_temp_monitor:

Haben Sie einen temporären Monitor (oder TV)?
---------------------------------------------------------------------

#. Schließen Sie einen Monitor (oder TV), Maus und Tastatur an den Raspberry Pi an und schalten Sie ihn ein. Wählen Sie das Menü entsprechend den Zahlen in der Abbildung.

    .. image:: img/mac_vnc1.png
        :align: center

#. Der folgende Bildschirm wird angezeigt. Setzen Sie **VNC** auf dem **Interfaces**-Tab auf **Enabled** und klicken Sie auf **OK**.

    .. image:: img/mac_vnc2.png
        :align: center

#. Ein VNC-Symbol erscheint oben rechts auf dem Bildschirm und der VNC-Server startet.

    .. image:: img/login1.png
        :align: center

#. Öffnen Sie das VNC-Server-Fenster durch Klicken auf das **VNC**-Symbol, dann klicken Sie auf die **Menu**-Schaltfläche in der oberen rechten Ecke und wählen Sie **Options**.

    .. image:: img/mac_vnc4.png
        :align: center

#. Der folgende Bildschirm wird angezeigt, auf dem Sie die Optionen ändern können.

    .. image:: img/mac_vnc5.png
        :align: center

    Setzen Sie **Encryption** auf **Prefer off** und **Authentication** auf **VNC password**.

#. Wenn Sie auf **OK** klicken, wird der Passworteingabebildschirm angezeigt. Sie können das gleiche Passwort wie das des Raspberry Pi verwenden oder ein anderes, also geben Sie es ein und klicken Sie auf **OK**.

    .. image:: img/mac_vnc16.png
        :align: center

    Sie sind jetzt bereit, sich von Ihrem Mac aus zu verbinden. Es ist in Ordnung, den Monitor zu trennen.

**Von hier aus handelt es sich um den Betrieb auf der Mac-Seite.**

#. Wählen Sie **Connect to Server** aus dem Finder-Menü, das Sie durch Rechtsklicken öffnen können.

    .. image:: img/mac_vnc10.png
        :align: center

#. Geben Sie ``vnc://<benutzername>@<hostname>.local`` (oder ``vnc://<benutzername>@<IP-Adresse>``) ein. Nach der Eingabe klicken Sie auf **Connect**.

    .. image:: img/mac_vnc11.png
        :align: center

#. Ihnen wird nach einem Passwort gefragt, bitte geben Sie dieses ein.

    .. image:: img/mac_vnc12.png
        :align: center

#. Der Desktop des Raspberry Pi wird angezeigt und Sie können ihn so bedienen, als wären Sie direkt darauf.

    .. image:: img/mac_vnc13.png
        :align: center

.. _no_temp_monitor:

Haben Sie keinen temporären Monitor (oder TV)?
---------------------------------------------------------------------------

* Sie können den SSH-Befehl verwenden, um die Bash-Shell des Raspberry Pi zu öffnen.
* Bash ist die Standard-Shell für Linux.
* Die Shell selbst ist ein Befehl (Anweisung), wenn der Benutzer Unix/Linux verwendet.
* Das Meiste von dem, was Sie tun müssen, kann über die Shell erledigt werden.
* Nach der Einrichtung auf der Raspberry Pi-Seite können Sie mit dem **Finder** vom Mac aus auf den Desktop des Raspberry Pi zugreifen.

#. Geben Sie ``ssh <benutzername>@<hostname>.local`` ein, um eine Verbindung zum Raspberry Pi herzustellen.

    .. code-block:: shell

        ssh pi@raspberrypi.local

    .. image:: img/mac_vnc14.png

#. Die folgende Nachricht wird nur angezeigt, wenn Sie sich zum ersten Mal anmelden, also geben Sie **yes** ein.

    .. code-block::

        The authenticity of host 'raspberrypi.local (2400:2410:2101:5800:635b:f0b6:2662:8cba)' can't be established.
        ED25519 key fingerprint is SHA256:oo7x3ZSgAo032wD1tE8eW0fFM/kmewIvRwkBys6XRwg.
        This key is not known by any other names
        Are you sure you want to continue connecting (yes/no/[fingerprint])?

#. Geben Sie das Passwort für den Raspberry Pi ein. Das von Ihnen eingegebene Passwort wird nicht angezeigt, achten Sie also darauf, keinen Fehler zu machen.

    .. code-block::

        pi@raspberrypi.local's password: 
        Linux raspberrypi 5.15.61-v8+ #1579 SMP PREEMPT Fri Aug 26 11:16:44 BST 2022 aarch64

        The programs included with the Debian GNU/Linux system are free software;
        the exact distribution terms for each program are described in the
        individual files in /usr/share/doc/*/copyright.

        Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
        permitted by applicable law.
        Last login: Thu Sep 22 12:18:22 2022
        pi@raspberrypi:~ $
 


    

#. Richten Sie Ihren Raspberry Pi so ein, dass Sie sich über VNC von Ihrem Mac aus anmelden können, sobald Sie erfolgreich darauf zugegriffen haben. Der erste Schritt besteht darin, Ihr Betriebssystem zu aktualisieren, indem Sie die folgenden Befehle ausführen.

    .. code-block:: shell

        sudo apt update
        sudo apt upgrade

    ``Möchten Sie fortfahren? [Y/n]``, geben Sie bei Aufforderung ``Y`` ein.

    Es kann eine Weile dauern, bis das Update abgeschlossen ist. (Dies hängt von der Anzahl der zu diesem Zeitpunkt anstehenden Aktualisierungen ab.)

#. Geben Sie den folgenden Befehl ein, um den **VNC Server** zu aktivieren.

    .. code-block:: shell

        sudo raspi-config

#. Das folgende Menü wird angezeigt. Wählen Sie mit den Pfeiltasten der Tastatur **3 Interface options** und drücken Sie die **Enter**-Taste.

    .. image:: img/image282.png
        :align: center

#. Wählen Sie anschließend **P3 VNC**.

    .. image:: img/image288.png
        :align: center

#. Verwenden Sie die Pfeiltasten auf der Tastatur, um **<Yes>** -> **<OK>** -> **<Finish>** auszuwählen und die Einrichtung abzuschließen.

    .. image:: img/mac_vnc8.png
        :align: center

#. Nun, da der VNC-Server gestartet ist, ändern wir die Einstellungen für die Verbindung von einem Mac aus.

    Um Parameter für alle Programme für alle Benutzerkonten auf dem Computer festzulegen, erstellen Sie ``/etc/vnc/config.d/common.custom``.

    .. code-block:: shell

        sudo nano /etc/vnc/config.d/common.custom

    Nachdem Sie ``Authentication=VncAuthenter`` eingegeben haben, drücken Sie ``Ctrl+X`` -> ``Y`` -> ``Enter``, um zu speichern und zu beenden.

    .. image:: img/mac_vnc15.png
        :align: center

#. Legen Sie außerdem ein Passwort fest, um sich über VNC von einem Mac aus anzumelden. Sie können dasselbe Passwort wie das des Raspberry Pi verwenden oder ein anderes.

    .. code-block:: shell

        sudo vncpasswd -service

#. Sobald die Einrichtung abgeschlossen ist, starten Sie den Raspberry Pi neu, um die Änderungen zu übernehmen.

    .. code-block:: shell

        sudo reboot

#. Wählen Sie nun **Connect to Server** aus dem **Finder**-Menü, das Sie durch Rechtsklicken öffnen können.

    .. image:: img/mac_vnc10.png
        :align: center
   
#. Geben Sie ``vnc://<benutzername>@<hostname>.local`` (oder ``vnc://<benutzername>@<IP-Adresse>``) ein. Nach der Eingabe klicken Sie auf **Connect**.

        .. image:: img/mac_vnc11.png
            :align: center

#. Sie werden nach einem Passwort gefragt, bitte geben Sie dieses ein.

        .. image:: img/mac_vnc12.png
            :align: center

#. Der Desktop des Raspberry Pi wird angezeigt und Sie können ihn von Ihrem Mac aus steuern.

        .. image:: img/mac_vnc13.png
            :align: center

