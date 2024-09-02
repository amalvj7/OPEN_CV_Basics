import cv2
import numpy as np

def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver


def empty(self):
    pass







cv2.namedWindow('TRACKBAR_window')
cv2.resizeWindow('TRACKBAR_window' ,640,240)
cv2.createTrackbar('Hue_Min' , 'TRACKBAR_window' , 0 ,179 , empty)
cv2.createTrackbar('Hue_Max' , 'TRACKBAR_window' , 166 ,179 , empty)
cv2.createTrackbar('Sat_Min' , 'TRACKBAR_window' , 33 ,179 , empty)
cv2.createTrackbar('Sat_Max' , 'TRACKBAR_window' , 179 ,179 , empty)
cv2.createTrackbar('Val_Min' , 'TRACKBAR_window' , 0 ,179 , empty)
cv2.createTrackbar('Val_Max' , 'TRACKBAR_window' , 157 ,179 , empty)



while True:
    img = cv2.imread('Resource/lamoo.jpeg')
    img_HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    h_min = cv2.getTrackbarPos('Hue_Min' , 'TRACKBAR_window' )
    h_max = cv2.getTrackbarPos('Hue_Max' , 'TRACKBAR_window' )
    s_min = cv2.getTrackbarPos('Sat_Min' , 'TRACKBAR_window' )
    s_max = cv2.getTrackbarPos('Sat_Max' , 'TRACKBAR_window' )
    v_min = cv2.getTrackbarPos('Val_Min' , 'TRACKBAR_window' )
    v_max = cv2.getTrackbarPos('Val_Max' , 'TRACKBAR_window' )
    print(h_min,h_max,s_min,s_min ,v_min, v_max)

    lower =np.array([h_min,s_min,v_min])
    higher = np.array([h_max,s_max , v_max])
    img_mask = cv2.inRange(img_HSV,lower , higher)
    img_output = cv2.bitwise_and(img , img , mask = img_mask)

    #cv2.imshow('window_orginal' , img)
    #cv2.imshow('window_HSV' , img_HSV)
    #cv2.imshow('window_masked' , img_mask)
    #cv2.imshow('window_output' , img_output)

    img_stacked  = stackImages(0.6 , ([img,img_HSV] ,[img_mask ,img_output] ))
    cv2.imshow('window_stacked' , img_stacked)
    cv2.waitKey(1)
    