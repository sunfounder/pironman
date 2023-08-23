Linux /Unix ユーザー
==========================

#. **Applications** ->\ **Utilities** を開き、 **Terminal** を探して開いてください。

    .. image:: img/image21.png
        :align: center

#. あなたのRaspberry Piが同じネットワーク上にあるかどうかを確認するには、 ``ping <hostname>.local`` を入力します。

    .. code-block:: shell

        ping raspberrypi.local

    .. image:: img/mac-ping.png
        :width: 550
        :align: center

    * ターミナルで ``ping: cannot resolve <hostname>.local`` というプロンプトが表示された場合、Raspberry Piがネットワークに接続できていない可能性があります。ネットワークを確認してください。
    * もし ``<hostname>.local`` にpingができない場合、代わりに :ref:`get_ip` を参照して ``ping <IP address>`` を試してみてください。（例: ``ping 192.168.6.116``）
    * ``64 bytes from <IP address>: icmp_seq=0 ttl=64 time=0.464 ms`` のようなプロンプトが複数表示される場合、あなたのコンピュータはRaspberry Piにアクセスできることを意味します。

#. ``ssh <username>@<hostname>.local`` （または ``ssh <username>@<IP address>`` ）を入力します。

    .. code-block:: shell

        ssh pi@raspberrypi.local

#. 以下のメッセージが表示されることがあります。

    .. code-block::

        'raspberrypi.local (192.168.6.116)' の真正性は確立できません。
        ECDSAキーのフィンガープリントはSHA256:7ggckKZ2EEgS76a557cddfxFNDOBBuzcJsgaqA/igz4です。
        接続を続行しますか？ (yes/no/[fingerprint])?

    \"yes\" と入力してください。

    .. image:: img/mac-ssh-login.png
        :width: 550
        :align: center

#. 以前設定したパスワードを入力してください。（私の場合は ``raspberry`` です。）

#. Raspberry Piに接続が完了し、次のステップに進む準備ができました。

    .. image:: img/mac-ssh-terminal.png
        :width: 550
        :align: center

