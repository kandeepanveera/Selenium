from selenium import webdriver
import time

from selenium.webdriver.common.by import By
list1=[]
a=webdriver.Chrome("chromedriver.exe")
a.get("https://webglsamples.org/fishtank/fishtank.html")
a.implicitly_wait(20)
ele1=a.find_element(By.XPATH,"//*[@id='setSetting3']").click()
ele2=a.find_element(By.ID,"fps")

for i in range(5):
    c = ele2.text
    list1.append(c)
    time.sleep(60)
print(list1)
time.sleep(5)
a.quit()


