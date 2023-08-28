.. _set_up_homeass:


Einrichtung Ihres Home Assistant
==================================

**Schritt 1**

In diesem Schritt aktivieren wir die I2C-Schnittstelle, um das Pironman OLED-Display in Betrieb zu nehmen.

Öffnen Sie den Datei-Explorer und navigieren Sie zur SD-Karte, die als  ``Hassio-boot`` bezeichnet ist.

.. image:: img/sp230628_095957.png

Erstellen Sie im Stammverzeichnis der SD-Karte einen neuen Ordner namens  ``CONFIG`` .

.. image:: img/sp230628_100453.png

Im Ordner ``CONFIG`` legen Sie nun einen Unterordner namens ``modules`` an.

.. image:: img/sp230628_101108.png

Aktivieren Sie die Anzeige der Dateiendungen.

.. image:: img/sp230628_101216.png

Erstellen Sie im ``modules`` -Ordner eine Textdatei und benennen Sie diese in ``rpi-i2c.conf`` um. Bestätigen Sie die Änderung der Dateiendung mit "Yes".

.. image:: img/sp230628_101545.png

Öffnen Sie ``rpi-i2c.conf`` mit dem Texteditor und fügen Sie den folgenden Inhalt ein:

.. code-block::

    i2c-dev

Speichern und schließen Sie die Datei.

**Schritt 2**

In diesem Schritt konfigurieren wir die RGB-LED.

#. Öffnen Sie die Datei ``config.txt`` im Verzeichnis ``Hassio-boot``.

    .. image:: img/sp230628_102441.png

#. Fügen Sie die folgenden Zeilen am Ende der Datei ein:

    .. code-block::

        dtparam=i2c_vc=on
        dtparam=i2c_arm=on
        dtoverlay=gpio-poweroff,gpio_pin=26,active_low=0
        dtoverlay=gpio-ir,gpio_pin=13

#. Identifizieren Sie den Pin, den Sie für den WS2812 LED-Streifen verwenden.

    .. image:: img/strip_select.png

    * Wenn Sie den Standard-SPI-Pin (GPIO10) verwenden, müssen Sie die folgenden Befehle zur ``config.txt`` hinzufügen, um SPI zu aktivieren und die Frequenz auf 500bps einzustellen.

        .. code-block::

            dtparam=spi=on
            core_freq=500
            core_freq_min=500
            # Aktivieren Sie den Ton, falls erforderlich.
            dtparam=audio=on
    
    * Wenn Sie PWM (GPIO12) nutzen, das ebenfalls für die Audioausgabe verwendet wird, deaktivieren Sie den Ton. Fügen Sie den folgenden Befehl in die ``config.txt`` ein:

        .. code-block::

            dtparam=audio=off

    * Für die Nutzung von PCM (GPIO21) ist keine weitere Konfiguration erforderlich. Achten Sie jedoch darauf, dass es zu Konflikten mit I2S-Geräten wie ``hifiberry-dac`` oder ``i2s-mmap`` kommen kann. Deaktivieren Sie diese und schalten Sie den Ton bei Bedarf ein.

        .. code-block::

            # Aktivieren Sie den Ton, falls erforderlich.
            dtparam=audio=on
            # Kommentieren Sie das I2S-Gerät aus.
            # dtoverlay=hifiberry-dac
            # dtoverlay=i2s-mmap

#. Speichern und schließen Sie die Datei.

**Schritt 3**

Im nächsten Schritt konfigurieren wir das WLAN für Pironman.

.. note:: Falls Sie eine kabelgebundene Verbindung bevorzugen, können Sie diesen Schritt überspringen.

Legen Sie im ``CONFIG`` Ordner einen neuen Unterordner namens ``network`` an.

.. image:: img/sp230628_113426.png

Im ``network`` -Ordner erstellen Sie eine Textdatei namens ``my-network`` (ohne Dateiendung).

.. image:: img/sp230628_113506.png

Tragen Sie die folgenden Informationen in die Datei ``my-network`` ein, wobei Sie ``MY_SSID`` und ``MY_WLAN_SECRET_KEY`` durch Ihre eigenen Netzwerkinformationen ersetzen:

.. code-block::

    [connection]
    id=my-network
    uuid=72111c67-4a5d-4d5c-925e-f8ee26efb3c3
    type=802-11-wireless

    [802-11-wireless]
    mode=infrastructure
    ssid=MY_SSID
    # Entfernen Sie den Kommentar, falls Ihr SSID nicht ausgestrahlt wird.
    #hidden=true

    [802-11-wireless-security]
    auth-alg=open
    key-mgmt=wpa-psk
    psk=MY_WLAN_SECRET_KEY

    [ipv4]
    method=auto

    [ipv6]
    addr-gen-mode=stable-privacy
    method=auto

Speichern und schließen Sie die Datei.

**Schritt 4**

Entnehmen Sie die microSD-Karte aus dem Computer und stecken Sie sie in den Raspberry Pi. Verbinden Sie dann die Stromversorgung (und bei Bedarf das Ethernet-Kabel).

Öffnen Sie einen Browser und navigieren Sie zu ``homeassistant.local:8123`` , oder ermitteln Sie die IP-Adresse über Ihren Router, falls die lokale Adresse nicht funktioniert.

Beim ersten Start von Home Assistant kann die Initialisierung einige Zeit in Anspruch nehmen.

.. image:: img/sp230628_141749.png

**Schritt 5**

Als Nächstes werden Sie aufgefordert, das erste Benutzerkonto anzulegen.

.. image:: img/sp230627_135949.png

