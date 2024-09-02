import cv2

#reading the image 
img_color  = cv2.imread('Resource/lena.jpg' , 1) # 1--> color ,
img_grey  = cv2.imread('Resource/lena.jpg' , 0) # 0 --> greay
img_unchanged = cv2.imread('Resource/lena.jpg' , -1) # -1--> gives the unchanged image

# writig the image
copied_image_lena  = cv2.imwrite( 'copied_image_lena.png' ,img_color )
copied_image = cv2.imread('copied_image_lena.png')

#showing the image
cv2.imshow('lena_window_1' , img_color)
cv2.imshow('lena_window_2' , img_grey)  
cv2.imshow('lena_window_3' , img_unchanged)
cv2.imshow('lena_window_4' , copied_image)  

cv2.waitKey(5000)  # window will wait for the 5000 milli second
cv2.destroyAllWindows() #close all OPENCV windows