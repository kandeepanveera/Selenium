from selenium import webdriver

a=webdriver.Chrome("chromedriver.exe")
a.get("https://www.toolsqa.com/automation-practice-table/")
rows=len(a.find_elements_by_xpath("//*[@id='content']/table/tbody/tr"))
cols=len(a.find_elements_by_xpath("//*[@id='content']/table/thead/tr/th"))
print(rows)
print(cols)

print("Structure"+"   "+"Country"+"    "+"City"+"    "+"Height"+"    "+"Built"+"    "+"Rank"+"    "+"Details")
for r in range(2,rows+1):
    for c in range(1,cols+1):
        value=a.find_element_by_xpath("//*[@id='content']/table/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
        print(value,end="   ")
    print()
a.quit()