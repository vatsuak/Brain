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
img =cv2.imread('./find_phone/29.jpg')

mask[newmask == 0] = 1
mask[newmask == 255] = 0
mask, bgdModel, fgdModel = cv.grabCut(img,mask,None,bgdModel,fgdModel,5,cv.GC_INIT_WITH_MASK)
mask = np.where((mask==2)|(mask==0),0,1).astype('uint8')
img = img*mask[:,:,np.newaxis]

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
h ,w = np.shape(img)
img = cv2.blur(img,(7,7))
_,thresh2 = cv2.threshold(img,100,255,cv2.THRESH_BINARY_INV)
# thresh2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV,11,0)
# thresh2 = cv2.blur(thresh2,(13,13))
plt.imshow(thresh2,'gray')
plt.show()
# _,contours,_ = cv2.findContours(thresh2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# cnt = contours[0]
# rect = cv2.minAreaRect(cnt)
# box = cv2.boxPoints(rect)
# box = np.int0(box)
# print(box)
# plt.imshow(cv2.drawContours(img,[box],0,(255,255,255),2),'gray')
# plt.show()

