.. _rgb_strip:

WS2812 RGBストリップ
=======================

**ピン選択**

#. Raspberry Piは、WS2812 RGB LEDストリップの駆動に使用できる3つの高速信号駆動モードを持っています。ただし、これらのモードには他の用途があり、WS2812 RGB LEDストリップに使用すると、元々の機能が無効になります。

    .. image:: img/strip_select.png

    * SPI (IO10) はSPIインターフェース用。
    * PWM (IO12) はアナログオーディオ（3.5mmオーディオジャック）用。
    * PCM (IO21) はデジタルオーディオ（HDMIオーディオ）用。

#. デフォルトではSPI（IO10）ドライブモードが選択されています。組み立て過程で異なるピン（例: IO21）に切り替える場合は、対応する設定も変更する必要があります。

    .. code-block:: shell

        pironman -rp 21

**その他の設定**

WS1812 RGBストリップは、Pironmanのステータスを表示するために使用できる8つのRGB LEDを備えたライトストリップです。コマンドを使用してオン/オフを切り替えたり、色（デフォルトは青）、表示モード、変更率を変更することができます。

* WS2812 RGBストリップをオンにする。

.. code-block:: shell

    pironman  -rw on

* オフにする。

.. code-block:: shell

    pironman  -rw off

* その色を変更し、16進色値を使用する。

.. code-block:: shell

    pironman  -rc fe1a1a

* 表示モードを変更する。選択できる4つのモードがあります： ``breath``、 ``leap``、 ``flow``、 ``raise_up``。

.. code-block:: shell

    pironman  -rs leap

* 変更速度を変更する（0〜100%）。

.. code-block:: shell

    pironman  -rb 80

* 上記はWS2812 RGBストリップのために事前に設定したエフェクトです。他のエフェクトを表示させたい場合は、 ``/opt/pironman/ws2812_RGB.py`` を開いて変更して実行できます。

    このpythonスクリプトを開いて内容を変更します。

    .. code-block:: shell

        sudo nano /opt/pironman/ws2812_RGB.py

    ``Ctrl+X`` -> ``Y`` -> ``Enter`` を押して、編集を保存して終了します。

    実行します。

    .. code-block:: shell

        sudo python3 /opt/pironman/ws2812_RGB.py
