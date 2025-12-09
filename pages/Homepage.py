from selenium.webdriver.common.by import By
from utility.WaitUtility import WaitUtility
class Homepage:
    def __init__(self,driver):   #invoke driver
        self.driver = driver  #assigning to class object, fectching driver value and assigining the self.driver object
        self.waitutility = WaitUtility()
    def signin(self,driver):
        self.driver.find_element(By.XPATH, "//a[@href='https://groceryapp.uniqassosiates.com/admin/list-admin' and @class='small-box-footer']").click()
    def Home(self,driver):
        self.driver.find_element(By.XPATH,"//a[text()='Home']").click()
    def nav_item_dropdown(self,driver):
        self.driver.find_element(By.XPATH, "//li[@class='nav-item dropdown']").click()
    def sign_out(self,driver):
        sign_outclick=self.driver.find_element(By.XPATH, "//a[@href='https://groceryapp.uniqassosiates.com/admin/logout']")
        self.waitutility.wait_until_clickable(self.driver, sign_outclick)
        sign_outclick.click()
        #//a/i[@class='ace-icon fa fa-power-off']
