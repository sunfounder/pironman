.. _kodi_osmc:

Raspberry PiにOSMCを使用してKodiをインストール
================================================

|link_kodi| は、Raspberry Piでメディアを再生するためのもっとも人気のある方法の一つです。多くの異なるメディアフォーマットをサポートしており、このメディアセンターソフトウェアを使用して音楽、動画、画像を再生できます。

Kodiを使用すると、すべてのメディアファイルをスキャンしてソートできます。ファイルの情報をダウンロードし、魅力的な方法で表示します。

Raspberry PiのシステムにKodiを直接インストールすることも、 |link_osmc| や |link_libreelec| のようなKodiがプリインストールされているディストリビューションを使用することもできます。

このチュートリアルでは、OSMCメディアセンターのインストールとセットアップ方法を紹介します。

.. image:: img/kodi/kodi0.png

OSMCは、Kodiメディアセンターソフトウェアを使用するオペレーティングシステムのディストリビューションです。

OSMCの利点の一つは、完全なオペレーティングシステムの上に構築されており、組み込みのKodi機能を超えて簡単に拡張できることです。
例えば、バックエンドに簡単にアクセスできるので、Netflixを簡単にセットアップすることができます。

Kodiを最高の状態で使用するためには、Raspberry Pi 4以降のモデルの使用をおすすめします。高性能なプロセッサと増加したRAMが、Kodiの最適な動作をサポートします。

部品リスト
------------------

**必須**

* Pironman
* Micro SDカード（8GB以上）
* イーサネットケーブルまたはWi-Fi
* HDMIケーブル
* モニター
* キーボードとマウス

**オプション**

* M.2 SATA SSD

OSMCイメージのインストール
---------------------------------

このセクションでは、Micro SDカードにOSMCイメージをインストールする方法を学びます。従来はEtcherやWin32ディスクイメージャーなどの書き込みツールが使用されていましたが、Raspberry PiはRaspberry Pi Imagerを開発し、イメージとツールが一体となったもので、イメージのインストールが簡単になりました。

#. |link_imager| がない場合はダウンロードしてください。

#. Raspberry Pi Imagerを開き、 **CHOOSE OS** をクリックします。

    .. image:: img/kodi/kodi1.png

#. **Media player OS** ボタンをクリックします。このボタンをクリックすると、Kodi用の2つのイメージが表示されます。

    .. image:: img/kodi/kodi2.png

#. ここでは **OSMC** を選択します。

    .. image:: img/kodi/kodi6.png

#. Raspberry Pi 0/1、2/3、4/400のバージョンが提供されていますので、適切なバージョンを選択してください。

    .. image:: img/kodi/kodi7.png

#. 適切なドライブを選択した後、書き込みをクリックします。

    .. image:: img/kodi/kodi8.png

#. インストール完了のメッセージが表示されたら、Micro SDカードを取り出してください。

    .. image:: img/kodi/kodi9.png

Raspberry PiでのOSMCの初期セットアップ
-------------------------------------------------

OSMCをSDカードにインストールしたので、初期セットアップの手順を説明します。

#. Micro SDカードを取り出し、Pironのカードスロットに挿入します。

    .. image:: img/kodi/connect_power.jpg

#. HDMIケーブルでディスプレイをPironmanに接続し、電源スイッチで電源を入れます。

#. OSMCを初めて起動すると、次の画面が表示されます。OSMCのセットアップガイドを続ける前に、セットアッププロセスが完了するのを待ってください。

    .. image:: img/kodi/kodi10.png

#. インストールが完了したら、Pironmanを再起動する必要があります。電源スイッチを長押しするか、電源ケーブルを再接続して再起動できます。

#. 再起動すると、言語を選択するように求められる設定ページが表示されます。OSMCの言語を選択した後、 **Yes** を選択してセットアップを続けてください。

    .. image:: img/kodi/kodi11.png

#. 次に、タイムゾーンを選択するように求められます。正しい時間を確保するために、住んでいる場所の関連するタイムゾーンを選択してください。

    .. image:: img/kodi/kodi12.png

