.. _ssd:

SATA M.2 SSD
=====================================

NVME M.2 SSDとの非互換性の理由
--------------------------------------

.. note::
    M.2 SSDのハードドライブインターフェースはSATAプロトコルのみをサポートし、NVME/PCIeはサポートしていません。

現在のインターフェースはSATA M.2 SSDに適応する設計となっています。ここで、NVMe M.2 SSDとの互換性を持たせない決定の背景を説明いたします：

NVMe SSDは高性能コンピューティング環境での性能が非常に高い一方、Raspberry Pi 4の処理能力やバス帯域幅は限定されています。したがって、NVMe SSDを接続しても、ハードウェアの制約から、SSDのパフォーマンスを最大限に活用できない場合があり、リソースの最適な利用が難しいと考えられます。

さらに、Raspberry Pi 4のUSB電源供給には制約があります。NVMe SSDを接続すると、特に高負荷時には電源が不足する可能性があります。NVMe SSDは安定した動作のために高い電流を要求することが多いですが、Raspberry Pi 4のUSBポートがこれらの要求を満たせない場合、SSDの動作が不安定になったり、適切に機能しない恐れがあります。

以上の理由から、NVMe SSDを接続することで、大きな性能向上は期待できないと判断しました。このため、NVMe SSDインターフェースのサポートを見送っています。

設計に対するご理解をお願い申し上げます。お客様に最適な製品を提供し、スムーズな体験を実現することが私たちの目標です。

モデルに関して
---------------------------

M.2 SSDは、その仕様や性能特性によりさまざまなモデルが存在します。以下は、一般的なM.2 SSDのモデルを示しています：

* **M.2 SATA SSD**: これらは、2.5インチSATA SSDと同様のSATAインターフェイスを使用しますが、より小さなM.2フォームファクターで提供されます。SATA IIIの最大速度約600MB/sによって速度が制限されています。これらのSSDは、BキーとMキーの両方に対応したM.2スロットと互換性があります。
* **M.2 NVMe SSD**: これらのSSDは、PCIeレーンを介してNVMeプロトコルを使用し、M.2 SATA SSDよりも著しく速い速度を提供します。ゲーム、ビデオ編集、データ集約的なタスクなど、高速な読み書き速度が求められるアプリケーションに適しています。これらのSSDは、通常Mキーのスロットを要求します。これらのドライブはPCIe（Peripheral Component Interconnect Express）インターフェイスを利用しており、3.0、4.0、5.0などの異なるバージョンがあります。PCIeの新しいバージョンは、前任者のデータ転送速度を実質的に倍増させます。

M.2 SSDはBキー、Mキー、B+Mキーの3つの主要なタイプがあります。しかし、B+Mキーが後に導入され、BキーとMキーの機能を統合。結果として独立したBキーは廃止されました。下の画像を参照してください。

.. image:: img/ssd_key.png

一般的に、M.2 SATA SSDはB+Mキーであり、PCIe 3.0 x4レーンのM.2 NVMe SSDはMキーです。

.. image:: img/ssd_model2.png

長さについて
-----------------------

M.2モジュールはさまざまなサイズがあり、Wi-Fi、WWAN、Bluetooth、GPS、NFCなどにも使用されます。

Pironmanは、その名称から以下の4つのM.2 SATA SSDサイズをサポートしています：2230、2242、2260、および2280。「22」はミリメートル単位の幅を示し、次の2つの数字は長さを示します。ドライブの長さが長いほど、多くのNANDフラッシュチップを取り付けることができ、それにより容量が増えます。

.. image:: img/m2_ssd_size.png
    :width: 600

SSDの組み立て方法
------------------------------

#. Pironmanのベースプレートを取り外します。

    .. image:: img/ssd1.jpg
        :width: 600

#. M.2 SATA SSDのためのネジを外します。

    .. image:: img/ssd2.jpg

#. お持ちのM.2 SATA SSDを挿入します。

    .. image:: img/ssd3.jpg

#. 適切な位置にネジを固定します。

    .. image:: img/ssd4.jpg

#. ベースプレートを元に戻します。

    .. image:: img/ssd5.jpg

