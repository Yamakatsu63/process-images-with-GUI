# GUIを用いたガウシアンフィルタリング

gaussian.pyはトラックバーによって与えられた値によってガウシアンフィルタを作成し、キャプチャした画像をフィルタリングする．

## 説明

imageウィンドウにwebカメラから画像をキャプチャし、トラックバーgaussianの値によって15*15の大きさのガウシアンフィルタを作成する．
また、gaussianの値に1/10をかけているため、計算式内でのガウシアンの値は0~10となっている．

## 使い方

python環境でgaussian.pyを実行すると、imageウィンドウにwebカメラでキャプチャしている画像とトラックバーgaussianが表示される．トラックバーgaussianの値を変えると、リアルタイムでガウシアンフィルタが作成され、キャプチャした画像をフィルタリングする．Escキーを押すと終了する．．

## 依存ライブラリ

import cv2 : opencvを利用する

## 実行の様子

![demo](https://github.com/Yamakatsu63/process-images-with-GUI/blob/media/gaussian.gif)

## 引用

https://algorithm.joho.info/programming/python/opencv-gaussian-filter-py/ - ガウシアンフィルタの作成方法
