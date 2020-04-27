import unittest
from selenium import webdriver

class SearchEngineTest(unittest.TestCase):
    def test_google(self):
        self.driver=webdriver.Chrome("chromedriver.exe")
        self.driver.get("http://newtours.demoaut.com/")
        print("Title of the page is  :"+self.driver.title)
        self.driver.close()
    def test_mercury(self):
        self.driver=webdriver.Chrome("chromedriver.exe")
        self.driver.get("https://ksrtc.in/oprs-web/")
        print("Title of the page is  :" + self.driver.title)
        self.driver.close()
if __name__=="__main__":
    unittest.main()

