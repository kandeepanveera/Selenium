"""
Switching frame

"""

from selenium import webdriver
import time
from selenium.webdriver.common.by import By

a=webdriver.Chrome("chromedriver.exe")
a.get("https://selenium.dev/selenium/docs/api/java/")
time.sleep(3)

a.switch_to.frame("packageListFrame")#first frame
y=a.find_element_by_link_text("org.openqa.selenium").click()
#each time frame switching we cant to directly ,need to go main page and then we need to swift to second frme
a.switch_to.default_content()#main page it will switch
time.sleep(3)

a.switch_to.frame("packageFrame")#second frame
a.find_element_by_link_text("WebDriver").click()
time.sleep(3)

a.quit()

