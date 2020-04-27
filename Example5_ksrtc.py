from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

a=webdriver.Chrome()
a.get("https://ksrtc.in/oprs-web/login/show.do")
a.maximize_window()


a.find_element_by_id("userName").send_keys("kandeepan.ece1@gmail.com")
a.find_element_by_id("password").send_keys("Deepshika@123")
a.find_element_by_id("submitBtn").click()

print(a.title)
a.quit()

#elem3=a.find_element_by_id("notificationsCountValue")
#elem3.text








