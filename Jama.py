from selenium import webdriver

from selenium.webdriver.common.by import By
import unittest
class website_testing(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome("chromedriver.exe")
        cls.driver.maximize_window()
        cls.driver.get("https://jama4.intel.com/perspective.req#/testPlans/24952228/testRuns?projectId=309")

    def test_Title(self):
        print( "\n" )
        print(self.driver.title)
        self.assertEqual("Login - Jama Software", self.driver.title, "Wepage is wrong")

    def test_login(self):
        self.driver.find_element(By.ID,"j_username").send_keys("kandeepx")
        self.driver.find_element(By.ID,"j_password").send_keys("icelake@123")
        self.driver.find_element(By.ID,"loginButton").click()
        #self.driver.implicitly_wait(30)
        print( "\n" )
        print(self.driver.title)

        self.assertEqual("Jama Software", self.driver.title, "Webpage is wrong")

    def test_login2(self):
        self.driver.implicitly_wait(45)
        self.driver.find_element(By.XPATH,"//*[@id='ext-comp-1019-item-panel-testplan-testRuns-link']/div/div[2]").click()
        self.driver.implicitly_wait(30)
        ele3 = self.driver.find_element( By.ID, "ext-comp-1019-item-panel-testplan-testRuns-tests-passed-num" )
        ele4 = self.driver.find_element( By.ID, "ext-comp-1019-item-panel-testplan-testRuns-tests-failed-num" )
        ele5 = self.driver.find_element( By.ID, "ext-comp-1019-item-panel-testplan-testRuns-tests-blocked-num" )
        ele6 = self.driver.find_element( By.ID, "ext-comp-1019-item-panel-testplan-testRuns-tests-in-progress-num" )
        ele7 = self.driver.find_element( By.ID, "ext-comp-1019-item-panel-testplan-testRuns-tests-not-run-num" )
        ele8 = self.driver.find_element( By.ID, "ext-comp-1019-item-panel-testplan-testRuns-cycle-days-remaining-label" )
        print( "\nPassed Test cases:-", ele3.text )
        print( "Failed Test cases:-", ele4.text )
        print( "Blocked Test Cases:-", ele5.text )
        print( "Not Run Test Cases:-", ele7.text )
        print( "In Progress Test Cases:-", ele6.text )
        print( "No of Days Left to complete the BKC:-", ele8.text )

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        print("Test Case Completed....")

if __name__=="__main__":
    unittest.main(verbosity=2)

