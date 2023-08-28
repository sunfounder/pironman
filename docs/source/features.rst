Eigenschaften
======================

**Funktionen**

* Raspberry Pi Mini-PC
* Tower-Kühler kann einen Raspberry Pi bei 100% CPU-Auslastung auf 39°C bei einer Raumtemperatur von 25°C kühlen
* Integrierter USB zu M.2 SATA SSD, TRIM wird unterstützt
* IR-Empfänger für Multimedia-Center wie Kodi oder Volumio
* RGB-Lüfter, steuerbar über GPIO
* 16 WS2812 adressierbare RGB LEDs erleuchten das gesamte Gehäuse mit coolen Lichteffekten
* Retro-Metall-Anschaltknopf mit Kontrollleuchte für sicheres Herunterfahren
* 0.96" OLED-Display zeigt CPU-Auslastung, Temperatur, Festplattennutzung, IP-Adresse, RAM-Nutzung des Raspberry Pi usw.
* Externer GPIO-Erweiterungsanschluss mit Pin-Beschriftung für einfachen Zugang
* Speicherung des Power-Status zur Wiederherstellung nach einem versehentlichen Stromausfall
* Neuanordnung der microSD-Karte für einfachen Zugang
* Aluminium-Hauptkörper mit klarem Acryl-Seitenpanel

**Parameter**

1. Abmessungen: 112.45x68.2x118.92mm
2. Material
    a. Hauptkörper: Aluminiumlegierung
    b. Beidseitige und vordere Panel: Acryl
3. Unterstützte Plattform: Raspberry Pi 4B
4. Stromversorgung: USB Typ C 5V/3A
5. Nennleistung: 5V/800mA
6. Schnittstellen (d ~ i sind die original freigelegten Schnittstellen des Raspberry Pi)
    a. Raspberry Pi standard 40-Pin GPIO
    b. micro SD
    c. USB Typ C Stromanschluss
    d. USB 2.0 x 2
    e. USB 3.0
    f. Gigabit LAN-Port
    g. USB Typ C Raspberry Pi Stromversorgung (direkte Stromversorgung des Raspberry Pi, nicht empfohlen)
    h. micro HDMI x 2
    i. 3.5mm Kopfhöreranschluss
7. Anschaltknopf
8. OLED-Bildschirm: 0.96'' 128x64 Auflösung
9. Infrarotempfänger: 38KHz
10. Kühlventilator: Größe 40x40x10mm
11. WS2812 RGB LED: 16xWS2812B-5050

**Pin-Funktionen**

.. image:: img/pin_define.png

* **Shutdown Signal Pin**: Durch Drücken des Power-Buttons wird der Raspberry Pi ausgeschaltet und dabei GPIO26 auf ein hohes Level gesetzt. Wenn das Hauptboard dieses hohe Level erkennt, wird der Strom abgeschaltet.

**Abmessungszeichnung**

.. image:: img/pironman_dimension.png
    :width: 800
