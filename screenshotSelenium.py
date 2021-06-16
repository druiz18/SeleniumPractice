import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import cv2
import numpy as np
import time
from PIL import Image, ImageChops
class using_unittest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"D:\chromeDriver\chromedriver_win32\chromedriver.exe")

    def test_using_opencv(self):
        driver = self.driver
        driver.get("http://www.google.com")
        driver.save_screenshot('img2.png')
        time.sleep(3)
        assert "no se encontró el elemento: " not in driver.page_source

    def test_compare(self):
        img1 = Image.open('img1.png')
        img2 = Image.open('img2.png')

        diferencia = ImageChops.difference(img1, img2)
        if diferencia.getbbox():
            diferencia.show()

        # imagen_gris = cv2.cvtColor(diferencia,cv2.COLOR_BGR2GRAY)
        # contours,_ = cv2.findContours(imagen_gris,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        # for c in contours:
        #     if cv2.contourArea(c) >= 20:
        #         posicion_x,posicion_y,ancho,alto = cv2.boundingRect(c)
        #         cv2.rectangle(img1(posicion_x,posicion_y),(posicion_x+ancho,posicion_y+alto),(0,0,255),2)

        # while(1):
        #     cv2.imshow('imagen1', img1)
        #     cv2.imshow('imagen2', img2)
        #     cv2.imshow('diferencia detectada', diferencia)
        #     cv2.waitKey(0)
        #     #cv2.destroyAllWindows()
        
if __name__=='__main__':
    unittest.main()