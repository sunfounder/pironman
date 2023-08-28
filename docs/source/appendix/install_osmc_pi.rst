.. _kodi_osmc:

Kodi auf dem Raspberry Pi mit OSMC installieren
===============================================

|link_kodi| gehört zu den beliebtesten Möglichkeiten, Medien auf Ihrem Raspberry Pi abzuspielen. Es unterstützt eine Vielzahl unterschiedlicher Medienformate. Mit dieser Media-Center-Software können Sie Musik hören, Videos ansehen und sogar Ihre Bilder darstellen.

Mit Kodi können Sie Ihre Medien scannen und ordnen. Die Software lädt Informationen zu Ihren Dateien herunter und präsentiert diese ansprechend.

Sie haben die Möglichkeit, Kodi direkt auf Ihrem Raspberry Pi zu installieren oder eine Distribution mit vorinstalliertem Kodi, wie |link_osmc| oder |link_libreelec|, zu verwenden.

In diesem Tutorial zeigen wir Ihnen, wie Sie das OSMC Media Center einrichten und nutzen.

.. image:: img/kodi/kodi0.png

OSMC ist eine Betriebssystem-Distribution, die Kodi als Media-Center-Software verwendet.

Ein Vorteil von OSMC ist die aktive Weiterentwicklung und die Basis eines vollständigen Betriebssystems, wodurch es problemlos erweitert werden kann. So lässt sich beispielsweise Netflix einfach einrichten, da der Backend leicht zugänglich ist.

Für die beste Kodi-Erfahrung empfehlen wir die Verwendung eines Raspberry Pi 4 oder neuer. Ein leistungsfähiger Prozessor und mehr Arbeitsspeicher sorgen für eine optimale Performance.

Komponentenliste
-----------------------

**Erforderlich**

* Pironman
* Micro-SD-Karte (8 GB oder mehr)
* Ethernet-Kabel oder WLAN
* HDMI-Kabel
* Monitor
* Tastatur und Maus

**Optional**

* M.2 SATA SSD

Installation des OSMC-Images
---------------------------------

In diesem Abschnitt erfahren Sie, wie Sie ein OSMC-Image auf einer Micro-SD-Karte installieren. Traditionell kamen Brennprogramme wie Etcher und Win32 Disk Imager zum Einsatz, doch mittlerweile bietet Raspberry Pi den Raspberry Pi Imager an, ein All-in-One-Tool zur einfachen Image-Installation.

#. Falls Sie den |link_imager| noch nicht haben, laden Sie ihn bitte herunter.

#. Öffnen Sie den Raspberry Pi Imager und klicken Sie auf **CHOOSE OS**.

    .. image:: img/kodi/kodi1.png

#. Klicken Sie auf die Schaltfläche **Media player OS**. Hier stehen zwei Kodi-Images zur Auswahl.

    .. image:: img/kodi/kodi2.png

#. Wir entscheiden uns für **OSMC**.

    .. image:: img/kodi/kodi6.png

#. Versionen für Raspberry Pi 0/1, 2/3 und 4/400 stehen zur Verfügung; wählen Sie die passende Version aus.

    .. image:: img/kodi/kodi7.png

#. Nach Auswahl des richtigen Laufwerks klicken Sie auf "Schreiben".

    .. image:: img/kodi/kodi8.png

#. Sobald die Meldung "Installation erfolgreich" erscheint, können Sie die Micro-SD-Karte entfernen.

    .. image:: img/kodi/kodi9.png

Ersteinrichtung von OSMC auf dem Raspberry Pi
-------------------------------------------------

Nachdem OSMC nun auf der SD-Karte installiert ist, führen wir Sie durch die Ersteinrichtung.

#. Entnehmen Sie die Micro-SD-Karte und stecken Sie sie in den Kartensteckplatz des Piron.

    .. image:: img/kodi/connect_power.jpg

#. Verbinden Sie Ihren Monitor mit dem Pironman über das HDMI-Kabel und schalten Sie das Gerät ein.

#. Beim ersten Start von OSMC wird Ihnen der folgende Bildschirm angezeigt. Bitte warten Sie, bis der Einrichtungsvorgang abgeschlossen ist, bevor Sie mit unserer OSMC-Anleitung fortfahren.

    .. image:: img/kodi/kodi10.png

#. Nach Abschluss der Installation muss der Pironman neu gestartet werden. Ein langer Druck auf den Ein-/Ausschalter oder das erneute Einstecken des Netzkabels führt zum Neustart.

#. Die Konfigurationsseite wird angezeigt und fragt nach der Sprachauswahl. Wählen Sie **Yes**, um die Einrichtung nach der Sprachauswahl fortzusetzen.

    .. image:: img/kodi/kodi11.png

