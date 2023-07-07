import cv2
import pytesseract
import re
import os
import numpy as np
from regex import text_clean_up
 
cwd = os.getcwd()
data=[]
#load all images in the folder
inputfolder=cwd+"/assets"

def load_images_from_folder(folder,image_name):
        img = cv2.imread(os.path.join(folder,str(image_name)),-1)
        if img is not None:
           image=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY )
         #   image = cv2.GaussianBlur(image, (5,5), 0)
           image = cv2.bilateralFilter(image,9,75,75)

           kernel = np.ones((1, 1), np.uint8) 
           image = cv2.dilate(image, kernel, iterations=1)  
           image = cv2.erode(image, kernel, iterations=1)
           cv2.threshold(image,127,255,cv2.THRESH_BINARY)
           image = cv2.resize(image,(1356,856))
           hImg,wImg=image.shape
         
           test=image[171:171+500,20:20+1069]
           test = pytesseract.image_to_string(test, lang='eng',config='--psm 6')
           pattern = r'Name:'
           match = re.search(pattern, test)
           if not match:
               image=cv2.rotate(image, cv2.ROTATE_180)    
         
           test=image[171:171+500,20:20+1069]
           test = pytesseract.image_to_string(test, lang='eng',config='--psm 6')
           data=text_clean_up(test)
           return data
        else:
          return "image not existing"


def treatImage(image_name):
    return load_images_from_folder(inputfolder, image_name)
