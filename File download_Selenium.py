from selenium import webdriver

a=webdriver.Chrome("chromedriver.exe")
a.get("https://www.thinkbroadband.com/download")

a.maximize_window()

a.find_element_by_xpath("//*[@id='main-col']/div/div/div[8]/p[1]/a/img").click()
a.quit()
