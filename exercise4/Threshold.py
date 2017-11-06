
import cv2
import numpy as np

src = cv2.imread("/Users/wangchunxi/BU/courses/EC601/OpenCV_homework/Test_images/baboon.jpg")
gray = cv2.cvtColor(src,cv2.COLOR_RGB2GRAY) # convert to gray
# Thresholded 
# 0: Binary,      1: Binary Inverted,      2: Threshold Truncated,      3: Threshold to Zero,      4: Threshold to Zero Inverted    */
threshold_type = 2   #slider 1 [0, 4]
threshold_value = 128  #slider 2 [0 255]
T, Thresholded = cv2.threshold(gray, threshold_value, 255, threshold_type )
cv2.imwrite("/Users/wangchunxi/BU/courses/EC601/OpenCV_homework/hw/baboon/Thresholded.png", Thresholded)


current_threshold = 128
max_threshold = 255
# Binary Threshold
T, BinaryThreshold = cv2.threshold(gray, current_threshold, max_threshold, cv2.THRESH_BINARY);
cv2.imwrite("/Users/wangchunxi/BU/courses/EC601/OpenCV_homework/hw/baboon/Binary_threshold.png", BinaryThreshold)

# Band Threshold
threshold1 = 27
threshold2 = 125
T, lower = cv2.threshold(gray, threshold1, max_threshold,cv2.THRESH_BINARY)
T, upper = cv2.threshold(gray, threshold2, max_threshold,cv2.THRESH_BINARY_INV)
BandThresholding = cv2.bitwise_and(lower,upper)
cv2.imwrite("/Users/wangchunxi/BU/courses/EC601/OpenCV_homework/hw/baboon/Band_thresholding.png",BandThresholding)


# Semi Thresholding
T,thres = cv2.threshold(gray,current_threshold, max_threshold, cv2.THRESH_BINARY_INV or cv2.THRESH_OTSU);
SemiThresholding = cv2.bitwise_and(gray,thres);
cv2.imwrite("/Users/wangchunxi/BU/courses/EC601/OpenCV_homework/hw/baboon/Semi_thresholding.png",SemiThresholding)

# Adaptive thresholding
AdaptiveThreshold = cv2.adaptiveThreshold(gray, max_threshold, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 101, 10 );
cv2.imwrite("/Users/wangchunxi/BU/courses/EC601/OpenCV_homework/hw/baboon/Adaptive_Threshold.png",AdaptiveThreshold)


