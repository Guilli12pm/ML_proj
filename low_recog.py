import numpy as np
import cv2
import os
from eyes_check import check_eyes
import shutil
from codes import check_closer

video_capture = cv2.VideoCapture(0)
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
font = cv2.FONT_HERSHEY_SIMPLEX

#Ratios
ratio_all = {}
#print(os.listdir("Database/"))
for names in os.listdir("next_ite/"):
    if names != '.DS_Store':
        numb = 0
        ratio = []
        for pic in os.listdir("next_ite/" + names + "/"):
            if names != '.DS_Store':
                im = cv2.imread("next_ite/" + names + "/" + pic)
                height, width, what = im.shape
                numb += 1
                ratio.append(height)
        ratio_all[names] = sum(ratio)/numb

print(ratio_all)
while True:
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        who = check_closer(ratio_all,x)
        cv2.putText(frame,who,(x,y+20),font,0.8, (0, 255, 0), 2, cv2.LINE_AA)
    
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break



video_capture.release()
cv2.destroyAllWindows()