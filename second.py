import cv2
import pytesseract
import re
import os


cwd = os.getcwd()
data=[]
#load all images in the folder
inputfolder=cwd+"/assets"
if os.path.exists("preproceced")==False:
   os.mkdir("preproceced")
def load_images_from_folder(folder):
    images=[]
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename),-1)
        if img is not None:
           image=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY )
           cv2.imwrite('preproceced/'+filename,image)
           images.append(filename)
    return images
images=load_images_from_folder(inputfolder)
# print(len(images))
secondir=cwd+"\\preproceced"
 
for filename in os.listdir("preproceced"):
    #path = os.path.join(secondir,filename)
    path =os.path.join("preproceced",filename)
    # print(os.path.join("preproceced",filename))
    if path is not None:
       src = cv2.imread(os.path.join("preproceced",filename),-1)
       #src=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY )
       # cv2.imwrite("output2.png",src)

       hImg,wImg=src.shape
       boxes=pytesseract.image_to_data(src)
       for x,b in enumerate(boxes.splitlines()):
           if x!=0:
              b=b.split()
              #print(b)
              if len(b)==12:
                # x,y,w,h==int(b[6]),int(b[7]),int(b[8]),int(b[9])
                #    x,y,w,h=20,632,529,39
                #   x,y,w,h=476,320,462,80
                #    cv2.rectangle(src,(x,y),(w+x,h+y),(0,0,255),3)
                #    cv2.putText(src, "text", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
                #    1.2, (0, 0, 255), 3)   
                #NAME = src[y:y+h,x:x+w]
                NAME=src[632:632+39,20:20+529]
                ID=src[320:320+80,476:476+462]
                #if images rotation is correct just comment this part 'bottom 3 lines' to speed the program else uncomment it
                name = pytesseract.image_to_string(NAME, lang='eng',config='--psm 6')
                if name.startswith("Name:")==False:
                   src=cv2.rotate(src, cv2.ROTATE_180)
                #if images rotation   
       id = pytesseract.image_to_string(ID, lang='eng',config='--psm 6')
       name = pytesseract.image_to_string(NAME, lang='eng',config='--psm 6')
       data.append({'name':name.replace('Name: ', ''),'id':id})
    
    
print("data is :")
print(data) 
# "a" - Append - will append to the end of the file
# "w" - Write - will overwrite any existing content
f = open("data.txt", "w")
f.write(str(data))
f.close()

# cv2.imshow('result',src)
# cv2.waitKey(0)