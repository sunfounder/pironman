
Mac OS Xユーザー
==========================

Macユーザーにとって、Raspberry PiのデスクトップをVNC経由で直接アクセスする方が、コマンドラインからのアクセスより便利です。Raspberry PiでVNCを有効にした後、Finderを使用して設定済みのアカウントのパスワードを入力することでアクセス可能です。

この方法ではMacとRaspberry Pi間の通信が暗号化されません。通信は家庭やビジネスのネットワーク内で行われるので、保護されていなくても問題にはなりません。しかし、セキュリティを気にする場合は、 `VNC® Viewer <https://www.realvnc.com/en/connect/download/viewer/>`_ のようなVNCアプリケーションをインストールすることを検討してください。

また、一時的なモニター（テレビ）、マウス、キーボードを使用して、Raspberry Piのデスクトップを直接開き、VNCを設定するのも便利です。それが不可能な場合でも、SSHコマンドを使ってRaspberry PiのBashシェルを開き、そこからVNCをセットアップすることができます。

* :ref:`have_temp_monitor`
* :ref:`no_temp_monitor`

.. _have_temp_monitor:

一時的なモニター（またはテレビ）をお持ちですか？
---------------------------------------------------------------------

#. Raspberry Piにモニター（またはテレビ）、マウス、キーボードを接続し、電源を入れます。画像に示される数字に従ってメニューを選択してください。

    .. image:: img/mac_vnc1.png
        :align: center

#. 次の画面が表示されます。 **Interfaces** タブで **VNC** を **Enabled** に設定し、 **OK** をクリックしてください。

    .. image:: img/mac_vnc2.png
        :align: center

#. 画面の右上にVNCのアイコンが表示され、VNCサーバーが起動します。

    .. image:: img/login1.png
        :align: center

#.  **VNC** アイコンをクリックしてVNCサーバーウィンドウを開き、右上の **Menu** ボタンをクリックし、 **Options** を選択します。

    .. image:: img/mac_vnc4.png
        :align: center

#. 以下の画面が表示され、ここでオプションを変更することができます。

    .. image:: img/mac_vnc5.png
        :align: center

    **Encryption** を **Prefer off** 、 **Authentication** を **VNC password** に設定してください。

#.  **OK** をクリックすると、パスワード入力の画面が表示されます。Raspberry piのパスワードと同じ、または異なるパスワードを使用できますので、入力し **OK** をクリックしてください。

    .. image:: img/mac_vnc16.png
        :align: center

    これでMacから接続する準備が整いました。モニターを切断しても問題ありません。

**ここからはMac側の操作となります。**

#. Finderのメニューから **Connect to Server** を選択します。右クリックからも開くことができます。

    .. image:: img/mac_vnc10.png
        :align: center

#.  ``vnc://<username>@<hostname>.local`` または ``vnc://<username>@<IP address>`` と入力し、 **Connect** をクリックします。

    .. image:: img/mac_vnc11.png
        :align: center

#. パスワードの入力を求められるので、正確に入力してください。

    .. image:: img/mac_vnc12.png
        :align: center

#. Raspberry piのデスクトップが表示され、そのままMacから操作できるようになります。

    .. image:: img/mac_vnc13.png
        :align: center

.. _no_temp_monitor:

一時的なモニタ（またはTV）を持っていない場合
---------------------------------------------------------------------------

* Raspberry PiのBashシェルを開くには、SSHコマンドを使用できます。
* BashはLinuxの標準デフォルトシェルです。
* シェル自体は、ユーザーがUnix/Linuxを使用する際のコマンド（指示）です。
* 必要な操作のほとんどはシェルを通じて行うことができます。
* Raspberry Pi側の設定が完了したら、Macの **Finder** を使用してRaspberry Piのデスクトップにアクセスできます。

