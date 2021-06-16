import cv2
import numpy as np
#import os
import time

#from PIL import Image, ImageChops
#os.chdir(r"D:\Imagenes")
img1 = cv2.imread('imge2.png', 0)
img2 = cv2.imread('img2.png', 0)

cv2.imshow('Foto', img1)
cv2.waitKey(0)
cv2.destroyAllWindows()

