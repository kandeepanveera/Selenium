"""
AssertEqual
AssertNotequal
"""

import unittest
from selenium import webdriver

class Test(unittest.TestCase):
    def test_google(self):
        driver=webdriver.Chrome("chromedriver.exe")
        driver.get("https://www.google.com/")
        tit=driver.title
        #self.assertNotEqual("Google23",tit,"its not equal")
        self.assertEqual("Google", tit, "its not equal")
if __name__=="__main__":
    unittest.main()
