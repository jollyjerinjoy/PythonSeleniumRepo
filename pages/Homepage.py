from selenium.webdriver.common.by import By
from utility.WaitUtility import WaitUtility
from utility.page_utility import Page_Utility


class Homepage:
    def __init__(self,driver):   #invoke driver
        self.driver = driver  #assigning to class object, fectching driver value and assigining the self.driver object
        self.waitutility = WaitUtility()
        self.pageutility = Page_Utility()
    def signin(self,driver):
        pageutility_signin=self.driver.find_element(By.XPATH, "//a[@href='https://groceryapp.uniqassosiates.com/admin/list-admin' and @class='small-box-footer']") #.click()
        self.pageutility.click_on_element(pageutility_signin)
    def Home(self,driver):
        #self.driver.find_element(By.XPATH,"//a[text()='Home']").click()
        pageutility_Home=self.driver.find_element(By.XPATH, "//a[text()='Home']")  #.click()
        self.pageutility.click_on_element(pageutility_Home)
    def nav_item_dropdown(self,driver):
        pageutility_nav_item_dropdown=self.driver.find_element(By.XPATH, "//li[@class='nav-item dropdown']")    #.click()
        self.pageutility.click_on_element(pageutility_nav_item_dropdown)
    def sign_out(self,driver):
        pageutility_sign_outclick=self.driver.find_element(By.XPATH, "//a[@href='https://groceryapp.uniqassosiates.com/admin/logout']")
        self.waitutility.wait_until_clickable(self.driver, pageutility_sign_outclick)
        pageutility_sign_outclick.click()
        #//a/i[@class='ace-icon fa fa-power-off']
