"""
Screen shot
-save_screenshot('filename')
-get_screenshot_as_file('filename')

"""

from selenium import webdriver
a=webdriver.Chrome("chromedriver.exe")

a.get("http://newtours.demoaut.com/")
#one method
#a.save_screenshot("C:\\Users\kandeepx\Pictures\Camera Roll\home.png")
#second method
a.get_screenshot_as_file("C:\\Users\kandeepx\Pictures\Camera Roll\second.png")
a.quit()