#. ここで、デバイスの名前を変更するかどうかを尋ねられます。デフォルトのデバイス名は **osmc** ですが、別の名前に変更することをおすすめします。

    .. image:: img/kodi/kodi13.png

#. このセクションでは、SSHサービスを無効または有効にすることができます。OSMCのセットアップツールはデフォルトでSSHを有効にします。インストールを続けるには、 **Accept** をクリックしてください。

    .. image:: img/kodi/kodi14.png

#. このステップでは、OSMCおよびKodiの利用規約に同意するように求められます。ライセンスを読んで同意した後、 **Continue** オプションを選択してください。

    .. image:: img/kodi/kodi15.png

#. 好みのテーマを選択します。このガイドでは、デフォルトの **OSMC** テーマを使用します。

    .. image:: img/kodi/kodi19.png

#. ここで、OSMCのニュースレターにサインアップするかどうかを尋ねられます。このガイドでは、 **No thanks** オプションを使用して続けます。

    .. image:: img/kodi/kodi20.png

#. この時点で、Raspberry Pi上のOSMCの初期設定プロセスを完了しました。 **Exit** オプションを選択することで、Kodiのメイン画面に移動できます。

    .. image:: img/kodi/kodi21.png

OSMCでのネットワーク設定
--------------------------------------------

このセクションでは、OSMCインターフェースを使用してデバイスのネットワークを設定する方法を示します。

#. **Settings** オプションに移動します。

    .. image:: img/kodi/kodi22.png

#. 次に、 **My OSMC** メニューに進みます。

    .. image:: img/kodi/kodi16.png

#. **Network** を選択します。このメニューには、Raspberry PiのOSMCを設定するのに役立つ他のオプションも含まれています。

    .. image:: img/kodi/kodi17.png

#. このオプションでWIFIを設定することができます。また、ネットワークケーブルを接続するだけで、接続に関する情報が表示され、後でOSMCにリモートでアクセスするためにこのIPアドレスを覚えておく必要があります。

    .. image:: img/kodi/kodi24.png


ファイル転送
-----------------

OSMCデバイスとコンピューターの間でファイルを編集、追加、または変更するためにファイルを転送する必要があることがあります。
経験に応じて、ファイルを転送する方法は多岐にわたります。これらの方法の中には、SSHが有効になっている場合にすぐに動作するものもあります。Samba (SMB) サーバーやFTPサーバーなどの追加のOSMC機能が必要な方法もあります。

**SFTP**

簡単さを重視して、FileZillaを使用したSFTPのみに焦点を当てます。これは、OSMCに追加の変更を加えずに（SSHが有効になっている必要があります）すべての三つのプラットフォーム（Windows、macOS、Linux）ですぐに動作します。

FileZillaを初めて開くと、ホスト、ユーザー名、パスワードを提供する必要があります。

* ホスト: sftp://あなたのosmcのipアドレス
* ユーザー名: osmc
* パスワード: osmc (または指定されたパスワード)
* ポート: デフォルトのSSHポート22を使用する場合は空白のままにできます。

これらを入力したら、接続を確立するためにクイック接続ボタンをクリックします。

    .. image:: img/kodi/kodi37.png


**Sambaサーバー**

SMBサーバーを使用してもファイルを転送することができます。これはより直感的で役立つ方法ですが、以下のようにしてOSMCにこのサーバーを最初にインストールする必要があります。

#. **My OSMC** メニューページに移動し、 **App Store** アイコンを選択します。

    .. image:: img/kodi/kodi28.png

#. **Samba (SMB) Server** を選択します。

    .. image:: img/kodi/kodi29.png

#. **Install** を選択します。

    .. image:: img/kodi/kodi30.png

#. SMBサーバーのインストールを開始するために **Apply** を選択します。

    .. image:: img/kodi/kodi31.png