#.  ``ssh <username>@<hostname>.local`` と入力してRaspberry Piに接続します。

    .. code-block:: shell

        ssh pi@raspberrypi.local

    .. image:: img/mac_vnc14.png

#. 以下のメッセージは初回ログイン時のみ表示されるので、 **yes** と入力します。

    .. code-block::

        raspberrypi.local (2400:2410:2101:5800:635b:f0b6:2662:8cba)の真正性は確立できません。
        ED25519キーのフィンガープリントはSHA256:oo7x3ZSgAo032wD1tE8eW0fFM/kmewIvRwkBys6XRwgです。
        このキーは他の名前で知られていません。
        続行して接続してもよろしいですか（yes/no/[フィンガープリント]）？

#. Raspberry Piのパスワードを入力します。入力したパスワードは表示されませんので、間違いのないように注意してください。

    .. code-block::

        pi@raspberrypi.localのパスワード: 
        Linux raspberrypi 5.15.61-v8+ #1579 SMP PREEMPT Fri Aug 26 11:16:44 BST 2022 aarch64

        Debian GNU/Linuxとともに提供されるプログラムは無料ソフトウェアです。
        各プログラムの具体的な配布条件は、/usr/share/doc/*/copyrightにある
        個別のファイルで説明されています。

        Debian GNU/Linuxは、適用可能な法律の範囲で、絶対に保証されません。
        最終ログイン: Thu Sep 22 12:18:22 2022
        pi@raspberrypi:~ $ 

#. MacからVNCでログインできるようにRaspberry Piを設定します。まず、以下のコマンドを実行して、OSを更新します。

    .. code-block:: shell

        sudo apt update
        sudo apt upgrade

    ``続行しますか？ [Y/n]`` と表示されたら、 ``Y`` を入力します。

    アップデートには時間がかかる場合があります。（その時のアップデート量によります）

#. **VNC Server** を有効にするには、以下のコマンドを入力します。

    .. code-block:: shell

        sudo raspi-config

#. 次の画面が表示されます。キーボードの矢印キーで **3 Interface Options** を選択し、 **Enter** キーを押します。

    .. image:: img/image282.png
        :align: center

#. 次に、 **P3 VNC** を選択します。

    .. image:: img/image288.png
        :align: center

#. キーボードの矢印キーを使用して **<Yes>**  ->  **<OK>**  ->  **<Finish>** を選択して、設定を完了します。

    .. image:: img/mac_vnc8.png
        :align: center

#. VNCサーバが起動したので、Macからの接続設定を変更しましょう。

    すべてのユーザーアカウントのすべてのプログラムのパラメータを指定するには、 ``/etc/vnc/config.d/common.custom`` を作成します。

    .. code-block:: shell

        sudo nano /etc/vnc/config.d/common.custom

    ``Authentication=VncAuthenter`` を入力した後、 ``Ctrl+X`` -> ``Y`` -> ``Enter`` で保存して終了します。

    .. image:: img/mac_vnc15.png
        :align: center

#. さらに、MacからVNC経由でログインする際のパスワードを設定します。Raspberry Piのパスワードと同じものや異なるものを使用することができます。

    .. code-block:: shell

        sudo vncpasswd -service

#. 設定が完了したら、変更を適用するためにRaspberry Piを再起動します。

    .. code-block:: shell

        sudo sudo reboot

#. 次に、 **Finder** のメニューから **Connect to Server** を選択します。右クリックで開くことができます。

    .. image:: img/mac_vnc10.png
        :align: center

#. ``vnc://<username>@<hostname>.local`` （または ``vnc://<username>@<IPアドレス>`` ）と入力します。入力後、 **Connect** をクリックします。

        .. image:: img/mac_vnc11.png
            :align: center

#. パスワードが要求されるので、入力してください。

        .. image:: img/mac_vnc12.png
            :align: center

#. Raspberry piのデスクトップが表示され、そのままMacから操作することができます。

        .. image:: img/mac_vnc13.png
            :align: center
