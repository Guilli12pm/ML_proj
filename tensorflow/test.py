import numpy as np
from keras.preprocessing.image import load_img, img_to_array
import matplotlib.pyplot as plt
import os

# size of the image: 48*48 pixels
pic_size = 48

# input path for the images
base_path = "../Database/"

plt.figure(0, figsize=(12,20))
cpt = 0
print(os.listdir(base_path).remove('.DS_Store'))

for names in os.listdir(base_path):
    if names != '.DS_Store':
        for pic in os.listdir(base_path + names + "/"):
            if pic != '.DS_Store':
                cpt = cpt + 1
                plt.subplot(7,5,cpt)
                img = load_img(base_path + names + "/" + pic , target_size=(pic_size, pic_size))
                plt.imshow(img, cmap="gray")

plt.tight_layout()
plt.show()
