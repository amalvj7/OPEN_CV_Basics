import cv2

img  = cv2.imread('Resource/lena.jpg')
img_blur= cv2.GaussianBlur(img , (9,9) , 0) #(7,7) shows the intensity of the blue ,only take the odd and positive value



cv2.imshow('window_1_orginal' , img)
cv2.imshow('window_2_blur' , img_blur)


cv2.waitKey(0)