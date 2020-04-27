from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait #web driver will wait untill browser loads
import time
import unittest

class logintest(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.get("https://www.facebook.com/")
        self.driver.maximize_window()
    def test_login(self):
        driver=self.driver
        #time.sleep(4)
        elem=driver.find_element_by_name("email")
        elem.clear()
        #time.sleep(2)
        elem.send_keys("kandeepan.ece1@gmail.com")
        #time.sleep(2)
        elem1=driver.find_element_by_name("pass")
        elem1.clear()
        elem1.send_keys("deep1312")
        #time.sleep(3)
        elem2=driver.find_element_by_id("loginbutton").click()
        #time.sleep(3)
    def tearDown(self):
        self.driver.quit()
if __name__=='__main__':
    unittest.main()


