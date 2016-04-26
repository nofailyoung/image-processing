# coding: utf-8

from PIL import Image, ImageFilter
import cv2
import numpy as np

print '##### PIL #####'
img = Image.open('images/image.jpg')
# img.show()

#过滤图像
im_sharp = img.filter( ImageFilter.SHARPEN )
#保存过滤过的图像到文件中
im_sharp.save( 'images/image_sharpened.jpg', 'JPEG' )

#分解图像到三个RGB不同的通道（band）中。
r,g,b = img.split()
r.save( 'images/image_r.jpg', 'JPEG' )
g.save( 'images/image_g.jpg', 'JPEG' )
b.save( 'images/image_b.jpg', 'JPEG' )

#显示被插入到图像中的EXIF标记
exif_data = img._getexif()
print 'EXIF:', exif_data




print '##### CV2 #####'
#读取图像
img = cv2.imread('images/image.jpg')
#显示图像
cv2.imshow('images/image.jpg',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Applying Grayscale filter to image 作用Grayscale（灰度）过滤器到图像上
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#保存过滤过的图像到新文件中
cv2.imwrite('images/graytest.jpg',gray)