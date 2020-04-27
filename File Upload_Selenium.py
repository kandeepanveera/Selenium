import time

from selenium import webdriver
#from selenium.webdriver import ActionChains


a=webdriver.Chrome("chromedriver.exe")
a.get("http://testautomationpractice.blogspot.com/")

a.maximize_window()
a.switch_to.frame("frame-one1434677811")
a.find_element_by_id("RESULT_FileUpload-10").send_keys("‪C://Users/kandeepx/Pictures/ajiyh.jpg")
a.quit()


