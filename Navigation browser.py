# Navigating the single tab in browser(forward and backward history)

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome('chromedriver.exe')

driver.get("https://ksrtc.in/oprs-web/")
print(driver.title)# printing the title
driver.get("https://www.tnstc.in/home.html")
time.sleep(5)
print(driver.title)# printing the title
driver.back()
print(driver.title)# printing the title
driver.forward()
print(driver.title)# printing the title
driver.quit()