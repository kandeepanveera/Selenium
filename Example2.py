import time
import unittest
from selenium import webdriver

class search(unittest.TestCase):
    def setUp(self):
        self.a=webdriver.Chrome()
        self.a.get("https://www.amazon.in/")
        self.a.maximize_window()
        time.sleep(5)
    def test_product(self):
        elem1=self.a.find_element_by_xpath("//input[@id='twotabsearchtextbox']")
        elem1.send_keys("iphone\n")
        lis=self.a.find_elements_by_xpath("//h2[@class='a-size-mini a-spacing-none a-color-base s-line-clamp-2'] / a")
        print(str(len(lis)))
        #self.assertEqual(,len(lis))

        for i in lis:
            print(i.text)
    def tearDown(self):
        self.a.close()
if __name__ == "__main__":
    unittest.main()
