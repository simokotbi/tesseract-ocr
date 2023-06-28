import cv2
import pytesseract
import re
import os
 
 
cwd = os.getcwd()
data=[]
#load all images in the folder
inputfolder=cwd+"/assets"

def load_images_from_folder(folder,image_name):
        img = cv2.imread(os.path.join(folder,str(image_name)),-1)
        if img is not None:
           image=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY )
           img = cv2.GaussianBlur(img, (5,5), 0)
           cv2.threshold(img,127,255,cv2.THRESH_BINARY)
        #    cv2.imwrite('preproceced/'+filename,image)
           hImg,wImg=image.shape
           boxes=pytesseract.image_to_data(image)
           for x,b in enumerate(boxes.splitlines()):
              if x!=0:
                 b=b.split()
                 #print(b)
                 if len(b)==12:
                  
                    NAME=image[632:632+39,20:20+529]
                    ID=image[320:320+80,476:476+462]
                    name = pytesseract.image_to_string(NAME, lang='eng',config='--psm 6')
                    if name.startswith("Name:")==False:
                       image=cv2.rotate(image, cv2.ROTATE_180)   
           id = pytesseract.image_to_string(ID, lang='eng',config='--psm 6')
           name = pytesseract.image_to_string(NAME, lang='eng',config='--psm 6')
           data.append({'name':name.replace('Name: ', '').replace('\n', ''),'id':id.replace('\n', ''),'ImageName':image_name})
           return data
        else:
          return "image not existing"
      
        # print("data is :")
        # print(data) 
        # # "a" - Append - will append to the end of the file
        # # "w" - Write - will overwrite any existing content
        # f = open("data.txt", "w")
        # f.write(str(data))
        # f.close()


def treatImage(image_name):
    return load_images_from_folder(inputfolder, image_name)
