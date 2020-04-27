from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import HtmlTestRunner


class OrangeHDMTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.a = webdriver.Chrome("chromedriver.exe")
        cls.a.maximize_window()

    def test_Title(self):
        self.a.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
        s = self.a.title
        self.assertEqual("OrangeHRM", s, "Webpage Title is wrong")

    def test_login(self):
        self.a.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
        ele1 = self.a.find_element(By.ID, "txtUsername").send_keys("Admin")
        ele2 = self.a.find_element(By.ID, "txtPassword").send_keys("admin123")
        self.a.find_element(By.ID, "btnLogin").click()
        self.assertEqual("OrangeHRM", self.a.title, "Webpage Title is wrong")

    @classmethod
    def tearDownClass(cls):
        cls.a.quit()
        print("Test completed....!!!")

if __name__ == '__main__':
    unittest.main(verbosity=2)

