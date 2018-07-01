# GUIを用いたガンマ変換

gamma.pyは、トラックバーにより与えられた値によってキャプチャした画像のガンマ変換を行う．

## 説明

imageウィンドウにwebカメラから画像をキャプチャし、トラックバーgammaの値でガンマ変換を行う．ガンマ変換を計算式では、gammaの値が0のときゼロ除算が行われてしまうため、0.01を足している．また．それを100で割っているため、計算式内では、ガンマ値の範囲は0.01~1.01となっている．plot_curve()関数でトーンカーブの表示を行っている．

## 使い方

python環境でgamma.pyを実行すると、imageウィンドウにwebカメラでキャプチャしている画像とトラックバーgammaが表示される．トラックバーgammaの値を変えると、リアルタイムでキャプチャした画像がガンマ変換される．

## 依存ライブラリ

import numpy as np : 行列処理を行う
import cv2 : opencvを利用する
from matplotlib import pyplot as plt : グラフをプロットする
import matplotlib.gridspec as gridspec : グラフにグリッドを表示する

***実行の様子:***

![DEMO](https://github.com/Yamakatsu63/process-images-with-GUI/blob/media/gamma.gif)

## 引用

http://optie.hatenablog.com/entry/2018/03/03/141427
-トーンカーブの描き方

https://algorithm.joho.info/programming/python/opencv-gamma-correction-py/
-ガンマ変換の計算式
