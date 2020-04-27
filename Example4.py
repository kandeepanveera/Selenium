import time
from selenium import webdriver
import unittest

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

class Homepagetest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.a=webdriver.Chrome()
        cls.a.get("https://www.amazon.in/")
        cls.a.maximize_window()
        time.sleep(5)
    def test_Searchbox(self):
        #self.assertTrue(self.is_element_present (By.ID,"twotabsearchtextbox"))
        self.assertTrue(self.a.find_element_by_id("twotabsearchtextbox").is_enabled())
        x=self.a.find_element_by_id("twotabsearchtextbox").get_attribute("maxlength")
        print (str(x))
    #def test_lanugage(self):
        self.assertTrue(self.a.is_element_present(By.ID,"icp-nav-language"))
    
    def test_addcard(self):
        self.a.find_element_by_id("nav-cart")
        x="Your Shopping Cart is empty"
        y=self.a.find_element_by_css_selector("div.a-row sc-cart-header h1.sc-empty-cart-header").text()
        self.assertEqual(x,y)

        #self.assertEqual("128",x)
    @classmethod
    def tearDownClass(cls):
        cls.a.close()

if __name__ == "__main__":
    unittest.main()



