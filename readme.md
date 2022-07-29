# Add FUJIFILM watermark to your photograph

[中文文档](readme_CN.md)

## Build tips
1. in order to make binary by pyinstaller, you may need a lower version opencv. This project are using opencv-python==4.5.1.48
2. you can use the ico you like.
3. you can also choose the watermark like Zeiss, Leica

## Build
pyinstaller -F -i watermark.ico -w --hidden-import opencv-python add_water_mark.py --add-data "fuji.jpeg;."

## Usage
draw your photo to the exe file.

## example

![example](example.jpg)
