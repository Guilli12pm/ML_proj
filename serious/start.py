import numpy as np
import cv2
import sys
from PIL import ImageGrab
import time

faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

video_capture = cv2.VideoCapture(0)

i = 0
numb_pic = 1

while numb_pic != 30:
    i += 1
    print(i)
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.FONT_HERSHEY_SIMPLEX
    )

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
    if len(list(faces)) != 0:
        if i%2 == 0:
            frame = frame[y+2:y+(h-4) , x+2:x+(w-4)]
            img_name = "test_{}.png".format(numb_pic)
            cv2.imwrite("pic/"+img_name, frame)
            print("{} written!".format(img_name))
            numb_pic += 1


# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
