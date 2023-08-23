OLEDスクリーン
===================

インストール後、スクリプトは自動的に起動し、OLEDスクリーンにRaspberry PiのCPU、RAM、ROMの使用状況、CPU温度、IPアドレスが表示されます。

OLEDスクリーンの寿命を延ばすために、デフォルトで60秒後にOLEDがオフになり、電源ボタンを短く押すことで再び点灯します。以下のコマンドでこの機能を有効/無効にすることができます。

* スリープモードに設定: "al"は"常時点灯"を意味します。スリープモードでは、電源ボタンを短く押して起動します。

.. code-block:: shell

    pironman  -al off

* 常時点灯モードに設定:

.. code-block:: shell

    pironman  -al on

* 秒単位での期間を設定:

.. code-block:: shell

    pironman  -s 60

* 上記はOLEDスクリーンの設定内容です。OLEDスクリーンに他の情報や効果を表示させたい場合、 ``/opt/pironman/main.py`` を開いて変更し、実行することができます。

    このPythonスクリプトを開いて内容を変更します。

    .. code-block:: shell

        sudo nano /opt/pironman/main.py

    ``Ctrl+X`` -> ``Y`` -> ``Enter`` を押して、編集を保存して終了します。

    それを実行します。

    .. code-block:: shell

        sudo python3 /opt/pironman/main.py