Das System schlägt die Installation einiger erkannter Geräte vor, die Sie jedoch vorerst durch Klicken auf „FERTIG“ überspringen können.

.. image:: img/sp230627_141016.png



**Schritt 6**

Jetzt installieren wir das Pironman-Addon für Home Assistant.

Klicken Sie auf den folgenden Button, um das Addon schnell hinzuzufügen. Anschließend fahren Sie mit **Schritt 7** fort.

.. raw:: html

    <a href="https://my.home-assistant.io/redirect/supervisor_addon/?addon=6fa7f6d2_pironman&repository_url=https%3A%2F%2Fgithub.com%2Fsunfounder%2Fhome-assistant-addon" target="_blank"><img src="https://my.home-assistant.io/badges/supervisor_addon.svg" alt="Öffnen Sie Ihre Home Assistant-Instanz und zeigen Sie das Dashboard eines Supervisor-Addons an." /></a>

Alternativ führen Sie die unten aufgeführten Schritte für eine manuelle Installation durch:

1. Navigieren Sie in Home Assistant zu Settings -> Addons.

    .. image:: img/sp230628_150312.png

2. Klicken Sie unten rechts auf den Button "Addon Shop".

    .. image:: img/sp230628_150338.png

3. Klicken Sie oben rechts auf das Menü und wählen Sie "Repositories".

    .. image:: img/sp230627_145728.png

4. Geben Sie die Repository-URL ein: ``https://github.com/sunfounder/home-assistant-addon`` und klicken Sie auf Hinzufügen. Schließen Sie nach dem Hinzufügen des SunFounder-Repository das Popup-Fenster.

    .. image:: img/sp230627_150423.png

5. Klicken Sie erneut auf das Menü und wählen Sie "Check for updates".

    .. image:: img/sp230627_150716.png

6. Nach wenigen Sekunden erscheint das Pironman-Addon am Ende des Addon-Shops. Falls nicht, aktualisieren Sie die Seite.

    .. image:: img/sp230627_150717.png


**Schritt 7**

Öffnen Sie das Pironman-Addon und klicken Sie auf Installieren. Dieser Vorgang kann einige Minuten dauern.

.. image:: img/sp230627_150840.png

Aktuell müssen Sie den Schutzmodus deaktivieren, um dem Addon den Zugriff auf Hardware-Informationen zu ermöglichen. Finden Sie "Schutzmodus" und schalten Sie ihn aus. Starten (oder starten Sie neu) Sie dann das Addon.

.. image:: img/sp230627_153858.png

An diesem Punkt sollten die Lichteffekte von Pironman und das OLED-Display aktiv sein. Dies signalisiert, dass die Konfiguration abgeschlossen ist.

Fehlerbehebung
-------------------------

Sollte Ihr OLED- oder RGB-Streifen nicht ordnungsgemäß starten, navigieren Sie zur "Log"-Seite.

.. image:: img/sp230628_162143.png

.. code-block::

    [DEBUG] OLED-Initialisierung fehlgeschlagen:
    [Errno 2] Datei oder Verzeichnis nicht gefunden
    Kann /dev/spidev0.0 nicht öffnen. Modul spi_bcm2835 nicht geladen?

.. code-block::

    [DEBUG] Initialisierung des RGB-Streifens fehlgeschlagen:
    ws2811_init mit Code -13 gescheitert (SPI-Initialisierung nicht möglich)

Wenn Sie die obigen Logs sehen, war die Konfiguration nicht erfolgreich. Führen Sie die folgenden Schritte durch:

1. Fahren Sie Home Assistant zuerst herunter.

    .. warning::

        Ein erzwungenes Ausschalten könnte HassOS beschädigen. Folgen Sie den unten stehenden Herunterfahr-Anweisungen:

        .. image:: img/sp230628_162821.png

        .. image:: img/sp230628_162906.png

        Warten Sie dann eine Minute, bevor Sie die Stromversorgung trennen.


2. Wiederholen Sie **Schritt 1** und **Schritt 2** dieses Abschnitts (:ref:`set_up_homeass`).

3. Stecken Sie die SD-Karte wieder in Pironman, schließen Sie die Stromversorgung an und warten Sie ein bis zwei Minuten. Dann navigieren Sie in Ihrem Browser zu ``http://homeassistant.local:8123/``. Klicken Sie im Pironman-Addon auf STARTEN.

    .. raw:: html

        <a href="https://my.home-assistant.io/redirect/supervisor_addon/?addon=6fa7f6d2_pironman&repository_url=https%3A%2F%2Fgithub.com%2Fsunfounder%2Fhome-assistant-addon" target="_blank"><img src="https://my.home-assistant.io/badges/supervisor_addon.svg" alt="Öffnen Sie Ihre Home Assistant-Instanz und zeigen Sie das Dashboard eines Supervisor-Addons an." /></a>

4. Nach einer kurzen Wartezeit sollten sowohl der Pironman (RGB-Streifen & OLED) aktiv werden.

Addon-Konfiguration
-----------------------------

Sie können die Effekte von Pironman auf der Konfigurationsseite anpassen.

.. image:: img/sp230628_164931.png

Hier können Sie ändern:

* Die Temperaturanzeige-Einheit auf dem OLED.
* Die Leuchtdauer des OLED-Displays.
* Die Temperatur, bei der der Lüfter in Betrieb geht.
* Die Farbe und den Blinkmodus des RGB-Streifens.

Nachdem Sie die gewünschten Änderungen vorgenommen haben, klicken Sie auf "SAVE", um die Einstellungen zu übernehmen.
