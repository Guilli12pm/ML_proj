import numpy as np
import cv2
import os
from eyes_check import check_eyes
import shutil

directory = 'pic/'
for filename in os.listdir(directory):
    if filename.endswith(".png"):
        if check_eyes(filename):
            print(filename, "good")
            shutil.move("pic/"+filename, "next_ite/")
        else:
            print(filename, "bad")
