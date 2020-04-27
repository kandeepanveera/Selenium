""" Wait commands=========================
-Implicit wait(10sec) ......applicable for all the elements ,it will work based on time
-Explicit wait ......it will work on condition based

Synchronisation issue will resolve with this commands

======================================="""
from selenium import webdriver

x=webdriver.Chrome("chromedriver.exe")
x.get("https://www.goibibo.com/bus/#home")

print(x.title)
assert "Bus ticket booking online, Book AC Volvo Bus Tickets at discounted prices - Goibibo" in x.title
x.implicitly_wait(5)
ele=x.find_element_by_id("gi_source").send_keys("Chennai, Tamil Nadu")

ele1=x.find_element_by_id("gi_destination").send_keys("Bangalore, Karnataka")

ele2=x.find_element_by_id("gi_search_btn").click()
ele3=x.find_elements_by_css_selector("[@class=width100 fl]")
print(ele3.index())


x.quit()
