import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

x=webdriver.Chrome('chromedriver.exe')
x.get("https://www.limeroad.com/") # opening Google page
x.maximize_window()
#time.sleep(5) #Browser will wait for 5 sec's
print(x.title) #returns web page title
print(x.current_url) #returns current url page

elem=x.find_element_by_id("shopMen").click()

#elem1=x.find_element_by_xpath("//*[@id='m']/div/div[3]/div[1]/div[1]/div[2]")

time.sleep(3)
x.close() # this command will close the parent window not full browser(x.quit()==> will close the whole browser)