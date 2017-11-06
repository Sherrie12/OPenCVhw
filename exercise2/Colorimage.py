import cv2
import numpy as np

img = cv2.imread("/Users/wangchunxi/BU/courses/EC601/OpenCV_homework/Test_images/coins.png")
#cv2.namedWindow("Image")
cv2.imwrite("/Users/wangchunxi/BU/courses/EC601/OpenCV_homework/hw/coins/Original.png", img)

#RGB
b,g,r = cv2.split(img)
cv2.imwrite("/Users/wangchunxi/BU/courses/EC601/OpenCV_homework/hw/coins/Blue.png",b)
cv2.imwrite("/Users/wangchunxi/BU/courses/EC601/OpenCV_homework/hw/coins/Green.png",g)
cv2.imwrite("/Users/wangchunxi/BU/courses/EC601/OpenCV_homework/hw/coins/Red.png",r)

#ycbcr
ycbcr_image = cv2.cv2.cvtColor(img,cv2.COLOR_BGR2YCrCb)
y,cb,cr = cv2.split(ycbcr_image)
cv2.imwrite("/Users/wangchunxi/BU/courses/EC601/OpenCV_homework/hw/coins/y.png",y)
cv2.imwrite("/Users/wangchunxi/BU/courses/EC601/OpenCV_homework/hw/coins/cb.png",cb)
cv2.imwrite("/Users/wangchunxi/BU/courses/EC601/OpenCV_homework/hw/coins/cr.png",cr)

#hsv
hsv_image = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
h,s,v = cv2.split(hsv_image)
cv2.imwrite("/Users/wangchunxi/BU/courses/EC601/OpenCV_homework/hw/coins/Hue.png",h)
cv2.imwrite("/Users/wangchunxi/BU/courses/EC601/OpenCV_homework/hw/coins/Saturation.png",s)
cv2.imwrite("/Users/wangchunxi/BU/courses/EC601/OpenCV_homework/hw/coins/Value.png",v)

#cv2.waitKey(0)
#cv2.distroyAllWindows()
