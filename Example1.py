import time
import selenium
from selenium import webdriver
d=webdriver.Chrome()
from selenium.webdriver.support.ui import WebDriverWait
d.get('https://www.flipkart.com/')
d.maximize_window()
elem1=d.find_element_by_xpath("//input[@placeholder='Search for products, brands and more']")
elem1.send_keys("oneplus mobiles\n")
lis=d.find_elements_by_id('_3wU53n')

print(str(len(lis)) +"found")

for i in lis:
    print(i.text)

time.sleep(5)
d.quit()


