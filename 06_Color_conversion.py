import cv2

img  = cv2.imread('Resource/lena.jpg')

img_grey = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
img_RGB  = cv2.cvtColor(img , cv2.COLOR_BGR2RGB)
img_HSV = cv2.cvtColor(img , cv2.COLOR_BGR2HSV)

cv2.imshow('window_1_orginal' , img)
cv2.imshow('window_2_grey' , img_grey)
cv2.imshow('window_3_RGB ' , img_RGB )
cv2.imshow('window_3_HSV ' , img_HSV)


cv2.waitKey(0)