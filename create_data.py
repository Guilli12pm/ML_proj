import numpy as np
import cv2  #pip install opencv-python
import sys
from PIL import ImageGrab  #pip install Pillow
import keyboard #pip install keyboard
import time
import os

name = input("Enter name: ")
tot_numb_pic = int(input("\nEnter the number of pic you want to take: "))
new_name = name.replace(" ", "_")
os.mkdir("Database/" + new_name)

faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

video_capture = cv2.VideoCapture(0)

i = 0
numb_pic = 1

print('\nPlease check that nothing covers your camera \n')

#print("Keep 'Space' pressed as long as you want to take pictures")

val = True
while numb_pic <= tot_numb_pic:
#while val:
    #while keyboard.is_pressed(' '):
        #val = False

    i += 1
    #print(i)
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
            img_name = new_name+"_{}.png".format(numb_pic)
            cv2.imwrite("database/"+ new_name + "/" +img_name, frame)
            print("{} written!".format(img_name))
            numb_pic += 1


# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
