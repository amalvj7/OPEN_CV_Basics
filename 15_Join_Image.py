import cv2
import numpy as np

img  = cv2.imread('Resource/lena.jpg')

img_hor = np.hstack([img,img]) #its an numpy fn also we cant resize or stack different image its it deal with matrix
img_ver = np.vstack([img,img])

cv2.imshow('window_horizonal' , img_hor)
cv2.imshow('window_vertical' , img_ver)
cv2.waitKey(0)