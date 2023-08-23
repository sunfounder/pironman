.. _remote_desktop:


リモートデスクトップ
=====================

Raspberry Piのデスクトップをリモートで操作する方法は2つあります。

それは、 **VNC** と **XRDP** のいずれかを使用することができます。

VNC
--------------

VNCを通じてリモートデスクトップの機能を利用することができます。

**VNCサービスの有効化**

VNCサービスはシステムにインストールされています。デフォルトでは、VNCは
無効になっています。それをconfigで有効にする必要があります。

**ステップ1**

以下のコマンドを入力します：

.. code-block:: shell 

    sudo raspi-config

.. image:: img/image287.png
   :align: center

**ステップ2**

キーボードの下矢印キーを押して、 **3** **インターフェースオプション** を選び、 **Enter** キーを押します。

.. image:: img/image282.png
   :align: center

**ステップ3**

**P3 VNC**

.. image:: img/image288.png
   :align: center

**ステップ4**

**はい -> OK -> 完了** を選び、設定を終了します。

.. image:: img/image289.png
   :align: center

**VNCへのログイン**

**ステップ1**

パーソナルコンピュータに`VNC Viewer <https://www.realvnc.com/en/connect/download/viewer/>`_ をダウンロードし、インストールします。インストールが完了したら、それを開きます。

**ステップ2**

「**新しい接続**」を選択します。

.. image:: img/image290.png
   :align: center

**ステップ3**

Raspberry PiのIPアドレスと任意の**名前**を入力します。

.. image:: img/image291.png
   :align: center

**ステップ4**

作成した**接続**をダブルクリックします：

.. image:: img/image292.png
   :align: center

**ステップ5**

ユーザー名（デフォルトで**pi**）とパスワード（デフォルトで**raspberry**）を入力します。

.. image:: img/image293.png
   :align: center

**ステップ6**

これで、Raspberry Piのデスクトップが表示されます：

.. image:: img/image294.png
   :align: center

VNCの部分はこれで終了です。

XRDP
-----------------------

リモートデスクトップの別の方法として、XRDPがあります。これはRDP（Microsoft Remote Desktop Protocol）を使用してリモートマシンへのグラフィカルなログインを提供します。

**XRDPのインストール**

**ステップ1**

SSHを使用してRaspberry Piにログインします。

**ステップ2**

XRDPをインストールするための以下の指示を入力します。

.. code-block:: shell 

   sudo apt-get update
   sudo apt-get install xrdp

**ステップ3**

その後、インストールが開始されます。

「Y」と入力し、「Enter」キーを押して確認します。

.. image:: img/image295.png
   :align: center

**ステップ4**

インストールが完了したら、Windowsのリモートデスクトップアプリケーションを使用してRaspberry Piにログインする必要があります。

**XRDPへのログイン**

**ステップ1**

Windowsユーザーの場合、Windowsに付属しているリモートデスクトップ機能を使用できます。Macユーザーの場合は、APP StoreからMicrosoft Remote Desktopをダウンロードして使用することができます。両方とも大きな違いはありません。次の例はWindowsのリモートデスクトップです。

**ステップ2**

「**mstsc**」をRun (WIN+R)で入力して、リモートデスクトップ接続を開き、Raspberry PiのIPアドレスを入力して、「接続」をクリックします。

.. image:: img/image296.png
   :align: center

**ステップ3**

次に、xrdpのログインページが表示されます。ユーザー名と
パスワードを入力してください。それを入力した後、「OK」をクリックします。初めてログインするとき、ユーザー名は「pi」で、パスワードは「raspberry」です。

.. image:: img/image297.png
   :align: center

**ステップ4**

ここで、リモートデスクトップを使用してRPiに成功裏にログインしました。

.. image:: img/image20.png
   :align: center




