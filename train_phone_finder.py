import scipy
from scipy import signal
import numpy as np
import cv2
from matplotlib import pyplot as plt
import os
from random import randint
import numpy as np
import scipy.stats as st
from skimage.color import rgb2gray
import sys

#Function that takes in the path of the image and spits out the 
#normalized centroid location of the phone with respect to the image dimentions
#It finds only one possible object

def findCentroid(path):
    # reading the image as a greyscale
    img =cv2.imread(path,0)  
    #getting image dimensions                                             
    h ,w = np.shape(img)
    #using a smoothing filer of size 8x8 to remove noise
    img = cv2.blur(img,(8,8))
    #converting to binary using a value of 60 as the threshold, pixels with any value above this is a differnet class
    _,thresh2 = cv2.threshold(img,60,255,cv2.THRESH_BINARY_INV)
    #getting the contours as a list of objects 
    _,contours,_ = cv2.findContours(thresh2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if len(contours)<1: 
        return (0,0)         #if no contous are found return the center to be (0,0) i.e trhe origin
    # consider the first contour
    cnt = contours[0]
    # getting the dimentions of minimum area rectangle that surrounds the 1st contour in the list  
    # rect contains the following tuple ( center (x,y), (width, height), angle of rotation )
    rect = cv2.minAreaRect(cnt)
    # returing the normalized coordinates of the center
    return (rect[0][0]/w,rect[0][1]/h)

def main():
    #forming the agrument for the path to the dataset
    path = sys.argv[1]+'/'
    f = open(path+'labels.txt', 'r') 
    i = 0               #counter for the number of correctly processed images
    total = 0           # total number of images processed
    for x in f:         #read each line in the labels.txt file
        total+=1        #incerement the number of images processed by 1
        #break down the line into a 3-element tuple where, 
        #1st element is the image file name, 2nd is the x coordinate while the third is the y coordinate of the phone location
        val = x.split() 
        #forming the path of the image file with the first element of each line
        p = path+val[0]
        #getting the centroid of the phone in the image file via the findCentroid function
        (x,y) = findCentroid(p)
        # getting the ground-truth
        ax, ay = (float)(val[1]), (float)(val[2])
        #checking the error margin to be less than the .05 units circle
        if ((pow(x-ax,2)+pow(y-ay,2))<0.0025):
            i+=1 # counting the image as succesfully detected
    f.close()
    print('Accuracy with the given dataset: {:2.2%}'.format(i/total)) #displaying the accuracy 

if __name__ == '__main__':
    main()