"""
Select Any drop down from option
Find out how many options exist in drop down
count how many option present
capture option from drop down and print them
"""
from selenium import webdriver
import time
#select class need to import
from selenium.webdriver.support.ui import Select


a=webdriver.Chrome("chromedriver.exe")
a.get("https://fs2.formsite.com/R1Tuim/form1/index.html")

element=a.find_element_by_id("RESULT_RadioButton-6")
drop=Select(element)
drop.select_by_visible_text("M")# Option will selected by visible text

#drop.select_by_value("Radio-1")#option will be selected by Value
#drop.select_by_index("2")#option will be selected by index valu



#count the number of option
print(len(drop.options))

#capture all the option and print the items
all_option=drop.options
for option in all_option:
    print(option.text)

time.sleep(5)
a.quit()