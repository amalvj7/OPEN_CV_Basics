import cv2

img = cv2.imread('Resource/lena.jpg')
cv2.imshow('window_1' , img)

k = cv2.waitKey(0) # 0 mean infinity wait for the windows


if k == 27:  # 27 --> esc
    cv2.destroyAllWindows()
elif k == ord('s'): # ord is an function to read the keyboard , here we press s
    cv2.imwrite('lena_copied_waitkey.jpg' , img)
    cv2.destroyAllWindows()

    
