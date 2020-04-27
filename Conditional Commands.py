"""===============================
conditional commands
1.is_displayed()
2.is_enabled()
3.is_selected()

conditional commands is usefull to verify the radio button ,search box enable and displayed
================================="""

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

x=webdriver.Chrome("chromedriver.exe")
x.get("https://ksrtc.in/oprs-web/login/show.do")
x.maximize_window()
time.sleep(3)

ele=x.find_element_by_id("userName")
print("Username box is Displayed?")
print(ele.is_displayed())# returns the True or False
print("Username box is Enabled?")
print(ele.is_enabled())# returns the True or False

ele1=x.find_element_by_id("password")
print("Password box is present?")
print(ele1.is_displayed())# returns the True or False
print("Password box is Enabled?")
print(ele1.is_enabled())# returns the True or False

ele2=x.find_element_by_id("TermsConditions")
print("Terms & conditions is selected?")
print(ele2.is_selected())

x.quit()