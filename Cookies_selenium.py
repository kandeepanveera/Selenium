"""
Capture all cookies from browser
count number of cookies
read all cookie pairs
adding new cookies
deleting specificcookieby using name of cookie
deleting the all cookies

"""

from selenium import webdriver
a=webdriver.Chrome("chromedriver.exe")
a.get("https://www.amazon.in")

#capture all cookies created by browser
cookies=a.get_cookies()
print(len(cookies)) #print number of cookies

print(cookies)# print all cookie pairs

a.quit()
