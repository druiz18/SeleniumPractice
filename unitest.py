import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class using_unittest (unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"D:\chromeDriver\chromedriver_win32\chromedriver.exe")

    def test_search(self):
        driver = self.driver
        driver.get("http://www.google.com")
        self.assertIn("Google", driver.title)
        element=driver.find_element_by_name("q")
        element.send_keys("selenium")
        element.send_keys(Keys.RETURN)
        time.sleep(5)
        assert "no se encontró el elemento: " not in driver.page_source

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__': #name y main van entre dos doble guión bajo
    unittest.main()