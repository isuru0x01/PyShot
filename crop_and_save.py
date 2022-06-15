import cv2
import numpy as np
from os.path import join
from os import listdir
import easyocr
from matplotlib import pyplot as plt
import numpy as np

import os
os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"


saving_directory = r"output"
browsing_directory = r"input"

def crop_save():
    images = listdir(browsing_directory)
    image_arrays = []
    count = 0
    for image in images:
        im = cv2.imread(join(browsing_directory,image))
        exten = "."+image.split(".")[-1]
        image_arrays.append(im)
        print(f"Image {image} has dimensions as {np.shape(im)[0]} X {np.shape(im)[1]}.")
        x,y,w,h = cv2.selectROI(im)
        cropped_image = im[y:y+h,x:x+w]
        cv2.imshow("Res",cropped_image)
        print(f"Image created status: {cv2.imwrite(join(saving_directory,str(count)+exten),cropped_image)}")
        count = count+1
        print("Process complete...")
    

def extract_text():
    IMAGE_PATH = "output\\0.png"

    reader = easyocr.Reader(['en'], gpu=False)
    result = reader.readtext(IMAGE_PATH)

    img = cv2.imread(IMAGE_PATH)
    for detection in result:
        top_left = tuple([int(val) for val in detection[0][0]])
        bottom_right = tuple([int(val) for val in detection[0][2]])
        text = detection[1]
        font = cv2.FONT_HERSHEY_SIMPLEX
        img = cv2.rectangle(img, top_left, bottom_right, (0, 255, 0), 2)
        #img = cv2.putText(img, text, top_left, font, 2, (255,255,255),2, cv2.LINE_AA)
        print(text)

    plt.figure(figsize=(10,10))
    plt.imshow(img)
    plt.show()

    