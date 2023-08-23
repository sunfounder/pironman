機能
======================

**機能**

* Raspberry PiミニPC
* 25°Cの室温で100%のCPU負荷を持つPiを39°Cまで冷却できるタワークーラー
* オンボードのUSBからM.2 SATA SSDへ、TRIM対応
* KodiやVolumioのようなマルチメディアセンターのIRレシーバー
* GPIO制御を持つRGBファン
* 16 WS2812アドレス指定可能なRGB LEDで全体のケースをクールな光の効果で照らす
* 安全なシャットダウン用のインジケータライト付きのレトロな金属製電源ボタン
* Raspberry PiのCPU使用率、温度、ディスク使用率、IPアドレス、RAM使用率などを表示する0.96インチのOLEDディスプレイ
* ピン名ラベル付きの外部GPIOエクステンダーで簡単にアクセス
* 電源ステータスメモリ、偶発的な電源遮断時の電源ステータスを記憶
* 簡単なアクセスのためのmicroSDカードの再配線
* クリアアクリルサイドパネルを持つアルミニウム製の本体

**仕様**

1. 外形寸法: 112.45x68.2x118.92mm
2. 材質
    a. 本体: アルミ合金
    b. 両側面と前面: アクリル
3. 対応プラットフォーム: Raspberry Pi 4B
4. 電源入力: USB Type C 5V/3A
5. 定格電力: 5V/800mA
6. インターフェース (d ~ iはオリジナルのRaspberry Piインターフェース)
    a. Raspberry Pi標準40-Pin GPIO
    b. マイクロSD
    c. USB Type C電源入力
    d. USB 2.0 x 2
    e. USB 3.0
    f. ギガビットLANポート
    g. USB Type C Raspberry Pi電源供給 (Raspberry Piへの直接電源供給、推奨されません)
    h. マイクロHDMI x 2
    i. 3.5mmヘッドフォンジャック
7. 電源ボタン
8. OLEDスクリーン: 0.96インチ 128x64解像度
9. 赤外線受信器: 38KHz
10. 冷却ファン: サイズ 40x40x10mm
11. WS2812 RGB LED: 16xWS2812B-5050

**ピンの機能**

.. image:: img/pin_define.png

* **シャットダウン信号ピン**: 電源ボタンを押すと、Raspberry Piは電源がオフになり、GPIO26が高レベルに設定されます。メインボードがこの高レベルを検出すると、電源が遮断されます。

**寸法図**

.. image:: img/pironman_dimension.png
    :width: 800

