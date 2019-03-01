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

def findCentroid(path):
    img =cv2.imread(path,0)
    h ,w = np.shape(img)
    
    #img = cv2.equalizeHist(img)
    img = cv2.blur(img,(8,8))
    _,thresh2 = cv2.threshold(img,60,255,cv2.THRESH_BINARY_INV)
    _,contours,_ = cv2.findContours(thresh2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if len(contours)<1:
        return (0,0)
    cnt = contours[0]
    rect = cv2.minAreaRect(cnt)
    box = cv2.boxPoints(rect)
    box = np.int0(box)
    return (rect[0][0]/w,rect[0][1]/h)

def main():
    path = sys.argv[1]+'/'
    f = open(path+'labels.txt', 'r') 
    i = 0
    total = 0
    for x in f:
        total+=1
        val = x.split()
        p = path+val[0]
        (x,y) = findCentroid(p)
        ax, ay = (float)(val[1]), (float)(val[2])
        if ((pow(x-ax,2)+pow(y-ay,2))<0.0025):
            i+=1
    f.close()
    print('Accuracy with the given dataset: {:2.2%}'.format(i/total))

if __name__ == '__main__':
    main()