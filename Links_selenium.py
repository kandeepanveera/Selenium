"""

How many links present
Capture all the link in webpage
print all weblink and clicking the link

"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

a=webdriver.Chrome("chromedriver.exe")
a.get("http://magento-demo.lexiconn.com/")
a.find_element(By.ID,"search").send_keys("bed and bath")
a.find_element_by_xpath("//button[@class='button search-button']").click()

links=a.find_elements(By.TAG_NAME,"a")
print(len(links))
#printing the all the links
for link in links:
    print(link.text)
#clecking the link
a.find_element(By.XPATH,"//*[@id='top']/body/div/div[2]/div[2]/div/div[2]/div[2]/div[3]/ul/li[1]/div/h2/a").click()


time.sleep(5)
a.quit()