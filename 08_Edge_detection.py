import cv2
import numpy as np

img = cv2.imread('Resource/lena.jpg')
img_gray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
img_blur  = cv2.GaussianBlur(img_gray , (7,7) , 0)


kernal  = np.ones((5,5) , np.uint8)
img_canny = cv2.Canny(img_blur ,100 ,100 )  #detect the edge
img_dilation = cv2.dilate(img_canny , kernal , iterations = 1)  #increase the thickness of the edge
img_eroded  = cv2.erode(img_dilation, kernal , iterations= 1)


cv2.imshow('window_canny ' , img_canny)
cv2.imshow('window_dilated'  , img_dilation)
cv2.imshow('window_eroded'  , img_eroded)
cv2.waitKey(0) 