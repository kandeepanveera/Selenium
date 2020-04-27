import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PythonOrg(unittest.TestCase):
    def setup(self):
        self.driver=webdriver.Chrome()
    def test_search(self):
        a=self.driver
        a.get("https://www.google.com/")
        a.maximize_window()
        self.assertIn("Google",a.title)
        elem=a.find_element_by_name("q")
        elem.clear()
        elem.send_keys("Deepshika")
        elem.send_keys(Keys.RETURN)
        assert "No results found" not in a.page_source
    def tearDown(self):
        self.a.quit()


if __name__ == "__main__":
    unittest.main(verbosity=2)