#. Im nächsten Schritt werden Sie nach der Zeitzone gefragt. Wählen Sie die Zeitzone, in der Sie leben, um sicherzustellen, dass die Uhrzeit korrekt ist.

    .. image:: img/kodi/kodi12.png

#. Hier können Sie den Gerätenamen ändern. Der Standardname ist **osmc**; eine Änderung ist empfehlenswert.

    .. image:: img/kodi/kodi13.png

#. SSH kann in diesem Abschnitt aktiviert oder deaktiviert werden. OSMC aktiviert SSH standardmäßig. Klicken Sie auf **Accept**, um die Installation fortzusetzen.

    .. image:: img/kodi/kodi14.png

#. In diesem Schritt müssen Sie den Nutzungsbedingungen von OSMC und Kodi zustimmen. Nachdem Sie die Lizenz gelesen und akzeptiert haben, wählen Sie die Option **Continue**.

    .. image:: img/kodi/kodi15.png

#. Wählen Sie ein Design Ihrer Wahl. Für diese Anleitung verwenden wir das Standard-Design **OSMC**.

    .. image:: img/kodi/kodi19.png

#. Sie werden gefragt, ob Sie den OSMC-Newsletter abonnieren möchten. Wir setzen die Einrichtung mit der Option **No thanks** fort.

    .. image:: img/kodi/kodi20.png

#. Damit haben Sie die Erstkonfiguration von OSMC auf Ihrem Raspberry Pi abgeschlossen. Über die Option **Exit** gelangen Sie zum Hauptbildschirm von Kodi.

    .. image:: img/kodi/kodi21.png

Netzwerkkonfiguration in OSMC
--------------------------------------------

In diesem Abschnitt zeigen wir Ihnen, wie Sie das Netzwerk für Ihr Gerät über die OSMC-Benutzeroberfläche konfigurieren.

#. Gehen Sie zur Option **Settings**.

    .. image:: img/kodi/kodi22.png

#. Navigieren Sie dann zum Menü **My OSMC**.

    .. image:: img/kodi/kodi16.png

#. Wählen Sie **Netzwerk**. In diesem Menü finden Sie auch andere Optionen zur Konfiguration von OSMC auf Ihrem Raspberry Pi.

    .. image:: img/kodi/kodi17.png

#. Sie können WLAN konfigurieren oder einfach ein Netzwerkkabel anschließen. Nach der Verbindung wird die IP-Adresse angezeigt. Notieren Sie sich diese, da Sie sie später für den Fernzugriff benötigen.

    .. image:: img/kodi/kodi24.png

Dateiübertragung
-----------------

Manchmal müssen Dateien zwischen Ihrem OSMC-Gerät und Ihrem Computer übertragen werden, um bestehende Dateien zu bearbeiten, hinzuzufügen oder zu ändern.
Abhängig von Ihren Vorkenntnissen gibt es verschiedene Übertragungsmethoden. Einige funktionieren sofort (wenn SSH aktiviert ist), andere erfordern zusätzliche OSMC-Funktionen, wie einen Samba- (SMB-) oder FTP-Server.

**SFTP**

Um es einfach zu halten, konzentrieren wir uns auf SFTP mit FileZilla, da dies auf allen drei Plattformen (Windows, macOS und Linux) ohne zusätzliche Änderungen an OSMC funktioniert (sofern SSH aktiviert ist).

Wenn Sie FileZilla zum ersten Mal öffnen, müssen Sie Host, Benutzername und Passwort angeben.

* Host: sftp://ip-adresse-des-osmc
* Benutzername: osmc
* Passwort: osmc (oder das von Ihnen festgelegte Passwort)
* Port: kann freigelassen werden, um den Standard-SSH-Port 22 zu verwenden

Nach der Eingabe klicken Sie einfach auf die Schaltfläche "Schnellverbindung", um eine Verbindung herzustellen.

    .. image:: img/kodi/kodi37.png



**Samba Server**

Sie können Dateien auch über den SMB-Server übertragen, was eine intuitivere und nützlichere Methode ist. Allerdings müssen Sie zuerst zu OSMC gehen und diesen Server installieren. So geht's:

#. Öffnen Sie im **My OSMC** Menü die **App Store**-Ikone.

    .. image:: img/kodi/kodi28.png

#. Wählen Sie **Samba (SMB) Server** aus.

    .. image:: img/kodi/kodi29.png

#. Klicken Sie auf **Install**.

    .. image:: img/kodi/kodi30.png

#. Wählen Sie **Apply**, um die Installation des SMB-Servers zu starten.

    .. image:: img/kodi/kodi31.png

#. Oben rechts erscheint ein Pop-up, das Sie über den Installationsstatus informiert. Nach Abschluss der Installation können Sie von Ihrem Computer aus auf die Dateien Ihres Raspberry Pi zugreifen.

    .. image:: img/kodi/kodi32.png

