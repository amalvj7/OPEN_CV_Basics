import cv2
import numpy as np

img = np.zeros((512,512 , 3) ,np.uint8 ) # this will create and matrix of 512x512 with 0  :::: zero indicate balck #3 indicate BGR
print(img)

cv2.line(img , (0,0) , (200,300) , (0,255,0) , 3) #(image_name , (start_point), (end_point) ,(color) , thickness)
cv2.rectangle(img , (200,200) , (300,100) , (255,0,0) , cv2.FILLED)
cv2.circle(img , (400,400) , 50 , (255,0,0) ,5)
cv2.imshow('window_1_black' , img)
cv2.waitKey(0)