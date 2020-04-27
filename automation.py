from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

a=webdriver.Chrome()
a.get("https://www.google.com/")
a.maximize_window()

time.sleep(5)
elem=a.find_element_by_name("q")
elem.clear()

elem.send_keys("kandeepan")
elem.send_keys(Keys.RETURN)
assert "No result found" not in a.page_source




