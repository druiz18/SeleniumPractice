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
        driver.implicitly_wait(3)
        #time.sleep(3)
        #assert "no se encontró el elemento: " not in driver.page_source

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
        
        
if __name__=='__main__':
    unittest.main()