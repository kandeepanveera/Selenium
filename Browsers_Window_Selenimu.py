"""

-driver.current_window_handle
-driver.window_handles
(every window having unique value)
(will provide the all window value)

"""

from selenium import webdriver
import time
from selenium.webdriver.common.by import By

a=webdriver.Chrome("chromedriver.exe")
a.get("http://demo.automationtesting.in/Windows.html")
a.find_element_by_xpath("//*[@id='Tabbed']/a/button").click()
print(a.current_window_handle)# which will provide the current window value "CDwindow-40FFC3991D725008D0A28E69F5F4B10F"

hand=a.window_handles
for handles in hand:
    a.switch_to_window(handles)
    print(a.title)
    if a.title=="Frames & windows":
        a.close()

time.sleep(3)
a.quit()