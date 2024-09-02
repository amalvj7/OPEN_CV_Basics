import cv2
import numpy as np

img_1 = np.zeros((512,512 , 3) ) # this will create and matrix of 512x512 with 0  :::: zero indicate balck #3 indicate BGR
print(img_1.shape)

img_1[200:300, 0:200] = 0,0,255

cv2.imshow('window_1_black' , img_1)
cv2.waitKey(0)