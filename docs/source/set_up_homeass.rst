.. _set_up_homeass:


Home Assistantのセットアップ
==================================

**ステップ1**

この手順は、Pironman OLEDを起動するためのI2Cインターフェースを有効にするものです。

ファイルエクスプローラを開き、 ``Hassio-boot`` という名前のSDカードにアクセスします。

.. image:: img/sp230628_095957.png

ルートパーティションに ``CONFIG`` という新しいフォルダを作成します。

.. image:: img/sp230628_100453.png

``CONFIG`` フォルダの中に ``modules`` というフォルダを作成します。

.. image:: img/sp230628_101108.png

ファイル拡張子の表示を有効にします。

.. image:: img/sp230628_101216.png

``modules`` フォルダ内にテキストファイルを作成し、それを ``rpi-i2c.conf`` にリネームします。拡張子の変更を確認するプロンプトが表示されるので、「はい」を選択します。

.. image:: img/sp230628_101545.png

Notepadで ``rpi-i2c.conf`` を開き、以下の内容を追加します：

.. code-block::

    i2c-dev

ファイルを保存して閉じます。

**ステップ2**

このステップでは、RGB LEDの設定を行います。

#. ``Hassio-boot`` ディレクトリの ``config.txt`` というファイルを開きます。

    .. image:: img/sp230628_102441.png

#. 下部に以下の内容を追加します：

    .. code-block::

        dtparam=i2c_vc=on
        dtparam=i2c_arm=on
        dtoverlay=gpio-poweroff,gpio_pin=26,active_low=0
        dtoverlay=gpio-ir,gpio_pin=13

#. WS2812 LEDストリップを駆動するために使用するピンを特定することが重要です。

    .. image:: img/strip_select.png

    * デフォルトのSPIピン（GPIO10）を使用している場合、SPIを有効にし、周波数を500bpsに設定するために、以下のコマンドを ``config.txt`` ファイルに追加する必要があります。

        .. code-block::

            dtparam=spi=on
            core_freq=500
            core_freq_min=500
            # 必要に応じてオーディオを有効にします。
            dtparam=audio=on
    
    * オーディオ出力にも使用されるPWM（GPIO12）を使用している場合、オーディオを無効にする必要があります。 ``config.txt`` ファイルに以下のコマンドを挿入します：

        .. code-block::

            dtparam=audio=off

    * PCM（GPIO21）を使用している人は、追加のセットアップは不要です。ただし、 ``hifiberry-dac`` や ``i2s-mmap`` のようなI2Sデバイスと競合する可能性があります。これらを無効にし、必要に応じてオーディオをオンにします。

        .. code-block::

            # 必要に応じてオーディオを有効にします。
            dtparam=audio=on
            # i2sデバイスのコメントアウトをします。
            # dtoverlay=hifiberry-dac
            # dtoverlay=i2s-mmap

#. 最後に、このファイルを保存して閉じます。

**ステップ3**

次に、PironmanのWiFi設定を行います。

.. note:: ネットワークアクセスに有線接続を使用する予定の場合、この手順はスキップできます。

``CONFIG`` フォルダ内に ``network`` というフォルダを作成します。

.. image:: img/sp230628_113426.png

``network`` フォルダ内に、拡張子なしの新しいテキストファイル ``my-network`` を作成します。

.. image:: img/sp230628_113506.png

``my-network`` ファイルに、以下のテキストを書き込み、 ``MY_SSID`` および ``MY_WLAN_SECRET_KEY`` を自分のネットワークのSSIDとパスワードに置き換えます：

.. code-block::

    [connection]
    id=my-network
    uuid=72111c67-4a5d-4d5c-925e-f8ee26efb3c3
    type=802-11-wireless

    [802-11-wireless]
    mode=infrastructure
    ssid=MY_SSID
    # SSIDがブロードキャストされていない場合は、以下のコメントを解除します
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

ファイルを保存して終了します。

**ステップ4**

コンピュータからmicroSDカードを取り出し、Raspberry Piに挿入してください。その後、電源（必要であればイーサネットケーブルも）を接続します。

PCに戻り、 ``homeassistant.local:8123`` にアクセスします。
それが機能しない場合は、ルーターでIPアドレスを確認してください。

Home Assistantを初めて使用する際、初期設定が行われるため、しばらく待つ必要があります。

.. image:: img/sp230628_141749.png

**ステップ5**

次に、最初のアカウントを作成するように求められます。

