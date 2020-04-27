import unittest

from selenium import webdriver

class Test(unittest.TestCase):
    def testName(self):
        a=webdriver.Chrome("chromedriver.exe")
        self.assertIsNotNone(a)
        #self.assertIsNone(a)

if __name__=="__main__":
    unittest.main()