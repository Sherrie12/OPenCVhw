
import cv2
import numpy as np

img = cv2.imread("/Users/wangchunxi/BU/courses/EC601/OpenCV_homework/Test_images/coins.png")
pixel_RGB = img[20,25]
print("RGB: ",pixel_RGB)

ycbcr_image = cv2.cv2.cvtColor(img,cv2.COLOR_BGR2YCrCb)
pixel_ycbcr = ycbcr_image[20,25]
print("YCbCr:",pixel_ycbcr)

hsv_image = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
pixel_hsv = hsv_image[20,25]
print("HSV: ",pixel_hsv)