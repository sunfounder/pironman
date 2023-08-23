IR受信機
================

.. note::
    IR受信機はGPIO13に接続されています。別のピンに変更したい場合は、 :ref:`change_config` を参照してください。

IR受信機を使用する前に、接続をテストし、関連するモジュールをインストールする必要があります。

#. 下記のコマンドを使用してテストします。表示デバイスがあれば、設定が成功していると言えます。

    .. code-block:: shell

        sudo ls /dev |grep lirc

#. ``lirc`` モジュールをインストールします。

    .. code-block:: shell

        sudo apt-get install lirc -y

#. 以下のコマンドを実行し、リモートコントローラのキーを押すと、対応するキーのコードが表示されます。

    .. code-block:: shell

        mode2 -d /dev/lirc0

.. note::
    Raspberry PiでKodiを再生したい場合は、 :ref:`kodi_osmc` を参照してください。

