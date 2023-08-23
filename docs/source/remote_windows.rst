Windowsユーザー
=======================

Windowsを使用している場合、Windows PowerShellを使用してRaspberry Piにリモートでログインできます。

#. キーボードで ``windows`` + ``R`` ショートカットキーを押し、 **Run** プログラムを開きます。入力ボックスに **powershell** と入力してください。

    .. image:: img/sp221221_135900.png
        :align: center

#. Raspberry Piが同じネットワークにあるかどうかを確認するために、 ``ping <hostname>.local``  を入力します。

    .. code-block:: shell

        ping raspberrypi.local

    .. image:: img/sp221221_145225.png
        :width: 550
        :align: center

    * ターミナルが ``Ping request could not find host <hostname>.local`` と提示する場合、Raspberry Piがネットワークに接続できなかった可能性があります。ネットワークを確認してください。
    * ``<hostname>.local`` にピングを送ることができない場合は、 :ref:`get_ip` を参照して ``ping <IPアドレス>`` を試してください。 (例: ``ping 192.168.6.116``)
    * "Reply from <IPアドレス>: bytes=32 time<1ms TTL=64" のようなメッセージが複数回表示される場合、コンピュータはRaspberry Piにアクセスできることを意味します。

#. ``ssh <username>@<hostname>.local`` (または ``ssh <username>@<IPアドレス>``) を入力します。

    .. code-block:: shell

        ssh pi@raspberrypi.local

#. 以下のメッセージが表示される場合があります。

    .. code-block::

        'raspberrypi.local (192.168.6.116)'の真正性を確認できません。
        ECDSAキーの指紋はSHA256:7ggckKZ2EEgS76a557cddfxFNDOBBuzcJsgaqA/igz4です。
        接続を続行しますか (yes/no/[fingerprint])？

    "yes" と入力します。

#. 以前に設定したパスワードを入力します。（私の場合は ``raspberry`` です。）

    .. note::
        パスワードを入力すると、文字はウィンドウに表示されません。これは正常です。正しいパスワードを入力するだけです。

#. Raspberry Piに接続が完了しました。次のステップに進みましょう。

    .. image:: img/sp221221_140628.png
        :width: 550
        :align: center

リモートデスクトップ
---------------------

コマンドウィンドウを使用してRaspberry Piにアクセスするのに満足していない場合、リモートデスクトップ機能を使用して、GUIを使用してRaspberry Pi上のファイルを簡単に管理することもできます。

ここでは `VNC® Viewer <https://www.realvnc.com/en/connect/download/viewer/>`_ を使用します。

**VNCサービスを有効にする**

VNCサービスはシステムにインストールされています。デフォルトでは、VNCは無効になっています。それをconfigで有効にする必要があります。

#. 以下のコマンドを入力します：

    .. raw:: html

        <run></run>

    .. code-block:: shell 

        sudo raspi-config

#. キーボードの下矢印キーを押して **3** **Interfacing Options** を選び、 **Enter** キーを押します。

    .. image:: img/image282.png
        :align: center

#. 次に **P3 VNC** を選択します。 

    .. image:: img/image288.png
        :align: center

#. キーボードの矢印キーを使用して、 **<Yes>** -> **<OK>** -> **<Finish>** を選択し、設定を完了します。

    .. image:: img/mac_vnc8.png
        :align: center

**VNCにログインする**

#. パーソナルコンピューター上で `VNC Viewer <https://www.realvnc.com/en/connect/download/viewer/>`_ をダウンロードしてインストールする必要があります。

#. インストールが完了したら、それを開きます。次に、ホスト名またはIPアドレスを入力し、Enterを押します。

    .. image:: img/vnc_viewer1.png
        :align: center

#. Raspberry Piの名前とパスワードを入力した後、 **OK** をクリックします。

    .. image:: img/vnc_viewer2.png
        :align: center

#. Raspberry Piのデスクトップが表示されます。

    .. image:: img/login1.png
        :align: center

