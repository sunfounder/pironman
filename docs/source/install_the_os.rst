.. _install_os:

3. OSのインストール（共通）
========================================

.. note::

    Home Assistanceを使用したい場合は、:ref:`install_hassos` を参照してください。

.. note::

    * あなたのRaspberry Piに以下のPironman互換システムがインストールされている場合、この章をスキップしても構いません。

        .. image:: img/compitable_system.png

**ステップ1**

Raspberry Piは、Mac OS、Ubuntu 18.04、Windowsで動作するグラフィカルなSDカード書き込みツールを開発しています。これはイメージをダウンロードしてSDカードに自動でインストールするため、ほとんどのユーザーにとって最も簡単なオプションです。

ダウンロードページ https://www.raspberrypi.org/software/ を訪問して、ご使用のオペレーティングシステムに合った **Raspberry Pi Imager** のリンクをクリックしてください。ダウンロードが完了したら、インストーラを起動します。

.. image:: img/image11.png
    :align: center

**ステップ2**

インストーラを起動すると、オペレーティングシステムが実行をブロックしようとする場合があります。例えば、Windowsでは次のようなメッセージが表示される場合があります。

これが表示されたら、 **More info** をクリックしてから **Run anyway** をクリックし、Raspberry Pi Imagerのインストール手順に従ってください。

.. image:: img/image12.png
    :align: center

**ステップ3**

SDカードをコンピュータやラップトップのSDカードスロットに挿入します。

**ステップ4**

Raspberry Pi Imagerで、インストールしたいOSとインストール先のSDカードを選択します。

.. image:: img/image13.png
    :align: center

.. note:: 

    * 最初の使用時にはインターネットに接続する必要があります。
    * そのOSは将来のオフライン使用のために保存されます(``lastdownload.cache``, ``C:/Users/yourname/AppData/Local/Raspberry Pi/Imager/cache``)。次回ソフトウェアを開くと、「リリース日：日付、あなたのコンピュータにキャッシュされている」と表示されます。

.. raspios_armhf-2020-05-28のイメージをダウンロードし、Raspberry Pi Imagerで選択します。

**ステップ5**

使用しているSDカードを選択します。

.. image:: img/image14.png
    :align: center

**ステップ6**

**Ctrl+Shift+X** を押すか、 **setting** アイコンをクリックして、 **Advanced options** ページを開き、SSHを有効にし、ユーザ名とパスワードを設定します。

    .. note::
        * Raspberry Piにはデフォルトのパスワードがないため、自分で設定する必要があります。また、ユーザ名も変更可能です。
        * リモートアクセスのためには、SSHを手動で有効にする必要があります。

.. image:: img/image15.png
    :align: center

次に、wifiの設定を完了させて **SAVE** をクリックします。

.. note::

    ``wifi country`` は、Raspberry Piを使用している国の2文字の `ISO/IEC alpha2コード <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements>`_ に設定する必要があります。

.. image:: img/image16.png
    :align: center

**ステップ7**

**WRITE** ボタンをクリックします。

.. image:: img/image17.png
    :align: center

**ステップ8**

現在のSDカードにファイルがある場合、それらのファイルをバックアップすることをおすすめします。バックアップするファイルがない場合は、 **Yes** をクリックします。

.. image:: img/image18.png
    :align: center

**ステップ9**

少し待つと、書き込みが完了したことを示すウィンドウが表示されます。

.. image:: img/image19.png
    :align: center
