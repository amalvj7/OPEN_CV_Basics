import cv2

img = cv2.imread('Resource/lena.jpg')
print(img.shape) #the shape function will give the heigth , width , BGR_number


img_resize  = cv2.resize(img ,(200,300)) # open cv take width first and height ie width = 200 , heigth = 300
print(img_resize.shape)



cv2.imshow('window_1_img' , img)
cv2.imshow('window_2_resizeimg' , img_resize)
cv2.waitKey(0)