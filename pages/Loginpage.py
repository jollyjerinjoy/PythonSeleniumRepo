from selenium.webdriver.common.by import By


#from pages.Homepage import Homepage
from utility.WaitUtility import WaitUtility
from utility.page_utility import Page_Utility


class Loginpage:
    def __init__(self,driver):
        self.driver=driver
        self.waitutility = WaitUtility()
        self.pageutility=Page_Utility()  #pageutiliycode
    def enter_username(self,usernamevalue2):
        utilityusername=(self.driver.find_element(By.XPATH,"//input[@name='username']"))
        #utilityusername.send_keys(usernamevalue2)
        self.pageutility.send_data_to_element(utilityusername,usernamevalue2) #pageutiliycode
        return self
    def enter_password(self,passwordvalue2):
        utilitypassword=self.driver.find_element(By.XPATH, "//input[@name='password']")
        #utilitypassword.send_keys(passwordvalue2)
        self.pageutility.send_data_to_element(utilitypassword,passwordvalue2)  #pageutiliycode
        return self
    def signin(self,driver):
        from pages.Homepage import Homepage
        utilitysignin=self.driver.find_element(By.XPATH, "//button[@type='submit']")
        self.waitutility.wait_until_clickable(self.driver,utilitysignin)
        self.pageutility.click_on_element(utilitysignin) #pageutiliycode
        #signin.click()
        return Homepage(self.driver)  #classname



