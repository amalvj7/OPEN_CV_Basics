import cv2

img = cv2.imread('Resource/rgb_model.webp')
B , G , R = cv2.split(img) #this function split the image based on the red, blue and green


cv2.imshow('window_orginal' , img)

cv2.imshow('window_Blue' , B)
cv2.imshow('window_Green' , G)
cv2.imshow('window_Red' , R)

cv2.waitKey(0)