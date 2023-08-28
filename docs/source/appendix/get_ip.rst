.. _get_ip:

IP-Adresse ermitteln
========================

Es gibt verschiedene Möglichkeiten, die IP-Adresse herauszufinden. Zwei gängige Ansätze werden nachfolgend erläutert.

**Über den Router prüfen**

Falls Sie Zugriffsrechte auf den Router haben, etwa in einem Heimnetzwerk, können Sie die dem Raspberry Pi zugewiesenen Adressen über die Admin-Oberfläche des Routers einsehen.

Der Standard-Hostname des Raspberry Pi OS ist "raspberrypi". Diesen müssen Sie finden. (Falls Sie ArchLinuxARM verwenden, suchen Sie nach "alarmpi".)

**Netzwerksegment-Scan**

Alternativ können Sie ein Netzwerk-Scan durchführen, um die IP-Adresse des Raspberry Pi zu identifizieren. Dafür können Sie Software wie den **Advanced IP Scanner** verwenden.

Scannen Sie den festgelegten IP-Bereich, und die Namen aller verbundenen Geräte werden angezeigt. Ähnlich verhält es sich mit dem Standard-Hostname des Raspberry Pi OS, der "raspberrypi" ist, sofern Sie ihn nicht geändert haben.
