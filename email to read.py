import time
from selenium import webdriver
import re
from selenium.webdriver.support.ui import WebDriverWait

d=webdriver.Chrome()
d.get('https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin')
elem1=d.find_element_by_id('username')
elem1.send_keys("kandeepan.ece1@gmail.com")

elem2=d.find_element_by_id('password')
elem2.send_keys("Deepshika@123")

doc=d.page_source

emails=re.findall(r'[\w\.-]+@[\w\.-]',doc)

for email in emails():
    print(email)
