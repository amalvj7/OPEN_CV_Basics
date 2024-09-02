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



def Contour(image):
    contour , heirarchy =cv2.findContours(image , cv2.RETR_EXTERNAL , cv2.CHAIN_APPROX_NONE)
    for cnt in contour:
        area = cv2.contourArea(cnt)
        if area > 100:
            cv2.drawContours(img_Contour , cnt , -1 ,(255,0,0) , 3) 
            perimeter  = cv2.arcLength(cnt ,True) #True mean its an closed shape
            corner_points = cv2.approxPolyDP(cnt , 0.02*perimeter , True)  #give all the corner points in an list containg tuples
            no_of_sides = len(corner_points)

            x , y , width , height  = cv2.boundingRect(corner_points)
            if no_of_sides == 3:
                object_type  = "Traingle"
            elif no_of_sides == 4:
                side_ratio = width/float(height)
                if side_ratio >= .95 and side_ratio <=1.05:
                    object_type = "Square"
                else:
                    object_type = "Reactangle"
            else:
                 object_type = "circle"
            

            cv2.rectangle(img_Contour ,(x,y) , (x + width , y + height) ,(0,255,0) , 3)
            cv2.putText(img_Contour , object_type ,( int(x + width/2 ),int( y + height/2)) ,cv2.FONT_HERSHEY_COMPLEX , 0.7 , (0,0,0) , 2 )



img = cv2.imread('Resource/shapes.png')

img_gray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
img_blur  = cv2.GaussianBlur(img_gray , (7,7) ,0)
img_canny = cv2.Canny(img_blur , 100, 100)
img_Contour  = img.copy()
img_black = np.zeros_like(img)

Contour(img_canny)
img_stack = stackImages(0.6 , ([img , img_gray , img_blur] , [img_canny , img_Contour ,img_black]))

cv2.imshow('window_stack' , img_stack)
cv2.waitKey(0)

