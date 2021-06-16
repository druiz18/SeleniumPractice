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
        driver.get("http://www.youtube.com")
        driver.save_screenshot('img2.png')
        time.sleep(3)
        assert "no se encontró el elemento: " not in driver.page_source

    def test_compare(self):
        imagen1 = cv2.imread("img1.png", 1)
        imagen2 = cv2.imread("img2.png", 1)

        newimg1 = cv2.resize(imagen1, (500, 300))
        newimg2 = cv2.resize(imagen2, (500, 300))

        diferencia = cv2.subtract(newimg1, newimg2)

        #definir funcion de comparacion
        def compara (im1, im2):
	        diferencia = cv2.subtract(im1, im2)
	        if not np.any(diferencia):
		        print("Las imagenes son iguales")
	        else:
		        print("Las imagenes son diferentes")
        #mostrar las dos imagenes en pantalla
        imas = np.hstack((newimg1, newimg2))
        cv2.imshow("fotos", imas)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        #crear imagen de diferencia
        cv2.imwrite("imDiferencia.png", diferencia) 
        cv2.imshow("diferencia", diferencia)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        # img1 = Image.open('img1.png', 0)
        # img2 = Image.open('img2.png', 0)

        # diferencia = ImageChops.difference(img1, img2)
        # if diferencia.getbbox():
        #     diferencia.show()

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