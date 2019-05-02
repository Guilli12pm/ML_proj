import numpy as np
import cv2
from PIL import ImageGrab

faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

frame = cv2.imread("opencv_frame_9.jpg")

gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=10,
		minSize=(75, 75)
    )

print(faces)