import cv2
import numpy as np
#import os
import time
import matplotlib 
#from PIL import Image, ImageChops
#os.chdir(r"D:\Imagenes")
img1 = cv2.imread('imge2.png', 0)
img2 = cv2.imread('img2.png', 0)

imas = np.hstack((img1, img2))
cv2.imshow('imagenes', imas)

time.sleep(30)
