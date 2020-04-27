"""

title_is
title_contains
presence_of_element_located
visibility_of_element_located
visibility_of
presence_of_all_elements_located
text_to_be_present_in_element
text_to_be_present_in_element_value
frame_to_be_available_and_switch_to_it
invisibility_of_element_located
element_to_be_clickable
staleness_of
element_to_be_selected
element_located_to_be_selected
element_selection_state_to_be
element_located_selection_state_to_be
alert_is_present
"""

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


a=webdriver.Chrome("chromedriver.exe")
a.get("https://www.expedia.com/")
a.maximize_window()

a.find_element(By.ID,"tab-flight-tab-hp").click()
a.implicitly_wait(2)

a.find_element(By.ID,"flight-origin-hp-flight").send_keys("BLR")
time.sleep(1)
a.find_element(By.ID,"flight-destination-hp-flight").send_keys("MAA")
time.sleep(1)
a.find_element(By.ID,"flight-departing-hp-flight").clear()
a.find_element(By.ID,"flight-departing-hp-flight").send_keys("1/13/2020")
f=a.find_element(By.ID,"flight-returning-hp-flight")
f.clear()
time.sleep(3)
f.send_keys("1/15/2020")
a.find_element(By.XPATH,"//*[@id='gcw-flights-form-hp-flight']/div[7]/label/button").click()

#Explicit Waits
wait=WebDriverWait(a,10)
element=wait.until(EC.element_to_be_clickable((By.ID,"stopFilter_stops-1")))
element.click()

time.sleep(5)
a.quit()


