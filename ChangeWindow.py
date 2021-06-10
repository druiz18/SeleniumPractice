import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class using_unittest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"D:\chromeDriver\chromedriver_win32\chromedriver.exe")

    def test_ChangeWindow (self):
        driver = self.driver 
        
        driver.get("http://www.google.com")
        driver.maximize_window ()
        # try:
        #     element = WebDriverWait(driver, 10).until(EC.EC.presence_of_all_elements_located((By.NAME, "q")))
        # finally:
        #     driver.quit()

        driver.execute_script("window.open('');")
        #time.sleep(3)
        driver.switch_to.window(driver.window_handles[1])
        driver.get("http://stackoverflow.com")
        #time.sleep(3)
        driver.switch_to.window(driver.window_handles[0])
        #time.sleep(3)
        driver.execute_script("window.open('');")
        #time.sleep(3)
        driver.switch_to.window(driver.window_handles[2])
        driver.get("http://www.python.org")
        #time.sleep(3)
        driver.get("http://www.blender.org")
        #time.sleep(3)
        driver.back()
        #time.sleep(3)
        driver.switch_to.window(driver.window_handles[0])
        self.assertIn("Google", driver.title)
        element=driver.find_element_by_name("q")
        
        element.send_keys("selenium")
        element.send_keys(Keys.RETURN)
        try:
            element = WebDriverWait(driver, 10).until(EC.EC.presence_of_all_elements_located((By.NAME, "q")))
        finally:
            driver.quit()
        #time.sleep(5)
        assert "no se encontró el elemento: " not in driver.page_source

if __name__ == '__main__':
    unittest.main()
