import numpy as np
import cv2
from PIL import ImageGrab


def check_eyes(name):

  eyeCascade = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')

  frame = cv2.imread("pic/"+name)

  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

  eyes = eyeCascade.detectMultiScale(
          gray
      )

  # Check if detected eyes is greater than 1 
  if len(list(eyes)) > 0:
    return True
  else:
    return False