.. image:: img/sp230627_135949.png

システムは、検出されたデバイスのインストールを促しますが、今は「FINISH」をクリックしてスキップできます。

.. image:: img/sp230627_141016.png

**ステップ6**

次に、Home Assistant用のPironmanアドオンをインストールします。

下のボタンをクリックしてすぐに追加してください。その後、 **ステップ7** に進んでください。

.. raw:: html

    <a href="https://my.home-assistant.io/redirect/supervisor_addon/?addon=6fa7f6d2_pironman&repository_url=https%3A%2F%2Fgithub.com%2Fsunfounder%2Fhome-assistant-addon" target="_blank"><img src="https://my.home-assistant.io/badges/supervisor_addon.svg" alt="Open your Home Assistant instance and show the dashboard of a Supervisor add-on." /></a>

または、手動でインストールするには以下の手順に従ってください：

1. Home Assistantで「Settings」->「Addons」に移動します。

    .. image:: img/sp230628_150312.png

2. 右下の「Addon Store」ボタンをクリックします。

    .. image:: img/sp230628_150338.png

3. 右上のメニューボタンをクリックし、「Repositories」を選択します。

    .. image:: img/sp230627_145728.png

4. リポジトリのURLを入力: ``https://github.com/sunfounder/home-assistant-addon`` , 「Add」をクリックします。SunFounderのリポジトリを追加したら、ポップアップウィンドウを閉じます。

    .. image:: img/sp230627_150423.png

5. メニューボタンを再びクリックし、「Check for updates」をクリックします。

    .. image:: img/sp230627_150716.png

6. 数秒後、Pironmanアドオンがアドオンストアの最後に表示されます。表示されない場合は、ページをリフレッシュしてみてください。

    .. image:: img/sp230627_150717.png

**ステップ7**

Pironmanアドオンに入り、「インストール」をクリックします。このプロセスには数分かかる場合があります。

.. image:: img/sp230627_150840.png

現在、アドオンがハードウェア情報にアクセスできるように保護モードを無効にする必要があります。 「Protection Mode」を見つけてオフにします。その後、アドオンを起動（または再起動）します。

.. image:: img/sp230627_153858.png

この時点で、Pironmanの照明効果とOLEDディスプレイが点灯するはずです。これは、設定が完了したことを示しています。

トラブルシューティング
-------------------------

OLEDやRGBストリップが正常に起動しない場合は、「Log」ページに移動してください。

.. image:: img/sp230628_162143.png

.. code-block::

    [DEBUG] oled init failed:
    [Errno 2] No such file or directory
    Cannot open /dev/spidev0.0. spi_bcm2835 module not loaded?

.. code-block::

    [DEBUG] rgb_strip init failed:
    ws2811_init failed with code -13 (Unable to initialize SPI)

上記のログが表示される場合、設定が成功していないことを意味します。以下の手順に従ってください：

1. まず、Home Assistantをシャットダウンします。

    .. warning::

        強制的に電源を切ると、HassOSにダメージを与える可能性があります。以下のシャットダウン手順に従ってください：

        .. image:: img/sp230628_162821.png

        .. image:: img/sp230628_162906.png

        その後、電源プラグを抜く前に1分間待ってください。

2. このセクションの **ステップ1** と **ステップ2** を繰り返します (:ref:`set_up_homeass`) 。

3. SDカードをPironmanに再度挿入し、電源を接続し、1～2分待ちます。その後、ブラウザで ``http://homeassistant.local:8123/`` に移動します。Pironmanアドオンで「START」をクリックします。

    .. raw:: html

        <a href="https://my.home-assistant.io/redirect/supervisor_addon/?addon=6fa7f6d2_pironman&repository_url=https%3A%2F%2Fgithub.com%2Fsunfounder%2Fhome-assistant-addon" target="_blank"><img src="https://my.home-assistant.io/badges/supervisor_addon.svg" alt="Open your Home Assistant instance and show the dashboard of a Supervisor add-on." /></a>

4. しばらく待つと、Pironman (RGBストリップ & OLED) が点灯するはずです。

アドオン設定
-----------------------------

Pironmanの効果を「Settings」ページでカスタマイズできます。

.. image:: img/sp230628_164931.png

ここでは、以下を変更できます：

* OLEDに表示される温度の単位。
* OLED画面の明るさの持続時間。
* ファンが動作を開始する温度。
* RGBストリップの色と点滅モード。

変更を行った後、「SAVE」をクリックして設定を適用します。

