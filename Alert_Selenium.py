"""Working with Alerts

    -switch_to_alert().accept()
    -switch_to_alert().dismiss()"""

import selenium
from selenium import webdriver
import time

a=webdriver.Chrome("chromedriver.exe")
a.get("http://testautomationpractice.blogspot.com/")

a.find_element_by_xpath("//*[@id='HTML9']/div[1]/button").click()

time.sleep(5)
#print(a.switch_to_alert().text)
a.switch_to_alert().accept()
mess=a.find_element_by_id("demo")
print(mess.text)

print(a.title)

a.quit()
