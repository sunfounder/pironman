5. Pironmanの設定
===================================

.. note::
    * このPironmanはPCと同じ方法で使用され、電源をオン/オフするための電源ボタンが必要です。

.. _change_config:

互換性のあるシステム
-----------------------------------

Pironmanと互換性のあるシステムは以下のとおりです。

.. image:: img/compitable_system.png

あなたのシステムに ``git``、 ``python3`` 、 ``pip`` がプリインストールされていない場合、まずそれらをインストールする必要があります。

.. code-block:: shell

    sudo apt-get update
    sudo apt-get install git -y
    sudo apt-get install python3 python3-pip python3-setuptools -y


``pironman`` モジュールのインストール
--------------------------------------

以下のコマンドを使用して ``pironman`` モジュールをダウンロードおよびインストールします。

.. code-block:: shell

    cd ~
    git clone https://github.com/sunfounder/pironman.git -b v2.0
    cd ~/pironman
    sudo python3 install.py

.. warning::  ディレクティブの中の ``-b v2.0`` は必須です

インストール後、変更を反映するために再起動が必要です。ある時点で再起動のリマインダーが表示され、すぐに再起動するか、後で再起動するかを選択できます。

Pironmanの基本的な設定は以下の通りです。

   * OLED画面にはRaspberry PiのCPU、RAM、ROMの使用状況、CPU温度、IPアドレスが表示されます。
   * 60秒後、OLEDディスプレイはスリープモードに入り、電源ボタンを短く押すことで起動できます。
   * ファンは50度セルシウスでオンになります。
   * WS2812 RGBストリップをオンにして、色#0a1aff（青）で表示し、変更率が50％のブレスモードになります。
   * この時点で、2秒間押し続けて安全にシャットダウンするか、10秒間押し続けて強制的にシャットダウンすることができます。

設定の変更
-----------------------------

``pironman`` モジュールには、Pironmanの基本設定がいくつかあり、以下のコマンドでそれらを確認できます。

.. code-block:: shell

    pironman -c

現在の設定は以下のとおりです。

   * ファンは50度セルシウスでオンになります。
   * OLEDディスプレイの持続時間は60秒で、60秒後にスリープを開始します。
   * WS2812 RGBストリップをオンにして、色#0a1affで表示し、変更率が50％のブレスモードになります。

.. image:: img/pironman_c.jpg
    :align: center

これらの設定を自分のニーズに合わせて変更することもできます。

``pironman`` 、 ``pironman -h`` 、または ``pironman --help`` を使用して、次のような指示を表示します。

.. code-block:: shell

    使用法:
        pironman <オプション> <入力>

    オプション:
        start            pironmanサービスを開始

        stop             pironmanサービスを停止

        restart          pironmanサービスを再起動

        -h,--help        ヘルプ、このヘルプを表示

        -c,--check       すべての設定を表示

        -a,--auto        [ on ], ブート時の自動起動を有効にする
                         [ off ], ブート時の自動起動を無効にする

        -u,--unit        [ C/F ], 温度の単位を設定、
                             CまたはF（セルシウス/華氏）

        -f,--fan         [ temp ], ファンがオンになる温度、
                         セルシウス（デフォルト50）、範囲（30〜80）

        -al,--always_on  [on/off], 画面が常にオンかどうか、
                         デフォルトはFalse

        -s,--staty_time  [time], 画面の表示時間（秒）、
                         秒、デフォルト30

        -rw,--rgb_sw     [on/off], rgbストリップスイッチ

        -rs,--rgb_style  rgbストリップの表示スタイル、デフォルト：ブレス、
                         [breath / leap / flow / raise_up / colorful] の中から

        -rc,--rgb_color  [(HEX)color], rgbストリップの色を設定、
                         デフォルト: 0a1aff

        -rb,--rgb_speed  [speed], rgb点滅速度（0〜100, デフォルト50）

        -pwm,--rgb_pwm   [frequency], rgb信号の周波数（400〜1600, デフォルト1000 kHz）

        -rp,--rgb_pin    [pin], rgb信号ピン、次のようにすることができます [10 / spi/ SPI / 12 / pwm/ PWM] または
                         [21 / pcm / PCM], デフォルト10

例えば、ブート時のプログラムの自動実行をオフにする場合。

.. code-block:: shell

    pironman -a off

または、WS2812 RGBストリップの色をリセットする。

.. code-block:: shell

    pironman -rc ff8a40

これらの設定は ``/opt/pironman/config.txt`` に保存されており、このファイルを直接編集して変更することもできます。

.. code-block:: shell

    sudo nano /opt/pironman/config.txt

.. image:: img/pironman_config.jpg
    :align: center

編集を保存して終了するには、 ``Ctrl+X`` -> ``Y`` -> ``Enter`` を押します。

.. note::
    Pironmanコンポーネントの紹介および設定は、以下のリンクで見ることができます: :ref:`about_hardware`。