#. SSDブリッジと5V/3Vの電源供給を接続します。

    .. image:: img/ssd18.jpg


**SSDからの起動**
---------------------------
Raspberry PiにSSDをインストールしたので、Raspberry Pi OSをその上にインストールし、SSDからRaspberry Piを起動する方法を学びましょう。

**1. Raspberry Pi OSをSSDにインストール**

SSDにRaspberry Pi OSをインストールする方法は2つあります：

* 最初の方法は、 **Raspberry Pi Imager** を使用して直接インストールする方法です。これはMicro SDカードにOSをインストールするのと似ています。ストレージデバイスを選ぶよう求められたら、SSDを選択してください。この手順に不慣れな場合は、チュートリアル  :ref:`install_os`  を参照してください。

* 代替の方法は、既存のSDカードからコピーする方法です。SDカード上のファイルやシステムを保持したい場合は、この方法が適しています。

Micro SDの内容をSSDにコピーする方法を以下に説明します：

#. Pironmanにmicro SDカードを挿入し、USB Bridgeを使ってSSDをRaspberry Piに接続し、Pironmanの電源を入れます。

    .. image:: img/ssd18.jpg

#. Raspberry Piのデスクトップにアクセスします。これは、モニターを直接接続するか、リモートデスクトップを使用して行うことができます。詳細はチュートリアル :ref:`no_screen` を参照してください。

#. **start** メニューの **Accessoriesー** セクションから **SD Card Copier** を起動します。

    .. image:: img/sd_card_copy.png

#. コピー元デバイス（Micro SDカード）とコピー先デバイス（SSD、``/dev/sda/``）を選択します。正しいドライブを選択したことを確認し、 **"Start"** をクリックしてコピープロセスを開始します。これには数分かかることがあります。

    .. image:: img/sd_card_copy_select.png

#. **"Copy Complete"** と表示されたら、Raspberry Piをシャットダウンし、micro SDカードを取り外します。

.. note::

    Micro SDカードが **Raspberry Pi Lite** の場合、コピーを完了するためにコマンドを使用する必要があります。詳しい手順については、 :ref:`copy_lite` を参照してください。

**2. ブートローダーのインストール**

Raspberry Pi OSがSSDにインストールされたので、次はPiのブートローダーをリセットしてUSBからの起動を優先する必要があります。

#. Raspberry Piのウェブサイトから |link_raspberry_pi_imager| をダウンロードしてインストールします。

#. 余分なmicro SDカードをコンピュータに挿入します。このカードの内容は削除されるため、重要なデータのバックアップを忘れずに。

#. **Raspberry Pi Imager** を起動し、 **“Operating System”** の下にスクロールして **“Misc Utility Images”** をクリックします。

    .. image:: img/ssd6.png

#. **Bootloader** を選択します。

    .. image:: img/ssd7.png

#. 次に、 **USB Boot** を選択します。これでメインメニューに戻ります。

    .. image:: img/ssd8.png

#. **"Storage"** の下で、micro SDカードを選択します。進む前に、正しいドライブを選択したことを再確認してください。

    .. image:: img/ssd88.png

#. **“WRITE”** をクリックして、設定イメージをダウンロードし、それをmicro SDカードに書き込みます。

    .. image:: img/ssd9.png

#. 書き込みが成功したことを確認してから、micro SDカードをコンピュータから取り外します。

#. Pironmanにmicro SDカードを挿入し、電源を入れます。

    .. image:: img/connect_power.jpg

#. アップデートが完了すると、緑色のアクティビティLEDが定期的に点滅します。HDMIモニターが接続されている場合、完了時に画面が緑色になります。アップデートには10秒以上かかることがあるため、このプロセス中にmicro SDカードを取り外さないようにしてください。

    .. image:: img/ssd10.jpg

#. Raspberry Piの電源を切り、micro SDカードを取り外します。

**3. SSDからの起動**

#. この時点で、micro SDカードが取り外されていることを確認してください。USB Bridgeを使用してSSDをRaspberry Piに接続します。次に、Pironmanの電源を入れます。

    .. image:: img/login1.png


