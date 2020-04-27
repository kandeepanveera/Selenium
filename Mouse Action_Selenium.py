"""
============================
Mouse Action
-mouse hover
-double click
-right click
drag and drop
=============================
"""
import time

from selenium import webdriver
from selenium.webdriver import ActionChains


a=webdriver.Chrome("chromedriver.exe")

a.get("https://opensource-demo.orangehrmlive.com/")
a.maximize_window()
print("Title",a.title)
time.sleep(2)
a.find_element_by_id("txtUsername").send_keys("admin")
a.find_element_by_id("txtPassword").send_keys("admin123")
a.find_element_by_id("btnLogin").click()
admin=a.find_element_by_xpath("//*[@id='menu_admin_viewAdminModule']/b")
usermang=a.find_element_by_id("menu_admin_UserManagement")
user=a.find_element_by_id("menu_admin_viewSystemUsers")

actions=ActionChains(a)

actions.move_to_element(admin).move_to_element(usermang).move_to_element(user).click().perform()

time.sleep(3)

print("MouseHover test completed")
#===================================#Doucble click testing=======================================================

a.get("https://clicktestspeed.com/double-click-test")
a.maximize_window()
print("Title",a.title)
time.sleep(2)
double=a.find_element_by_id("clickarea")
actions=ActionChains(a)
actions.double_click(double).perform()#double click on element
actions.double_click(double).perform()
actions.double_click(double).perform()
actions.double_click(double).perform()
time.sleep(3)
v=a.find_element_by_id("clicks").text
y=a.find_element_by_id("cps").text
print("How Many Clicks performed in 5sec;", v)
print("Double clicks per second;", y)


print("\nDouble Click Test finished")

#====================================Right Click========================================================

a.get("https://unixpapa.com/js/testmouse.html")
right=a.find_element_by_xpath("/html/body/table/tbody/tr/td[1]/a[1]")
actions=ActionChains(a)
actions.context_click(right).perform()
message=a.find_element_by_xpath("/html/body/table/tbody/tr/td[1]/form/textarea").text

print("Please Find the mouse click actions:\n",message)
print("\nRight Click action completed")

#======================================Drag and Drop=====================================
"""a.get("https://codepen.io/Goldfsh/pen/zBbOqm")
source=a.find_element_by_xpath("//*[@id='p1']")
target=a.find_element_by_xpath("//*[@id='dz1']")

actions=ActionChains(a)
actions.drag_and_drop(source,target).perform()
time.sleep(2)
w=a.find_element_by_xpath("//*[@id='p1']").text
print(w,"is moved")"""

print("Drag and Drop action performed")

a.quit()