Pironman V2.0- SunFounder向けのRaspberry PiミニPCキット
=================================================================

SunFounder Pironman V2.0をお選びいただき、ありがとうございます。

.. note::
    このドキュメントは以下の言語で利用可能です。

        * |link_german_tutorials|
        * |link_jp_tutorials|
        * |link_en_tutorials|

    ご希望の言語でドキュメントにアクセスするために、それぞれのリンクをクリックしてください。

.. note::

    Pironmanには2つのバージョンがあります。各バージョンのオンラインチュートリアルのスクリプトは互換性がありませんので、注意してください。
    
    適切なセットアップを確保するため、取扱説明書に記載されているショートリンクを使用してバージョンを特定してください：

    * リンクが"pironman-v2.rtfd.io"の場合、このチュートリアルを続行してください。
    * リンクが"pironman.rtfd.io"と表示される場合は、|link_pironman_v1| のチュートリアルに従ってください。

    .. image:: img/about_version.jpg
        :width: 500
        :align: center


    .. image:: img/pironman.png
        :width: 400
        :align: center

PironmanはSunFounderのカスタマイズされたRaspberry Pi用ミニPCです。スクリーン、マウス、キーボードを接続するだけで、プロジェクト、エンターテインメント、オフィス用として使用することができます。

* サイズは4.43'' x 2.69'' x 4.68''
* Raspberry PiミニPC
* タワー型クーラーは、室温25°Cで100% CPU負荷のPiを39°Cに冷やすことができます
* 0.96" OLEDディスプレイには、Raspberry PiのCPU使用率、温度、ディスク使用率、IPアドレス、RAM使用率などが表示されます
* オンボードUSBからM.2 SATA SSDへ、TRIM対応
* GPIO制御付きのRGBファン
* 16個のWS2812アドレス指定可能なRGB LED
* KodiやVolumioのようなマルチメディアセンター用のIRレシーバ
* ピン名ラベル付きの外部GPIOエクステンダ
* 電源ステータスメモリ、電源ステータスを記憶し、電源が突然切れた場合に自動的に起動します
* クリアなアクリルサイドパネル付きのアルミニウム本体


.. note::
    以下のリンクから、WS2812 RGBストリップおよびM.2 SATA SSDの設定を見ることができます。

    * :ref:`rgb_strip`
    * :ref:`ssd`

.. note::

    以下にPironmanと互換性のあるシステムを示します。他のシステムをインストールしている場合、Pironmanの一部のコンポーネントが利用できない可能性があります。

    .. image:: img/compitable_system_hm.png

何か質問があれば、service@sunfounder.com までメールしてください。できるだけ早く対応させていただきます。

**表示言語について**

この文書は他の言語でも利用可能です。表示言語を切り替えるには、ページの左下にある **Read the Docs** アイコンをクリックしてください。

.. image:: img/translation.png
       :align: center

.. raw:: html

   <br/>


**About the display language**

This document is available in other languages as well. To switch the display language, kindly click on the **Read the Docs** icon located in the lower left corner of the page.

.. image:: img/translation.png
       :align: center

.. raw:: html

   <br/>

.. toctree::
    :maxdepth: 2

    このキットについて <self>
    what_do_we_need    
    list_and_assembly
    install_the_os
    set_up_your_raspberry_pi
    setup_pironman
    about_hardware
    appendix/appendix
    home_assistant    
    faq
