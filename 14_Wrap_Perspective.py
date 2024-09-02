import cv2
import numpy as np

img = cv2.imread('Resource/cards.jpeg')

height , width = 200 , 300
pts_1 =np.float32([[70,59] , [225,32] , [94,137] , [253,106]]) 
pts_2 = np.float32([[0,0] , [0,width] , [height , 0] , [height, width]])

matrix  = cv2.getPerspectiveTransform(pts_1,pts_2)
img_output = cv2.warpPerspective(img , matrix , (width , height))


cv2.imshow('window_2_wrap' , img_output)
cv2.imshow ('wundow_1' , img)
cv2.waitKey(0)