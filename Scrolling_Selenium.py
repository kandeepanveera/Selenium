"""
Scrolling:
3 methods available
*based on pixel
driver.execute_script("window.scrollBy(0,500)",")
*based on elements
driver.execute_script("arguments[0].scrollintoView();",Element)
*based on till last page
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")

"""

from selenium import webdriver
import time
driver=webdriver.Chrome("chromedriver.exe")
driver.get("https://truweight.in/blog/food-and-nutrition/millet-weight-loss-recipes-health-benefits-side-effects.html")
driver.maximize_window()
time.sleep(3)
#1.scroll down page by pixcel
#driver.execute_script("window.scrollBy(0,1000)","")

#2.scroll down the page by elements
#ragi=driver.find_element_by_xpath("//*[@id='post-4774']/div[3]/h4[2]/span")
#driver.execute_script("arguments[0].scrollIntoView();",ragi)

#3.scroll down page by till end
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
time.sleep(5)
driver.quit()