import XlAction
from selenium import webdriver

import time

path="C:\\Users\kandeepx\Documents\B\Login Credential.xlsx"
a=webdriver.Chrome("chromedriver.exe")
a.get("https://ksrtc.in/oprs-web/login/show.do")
a.maximize_window()
time.sleep(3)

rows=XlAction.GetRowCount(path,"Sheet1")
cols=XlAction.GetColCount(path,"Sheet1")

for r in range(2,rows+1):
    username=XlAction.ReadData(path,"Sheet1",r,1)
    password=XlAction.ReadData(path,"Sheet1",r,2)
    a.find_element_by_id("userName").send_keys(username)
    a.find_element_by_id("password").send_keys(password)
    a.find_element_by_id("submitBtn").click()
    if a.title=="KSRTC Official Website for Online Bus Ticket Booking - KSRTC.in":
        print("Test case passed")
        XlAction.WriteDate(path,"Sheet1",r,4,"Test Case Passed")
        a.find_element_by_link_text("Logout").click()
    else:
        print("Test Case Failed")
        XlAction.WriteDate(path,"Sheet1",r,4,"Test Case failed")

    a.find_element_by_link_text("Sign In").click()

print("Test Result saved in_(C:\\Users\kandeepx\Documents\B\Login Credential.xlsx)_mentioned location")
a.quit()



