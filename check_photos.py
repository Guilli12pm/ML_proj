import numpy as np
import cv2
import os
from eyes_check import check_eyes
import shutil

"""
directory = 'pic/'
for filename in os.listdir(directory):
    if filename.endswith(".png"):
        if check_eyes(filename):
            print(filename, "good")
            shutil.move("pic/"+filename, "next_ite/")
        else:
            print(filename, "bad")

"""

directory = 'Database/'

#print(os.listdir(directory))

#print(os.listdir(directory + os.listdir(directory)[0]))

for names in os.listdir(directory):
    if os.path.isdir(directory + names):
        if names not in os.listdir("next_ite/"):
            os.mkdir("next_ite/" + names + "/")
            print("\n")
            print("Working on: ", names)
            print("\n")
            for filename in os.listdir(directory + names + "/"):
                if filename.endswith(".png"):
                    if check_eyes(directory + names + "/",filename):
                        print(filename, "good")
                        shutil.move(directory + names + "/" + filename, "next_ite/" + names + "/")
                    else:
                        print(filename, "bad")
        else:
            print("\n")
            print("Working on: ", names)
            print("\n")
            for filename in os.listdir(directory + names + "/"):
                if filename.endswith(".png"):
                    if check_eyes(directory + names + "/",filename):
                        print(filename, "good")
                        shutil.move(directory + names + "/" + filename, "next_ite/" + names + "/")
                    else:
                        print(filename, "bad")
        shutil.rmtree(directory + names)