#. Unter Windows öffnen Sie mit ``Win+R`` das Ausführen-Fenster.

    .. image:: img/kodi/kodi33.png

#. Geben Sie ``\\ip-Adresse`` in das Eingabefeld ein.

    .. image:: img/kodi/kodi34.png

#. Nun sehen Sie ein freigegebenes Laufwerk namens ``osmc``.

    .. image:: img/kodi/kodi35.png

#. Sobald Sie darauf klicken, werden verschiedene Ordner angezeigt, in die Sie jetzt Ihre Musik, Videos oder Filme übertragen können.

    .. image:: img/kodi/kodi36.png

OSMC-Videos für Scrape hinzufügen
-----------------------------------

In diesem Abschnitt zeigen wir Ihnen, wie Sie einen Videordner zu OSMC hinzufügen, damit dieser gescraped werden kann.

Videos zu scrapen ist ein recht einfacher Vorgang und gehört zu den Hauptfunktionen von Kodi.

#. Zuerst müssen wir zum **Video**-Menü gehen.

    .. image:: img/kodi/kodi45.png

#. Als nächstes wählen wir das **Files**-Untermenü aus. Hier können Sie bereits importierte Ordner durchsuchen oder neue hinzufügen.

    .. image:: img/kodi/kodi38.png

#. Wählen Sie nun die Option **Add video..** Hier werden Ordner hinzugefügt, die Kodi in der OSMC-Bibliothek scannen soll.

    .. image:: img/kodi/kodi39.png

#. In diesem Menü sollten Sie entweder die Option **Browse** oder **Add** auswählen.

    .. image:: img/kodi/kodi40.png

    * Mit **Browse** finden Sie Ordner über den OSMC-Dateibrowser.
    * Die Option **Add** ermöglicht es, den Pfad zum Verzeichnis manuell einzugeben.
    * Wählen Sie unabhängig von Ihrer Entscheidung den Ordner aus, in dem Ihre TV-Serien und Filme gespeichert sind, und klicken Sie auf **OK**.
    * Filme und TV-Serien sollten in getrennten Ordnern aufbewahrt werden, da Kodi sonst möglicherweise nicht zwischen ihnen unterscheiden kann.

        .. image:: img/kodi/kodi41.png

#. OSMC unterteilt Videos in drei Kategorien: **Movies**, **Music Videos** und **TV Shows**. Wählen Sie die Kategorie aus, die am besten zu Ihrem Video passt.

    .. image:: img/kodi/kodi43.png

#. Nachdem Sie den Medientyp ausgewählt haben, klicken Sie auf OK. OSMC wählt automatisch einen vertrauenswürdigen **information provider** aus, der zum Scrapen Ihrer Bibliothek verwendet wird.

    .. image:: img/kodi/kodi44.png

    OSMC wird Ihr Video scannen und nach dessen Namen in einer Internetdatenbank suchen. Mit diesem Scan können Poster, Schauspieler, Nachrichten und andere interessante Informationen über Ihr Video abgerufen werden.

    Nachdem Sie Ok ausgewählt haben, sollte der Scrape-Vorgang automatisch starten. Ihr Film oder Ihre TV-Serie sollte nun zur OSMC-Schnittstelle hinzugefügt worden sein.

Fernbedienung konfigurieren
----------------------------

Ein 38kHz IR-Empfänger ist im Pironman integriert und ist mit dem GPIO13-Pin verbunden. Damit können Sie Kodi mit einer Fernbedienung steuern.

**1. IR-Empfänger konfigurieren**

#. Navigieren Sie zu **Settings** -> **My OSMC** und wählen Sie das **Raspberry Pi**-Symbol aus.

    .. image:: img/kodi/kodi23.png

#. Wählen Sie **Hardware Support** und geben Sie die Pin-Nummer 13 in ``gpio_pin`` ein.

    .. image:: img/kodi/kodi25.png

    Nachdem Sie dies eingestellt haben, werden Sie aufgefordert, neu zu starten, um diese Konfiguration zu übernehmen.

**2. Fernbedienung auswählen**

#. Kodi unterstützt viele verschiedene Fernbedienungen. Befolgen Sie die Anweisungen zur Konfiguration. Gehen Sie zurück zum **My OSMC**-Menü und wählen Sie das **Remotes**-Symbol, um zur Konfigurationsseite zu gelangen.

    .. image:: img/kodi/kodi26.png

#. Wählen Sie die Marke Ihrer Fernbedienung aus der Liste aus.

    .. image:: img/kodi/kodi27.png

Jetzt können Sie Kodi mit Ihrer Fernbedienung steuern.

Weitere Informationen finden Sie unter: https://osmc.tv/wiki/.

**3. Fernbedienung manuell hinzufügen**

