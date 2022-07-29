import cv2
import numpy
import sys

img_path = sys.argv[1]
from os import path

bundle_dir = getattr(sys, '_MEIPASS', path.abspath(path.dirname(__file__)))
global fuji_path
fuji_path = path.join(bundle_dir, 'fuji.jpeg')

img = cv2.imread(img_path)
fuji = cv2.imread(fuji_path)
shape_origin = img.shape
add_merge = int(min(shape_origin[0], shape_origin[1]) * 0.3)
shape = (shape_origin[0] + add_merge, shape_origin[1] + add_merge)
img_bg = numpy.ones(shape, dtype=numpy.uint8)
img_bg *= 255
img_bg = cv2.cvtColor(img_bg, cv2.COLOR_GRAY2BGR)
rate = add_merge * 0.4 / fuji.shape[0]
fuji = cv2.resize(fuji, None, fx=rate, fy=rate)
img_bg[int(add_merge / 2):int(shape_origin[0] + add_merge / 2),
int(add_merge / 2):int(shape_origin[1] + add_merge / 2), :] = img

fuji_shape = fuji.shape
yy_origin = int(add_merge * 0.75 + shape_origin[0] - fuji_shape[0] / 2)
x_origin = int((shape[1] - fuji_shape[1]) / 2)

img_bg[yy_origin:yy_origin + fuji_shape[0], x_origin:x_origin + fuji_shape[1]] = fuji
name = sys.argv[1]
name = name[:name.find('.')]
name = name + "_fuji_power!.jpg"
cv2.imwrite(name, img_bg, [int(cv2.IMWRITE_JPEG_QUALITY), 75])
print('ok')
