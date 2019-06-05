import cv2
import numpy as np
import os
#from matplotlib import pyplot as plt
import argparse
import imutils
import random
from shutil import copyfile

def sp_noise(image,prob):
    '''
    Add salt and pepper noise to image
    prob: Probability of the noise 0.01-0.1
    '''
    output = np.zeros(image.shape,np.uint8)
    thres = 1 - prob
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            rdn = random.random()
            if rdn < prob:
                output[i][j] = 0
            elif rdn > thres:
                output[i][j] = 255
            else:
                output[i][j] = image[i][j]
    return output

for names in ['to_erase']: #os.listdir("next_ite"):
    if names != ".DS_Store":
        print("Working on:", names)
        os.mkdir("new_pic/"+names)
        os.mkdir("normal_pic/"+names)
        li = os.listdir("next_ite/"+names)
        if ".DS_Store" in li:
            li.remove(".DS_Store")
        random.shuffle(li)
        for i in range(10):
            copyfile("next_ite/"+names+"/"+li[i],"new_pic/"+names + "/"+li[i])
            copyfile("next_ite/"+names+"/"+li[i],"normal_pic/"+names + "/"+li[i])
            # Blurring
            img = cv2.imread("next_ite/" + names + "/" + li[i])
            kernel = np.ones((5,5),np.float32)/25
            dst = cv2.filter2D(img,-1,kernel)
            cv2.imwrite("new_pic/"+names+"/"+li[i].strip(".png") + "_blurred_" + str(i) + ".png",dst)

            # Sharpening
            img1 = cv2.imread("next_ite/" + names + "/" + li[i])
            kernel_sharpening1 = np.array([[-1,-1,-1],
                              [-1, 9,-1],
                              [-1,-1,-1]])
            sharpened1 = cv2.filter2D(img1, -1, kernel_sharpening1)
            cv2.imwrite("new_pic/"+names+"/"+li[i].strip(".png") + "_sharpened_1_" + str(i) + ".png",sharpened1)

            img2 = cv2.imread("next_ite/" + names + "/" + li[i])
            kernel_sharpening2 = np.array([[-1,-1,-1],
                              [-1, 10,-1],
                              [-1,-1,-1]])
            sharpened2 = cv2.filter2D(img2, -1, kernel_sharpening2)
            cv2.imwrite("new_pic/"+names+"/"+li[i].strip(".png") + "_sharpened_2_" + str(i) + ".png",sharpened2)

            # S&P
            for numb in range(1,11,2):
                img = cv2.imread("next_ite/" + names + "/" + li[i])
                new = sp_noise(img,numb/100)
                cv2.imwrite("new_pic/"+names+"/"+li[i].strip(".png") + "_sp_" + str(numb) + ".png",new)

        for im in os.listdir("new_pic/"+names):
            if im != ".DS_Store":
                image = cv2.imread("new_pic/"+names+"/" + im)
                j = 0
                for angle in np.arange(0, 90, 30):
                    rotated = imutils.rotate_bound(image, angle)
                    cv2.imwrite("new_pic/"+names+"/"+im.strip(".png") + "_rot_anty_" + str(j) + ".png",rotated)
                    j += 1
                j = 0
                for angle in np.arange(-90, 0, 30):
                    rotated = imutils.rotate_bound(image, angle)
                    cv2.imwrite("new_pic/"+names+"/"+im.strip(".png") + "_rot_clock_" + str(j) + ".png",rotated)
                    j += 1
