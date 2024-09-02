#Cropping didnot want open_cv fn , image can be treated as array 

import cv2

img = cv2.imread('Resource/lena.jpg')

img_crop = img[0:200 ,200:400]


cv2.imshow('window_1_img' , img)
cv2.imshow('window_2_croped' , img_crop)
cv2.waitKey(0)