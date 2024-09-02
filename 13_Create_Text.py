import cv2
import numpy as np

img = np.zeros((512,512 , 3) ,np.uint8 ) # this will create and matrix of 512x512 with 0  :::: zero indicate balck #3 indicate BGR
print(img)

cv2.putText(img ,"TEXT_CHYAN_PADIKUVAA_in_the_image", cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0),3)
cv2.imshow('window_text' , img)