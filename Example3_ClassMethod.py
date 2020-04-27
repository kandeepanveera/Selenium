import time
import unittest
from selenium import webdriver


class search(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.a=webdriver.Chrome()
        cls.a.get("https://www.amazon.in/")
        cls.a.maximize_window()
        time.sleep(5)
    def test_product1(self):
        elem1=self.a.find_element_by_xpath("//input[@id='twotabsearchtextbox']")
        elem1.send_keys("iphone\n")
        lis = self.a.find_elements_by_xpath("//h2[@class='a-size-mini a-spacing-none a-color-base s-line-clamp-2'] / a")
        print(str(len(lis)))
        for i in lis:
            print(i.text)
        time.sleep(4)
    def test_product2(self):
        elem1=self.a.find_element_by_xpath("//input[@id='twotabsearchtextbox']")
        elem1.clear()
        elem1.send_keys("oneplus mobiles\n")
        lis = self.a.find_elements_by_xpath("//h2[@class='a-size-mini a-spacing-none a-color-base s-line-clamp-2'] / a")
        print(str(len(lis)))
        for i in lis:
            print(i.text)
        time.sleep(2)
    @classmethod
    def tearDownClass(cls):
        cls.a.close()
if __name__ == "__main__":
    unittest.main()