#. 右上隅にポップアップが表示され、インストールを促します。インストールが完了すると、自分のコンピューターからRaspberry Piのファイルにアクセスできるようになります。

    .. image:: img/kodi/kodi32.png

#. Windowsで ``Win+R`` を使用してRun Boxを開きます。

    .. image:: img/kodi/kodi33.png

#. 入力ボックスに ``\\ipアドレス`` を入力します。

    .. image:: img/kodi/kodi34.png

#. すると、 ``osmc`` という名前の共有ドライブが表示されます。

    .. image:: img/kodi/kodi35.png

#. クリックすると、さまざまなフォルダが表示され、音楽、ビデオ、映画などをこれらのフォルダに転送することができます。

    .. image:: img/kodi/kodi36.png


OSMCのビデオをScrapeに追加する
-----------------------------------

このセクションでは、OSMCがスクレイプするためのビデオフォルダを追加する方法を説明します。

ビデオのスクレイピングはかなり簡単なプロセスであり、Kodiの主要な機能の一つです。

#. まず、 **Video** メニューに移動します。

    .. image:: img/kodi/kodi45.png

#. 次に、 **Files** サブメニューを選択します。このサブメニューでは、インポート済みのフォルダを閲覧するか、追加のフォルダを追加することができます。

    .. image:: img/kodi/kodi38.png

#. 次に、 **Add video..** オプションを選択します。このオプションでは、OSMCのKodiがライブラリにスキャンするためのフォルダを追加します。

    .. image:: img/kodi/kodi39.png

#. このメニューでは、 **Browse** または **Add** オプションを選択する必要があります。

    .. image:: img/kodi/kodi40.png

    * **Browse** オプションは、OSMCのファイルブラウザを使用してフォルダを検索することができます。
    * **Add** オプションを使用すると、ディレクトリへのパスを手動で入力できます。
    * どちらの方法を選択しても、テレビ番組や映画が格納されているフォルダを選択して、 **OK** をクリックします。
    * 映画とテレビ番組は別々のフォルダに分けて保存してください。
    * 同じフォルダに含まれている場合、Kodiのスクレイパはそれらを区別することができません。

        .. image:: img/kodi/kodi41.png

#. OSMCはビデオを3つのカテゴリー、 **Movies** 、 **Music Videos** 、 **TV Shows** に分けます。あなたのビデオに最も関連するオプションを選択します。選択するオプションによって、OSMCがビデオから情報を取得する方法が変わります。

    .. image:: img/kodi/kodi43.png

#. メディアの種類を選択した後、 **OK** を選択できます。OSMCはライブラリをスクレイプするために使用される信頼できる **情報提供者** を自動的に選択します。

    .. image:: img/kodi/kodi44.png

    OSMCはあなたのビデオをスキャンし、インターネット上のデータベースでその名前を検索します。このスキャンにより、ポスターや俳優、メッセージ、ビデオに関するその他の興味深い情報を取得することができます。

    OKを選択した後、スクレイピングプロセスが自動的に開始されるはずです。OSMCのインターフェースに映画やテレビ番組が追加されたことが確認できるでしょう。

リモートを設定する
----------------------------

Pironmanには38KHzのIRレシーバが組み込まれており、GPIO13ピンに接続されているため、リモートコントロールを使用してKodiを制御できます。

**1. IRレシーバを設定する**

#. **Settings** -> **My OSMC** メニューに移動し、 **Raspberry Pi** アイコンを選択します。

    .. image:: img/kodi/kodi23.png

#. **Hardware Support** を選択し、 ``gpio_pin`` に13と入力します。

    .. image:: img/kodi/kodi25.png

    設定が完了すると、この設定を有効にするために再起動するように求められます。

**2. リモートコントロールを選択する**

#. Kodiは多種多様なリモートをサポートしているため、それらを設定するための指示に従うことができます。 **My OSMC** メニューに戻り、 **Remotes** アイコンを選択して設定ページに進みます。

    .. image:: img/kodi/kodi26.png

#. リストから使用しているリモートのブランドを選択します。

    .. image:: img/kodi/kodi27.png

