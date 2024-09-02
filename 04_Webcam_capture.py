import cv2

clip = cv2.VideoCapture(0) # instead of the video name , we gave the 0 , 0-->inbuilt webcam

while True:
    ret , frames = clip.read()
    cv2.imshow('window_1' , frames)

    if cv2.waitKey(22) & 0xFF == ord('q'):
        break

clip.release()
cv2.destroyAllWindows()
