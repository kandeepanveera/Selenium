"""
how to find how many input boxes present in web page
how to provide """



import time

from selenium import webdriver
from selenium.webdriver.common.by import By
a=webdriver.Chrome("chromedriver.exe")
a.get("https://fs2.formsite.com/R1Tuim/form1/index.html")

a.maximize_window()

#How to find how many inputs present in page
f=a.find_elements(By.CLASS_NAME,'text_field')
print(len(f))
a.find_element_by_id("RESULT_TextField-4").send_keys("kandeepan")
a.find_element(By.ID,"RESULT_TextField-5").send_keys("veeraragavan")
#.find_element(By.ID,"RESULT_TextField-4").send_keys('12345678901')
a.quit()