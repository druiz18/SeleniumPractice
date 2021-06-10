import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path=r"D:\chromeDriver\chromedriver_win32\chromedriver.exe")
driver.get("http://gmail.com")

user = driver.find_element_by_id("identifierId")
user.send_keys("d.ruiz2257@gmail.com")
user.send_keys(Keys.ENTER)
time.sleep(10)

password = driver.find_element_by_name("password")
password.send_keys("lauyruiz100pre")
password.send_keys(Keys.ENTER)
time.sleep(50)
driver.close()