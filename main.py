from pdf2image import convert_from_path
from PIL import Image
import cv2
import matplotlib.pyplot as plt
import numpy as np
import os


mainDir = 'C:\Projects\openCV\pdfdarkmode\darkmodepdf\pdf'


def convertPDF():
    images = convert_from_path(mainDir+'\sample1.pdf')
    for i,image in enumerate(images):
        image = np.array(image)
        beforeImg = image
        image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        _,image = cv2.threshold(image,60,255,cv2.THRESH_BINARY_INV)
        blur = cv2.GaussianBlur(image,(3,3),0)
        imgnew = cv2.addWeighted(blur,2,image,-0.5,0)
        kernel = np.ones((1,1),np.uint8)
        image = cv2.dilate(imgnew,kernel,iterations=1)
        cv2.imwrite(mainDir+'\image'+str(i)+'.png',image)
        print("Lol")
     

def validateDIR(dirList):
    newArr = []
    for link in dirList:
        if link[-3:] == 'png':
            newArr.append(link)    

    return newArr    

def makePDF():
    list_of_images = os.listdir(mainDir)

    list_of_images = validateDIR(list_of_images)

    images = []

    for i in range(len(list_of_images)):
        images.append(Image.open(mainDir+'\\'+list_of_images[i]))

    images[0].save(mainDir+'\\'+'converted1.pdf',save_all=True,append_images = images[1:])
    print(images)

def delImages():
    list_of_images = os.listdir(mainDir)
    list_of_images = validateDIR(list_of_images)
    for l in list_of_images:
        os.remove(mainDir+'\\\\'+l) 

convertPDF()
makePDF()
delImages()

