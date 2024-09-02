import cv2

clip = cv2.VideoCapture('Resource/samples_data_tree.avi') # Open the video file

while True:
    ret , frames = clip.read() # covert the video into each frames
    cv2.imshow('window_1' , frames)  # Display the frame

    if cv2.waitKey(20) & 0xFF == ord('q'): 
        break

clip.release()
cv2.destroyAllWindows()
