"""
1)slected or not =isselected()

"""


import time
from selenium import webdriver
from selenium.webdriver.common.by import By
a=webdriver.Chrome("chromedriver.exe")
a.get("https://www.nobroker.in/property/rent/bangalore/Jeevan%20Bima%20Nagar?searchParam=W3sibGF0IjoxMi45NjQxNjMsImxvbiI6NzcuNjU4MDc2LCJwbGFjZUlkIjoiQ2hJSlM3NDZtUDRUcmpzUjdKWmNQenRrdFJBIiwicGxhY2VOYW1lIjoiSmVldmFuIEJpbWEgTmFnYXIifV0=&radius=2.0&sharedAccomodation=0")
selection_rent=a.find_element_by_id("selectedLocality0")

print("Locations:-",selection_rent.text)

w=a.find_element_by_id("WITHIN_15_DAYS").is_selected()
print("With in 15 days selected:-",w)
r=a.find_elements(By.CLASS_NAME,"fbsearch")
print(len(r))

for r in len(r):
    print(r)



a.quit()
