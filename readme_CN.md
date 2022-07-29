# 给照片添加富士水印

## 打包小贴士
opencv的最新版本pyinstaller并不能成功打包，记得使用旧版，发布使用的版本是4.5.1.48。

## 打包
pyinstaller -F -i watermark.ico -w --hidden-import opencv-python add_water_mark.py --add-data "fuji.jpeg;."

## Usage
把文件拖到exe上面就可以辣。
如果是py文件不想编译的话:`python add_water_mark.py path_to_photo`

## example

![example](example.jpg)