Das manuelle Konfigurieren einer Fernbedienung ermöglicht es, Ihre .conf-Datei zu erhalten, die zu Ihrer Fernbedienung passt. Fügen Sie sie zur **Remotes**-Liste hinzu und wählen Sie sie als aktuell zu verwendende Fernbedienung aus.

**i. Anmeldung über SSH**

Melden Sie sich jetzt über Ihren PC remote im OSMC-System an. Der Standardname und das Standardpasswort lauten ``osmc``.

Windows-Benutzer können hier einen SSH-Client namens PuTTY herunterladen.

Alternativ bieten einige Windows 10-Installationen Zugriff auf einen SSH-Client über die "PowerShell" im Windows Startmenü. Wenn Ihr Windows 10-System dies unterstützt, können Sie den Linux-Anweisungen folgen.

Linux- und OS X-Benutzer sollten bereits einen SSH-Client haben.

Sie können die IP-Adresse Ihres Geräts unter **Settings** -> **Systeme** -> **Netzwerk** finden.

* Windows

Starten Sie PuTTY, geben Sie die IP-Adresse Ihres Geräts ein und klicken Sie auf **OK**. Wenn Sie aufgefordert werden, geben Sie für den Benutzernamen und das Passwort jeweils ``osmc`` ein.

.. image:: img/kodi/kodi_remote1.png

* Linux / OS X

Öffnen Sie ein Terminal und führen Sie den folgenden Befehl aus:

.. code-block:: shell

    ssh osmc@<IP-Adresse Ihres Geräts>

Bei der ersten Verbindung zum Gerät werden Sie aufgefordert, den SSH-Schlüssel zu akzeptieren. Tippen Sie **yes** ein.


**ii. Erstellung einer LIRC-Konfigurationsdatei**

#. Stellen Sie sicher, dass Sie ``gpio_pin`` in OSMC über **Settings** -> **My OSMC** -> **Raspberry Pi** -> **Hardware Support** auf 13 gesetzt haben.

    .. image:: img/kodi/kodi25.png

#. Überprüfen Sie im Terminal, ob der Raspberry Pi Ihren IR-Empfänger erkennt. Führen Sie dazu den folgenden Befehl aus.

    .. code-block:: shell

        ls /dev/lirc*

    Eine Port-Meldung wie ``/dev/lirc0`` sollte erscheinen.

#. Nun überprüfen Sie, ob Daten von der Fernbedienung empfangen werden können.

    .. code-block:: shell

        sudo mode2 --driver default --device /dev/lirc0

#. Drücken Sie anschließend eine Taste auf der Fernbedienung und sehen Sie, ob eine Abfolge von Pulssignalen erscheint.

    .. code-block:: shell

        osmc@osmc:/etc/lirc$ sudo mode2 --driver default --device /dev/lirc0
        Verwende Treiber Standard für Gerät /dev/lirc0
        Versuche Gerät: /dev/lirc0
        Verwende Gerät: /dev/lirc0
        Als normaler Benutzer osmc ausgeführt
        space 16777215
        pulse 9083
        space 4442
        pulse 628
        space 509
        pulse 626
        space 508
        pulse 596
        space 543
        pulse 593
        space 538

#. Stoppen Sie nun lircd.

    .. code-block:: shell

        sudo killall lircd

#. Listet alle verfügbaren ``KEY_codes`` auf, um sie später zuzuordnen.

    .. code-block:: shell

        irrecord --list-namespace

#. Erstellen Sie nun eine ``.conf`` Konfigurationsdatei, die zu Ihrer Fernbedienung passt.

    .. code-block:: shell
        
        irrecord -d /dev/lirc0

    * Führen Sie einfach den oben genannten Befehl aus.
    * Drücken Sie die Eingabetaste zweimal.
    * Benennen Sie die Fernbedienung.
    * Halten Sie eine Taste gedrückt, bis die Meldung **Please enter the name ..** erscheint.
    * Beziehen Sie sich auf den vorherigen Befehl, um alle Tasten zu definieren.

    .. image:: img/kodi/kodi_remote.png

    * Nach der Konfiguration aller Tasten auf der Fernbedienung, drücken Sie Enter zum Beenden. Mit dem Befehl ``ls`` können Sie überprüfen, ob die konfigurierte ``.conf`` Datei existiert.

#. Kehren Sie nun zurück zu OSMC und klicken Sie auf **Settings** -> **My OSMC** -> **Remotes**.

    .. image:: img/kodi/kodi_remote2.png

#. Wählen Sie die .conf-Datei in Ihrem Home-Verzeichnis aus und bestätigen Sie mit OK.

    .. image:: img/kodi/kodi_remote4.png

#. Sobald die Datei ausgewählt ist, drücken Sie OK zur Bestätigung.

    .. image:: img/kodi/kodi_remote3.png

Ab diesem Zeitpunkt können Sie OSMC mit Ihrer Fernbedienung steuern.

