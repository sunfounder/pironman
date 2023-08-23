FAQ
============

PironmanのLEDは点灯しているが、電源ボタンを押してもRaspberry Piが起動しないのは？
-------------------------------------------------------------------------------------------

以下の条件を確認してください。

#. Raspberry Pi用の別の電源はありますか？

    以下の理由でこれを行わないでください。

    Raspberry Pi自体にはオン/オフ制御がないため、Raspberry Piの電源を入れることでのみ起動します。
    したがって、Pironmanは電源オフ後にRaspberry Piの電源を切り、Raspberry Piの電源を入れてRaspberry Piを起動します。
    Raspberry PiとPironmanの両方の電源を入れると、シャットダウン後、Raspberry Piは外部からプラグを挿入されて常に電源が供給されているため、PironmanはRaspberry Piの電源を入れてRaspberry Piを起動する方法がありません。

#. Micro SDカードは既にPironmanのスロットに挿入されていますか？
#. Micro SDカードにシステムはインストールされていますか？
#. GPIOブリッジのFFCケーブルが正しく接続されているか、特に注意が必要ですか？

    .. image:: img/gpio_bridge1.gif
    .. image:: img/gpio_bridge2.gif

.. _copy_lite:

Micro SDからSSDにRaspberry Pi OS Liteをコピーする方法は？
----------------------------------------------------------

#. ブートローダを更新する


    .. code-block:: shell

        sudo apt update
        sudo apt full-upgrade
        sudo rpi-update
        sudo rpi-eeprom-update -d -a

    設定後、効果を適用するために再起動します。

#. 以下のコマンドを使用して、ストレージデバイスの名前を表示します。

    .. code-block:: shell

        sudo fdisk -l

#. Raspberry Piに接続されているすべてのドライブのリストが表示されます。ほとんどの場合、 ``/dev/mmcxxx`` はMicro SDカードを指し、 ``/dev/sda/`` はSSDを指します。

    .. image:: img/ssd16.png

#. 次に、以下のコマンドを使用して、Micro SDカードからSATA M.2 SSDにシステムをクローンします。

    .. note::
        Micro SDカードの名前を ``/dev/mmcblk0`` に置き換え、SSDの名前が異なる場合は ``/dev/sda`` も変更してください。

    .. code-block:: shell

        sudo dd if=/dev/mmcblk0 of=/dev/sda bs=4M

#. Micro SDカードを取り外し、M.2 SATA SSDを接続して、Pironmanの電源を入れます。
