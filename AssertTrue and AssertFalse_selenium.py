import unittest
from selenium import webdriver

class Test(unittest.TestCase):
    def testName(self):
        a=webdriver.Chrome("chromedriver.exe")
        a.get("https://www.google.com/")
        tit=a.title
        #self.assertTrue(tit=="Google") #True
        self.assertFalse(tit == "Google123")  # False

if __name__=="__main__":
    unittest.main()