Kodiはあなたのリモートで制御することができます。

詳細については、次のURLを参照してください：https://osmc.tv/wiki/。

**3. リモートを手動で追加する**

リモートを手動で設定することは、あなたのリモートに適した.confファイルを取得し、 **リモート** リストに追加し、現在使用するものとして選択する方法です。

**i. SSH経由でのログイン**

PCからOSMCシステムにリモートでログインします。デフォルトの名前とパスワードは ``osmc`` です。

Windowsユーザーは、ここでPuTTYというSSHクライアントをダウンロードできます。

代わりに、一部のWindows 10のインストールでは、Windowsのスタートメニューから“PowerShell”を使用してコマンドラインのSSHクライアントにアクセスできます。Windows 10システムがこれをサポートしている場合、Linuxの手順を使用できます。

LinuxおよびOS Xのユーザーは既にSSHクライアントを持っているはずです。

デバイスのIPアドレスは、 **Settings** -> **Systems** -> **Network** で見ることができます。

* Windows

PuTTYを実行し、デバイスのIPアドレスを入力して、 **OK** をクリックします。求められた場合、ユーザー名とパスワードの両方として ``osmc`` を入力します。

.. image:: img/kodi/kodi_remote1.png

* Linux / OS X

ターミナルインターフェースを開き、以下のコマンドを実行します：

.. code-block:: shell

    ssh osmc@<あなたのデバイスのIPアドレス>

このデバイスに初めて接続する場合、SSHキーを受け入れるように求められます。 **yes** と入力します。


**ii. LIRC設定ファイルの作成**

#. ``gpio_pin`` がOSMCの **Settings** -> **My OSMC** -> **Raspberry Pi** -> **Hardware Support** で13に設定されていることを確認してください。

    .. image:: img/kodi/kodi25.png

#. ターミナルで、Raspberry PiがIRレシーバを検出しているかどうかを次のコマンドで確認します。

    .. code-block:: shell

        ls /dev/lirc*

    ``/dev/lirc0`` のようなポートメッセージが表示されるはずです。

#. 次に、リモートからデータを受信できるかどうかを確認します。

    .. code-block:: shell

        sudo mode2 --driver default --device /dev/lirc0

#. リモートのボタンを押し、パルスデータの文字列が表示されるかどうかを確認します。

    .. code-block:: shell

        osmc@osmc:/etc/lirc$ sudo mode2 --driver default --device /dev/lirc0
        Using driver default on device /dev/lirc0
        Trying device: /dev/lirc0
        Using device: /dev/lirc0
        Running as regular user osmc
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

#. lircdを停止します。

    .. code-block:: shell

        sudo killall lircd

#. すべての利用可能な ``KEY_codes`` を後でマッチングするために取得します。

    .. code-block:: shell

        irrecord --list-namespace

#. これで、リモートに適した ``.conf`` 設定ファイルを作成します。

    .. code-block:: shell
        
        irrecord -d /dev/lirc0

    * 上記のコマンドを実行するだけです。
    * Enterキーを2回押します。
    * リモートコントロールに名前を付けます。
    * **Please enter the name ..** が表示されるまで、キーを押し続けてサンプルを取ります。
    * すべてのキーを定義するために前のコマンドを参照してください。

    .. image:: img/kodi/kodi_remote.png

    * リモートのすべてのキーを設定した後、Enterを押して終了します。 ``ls`` コマンドを使用して、設定した ``.conf`` ファイルが存在しているかどうかを確認できます。

#. これで、OSMCに戻って、 **Settings** -> **My OSMC** -> **Remotes** をクリックします。

    .. image:: img/kodi/kodi_remote2.png

#. Browseを使用してHomeフォルダの下にある.confファイルを選択します。

    .. image:: img/kodi/kodi_remote4.png

#. 一度選択すると、OKを押して選択し、変更を確認します。

    .. image:: img/kodi/kodi_remote3.png

この時点で、リモートを使用してOSMCを制御できるようになります。


