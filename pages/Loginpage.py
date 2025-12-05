from selenium.webdriver.common.by import By

from utility.WaitUtility import WaitUtility


class Loginpage:
    def __init__(self,driver):
        self.driver=driver
        self.waitutility = WaitUtility()
    def enter_username(self,usernamevalue2):
        self.driver.find_element(By.XPATH,"//input[@name='username']").send_keys(usernamevalue2)
    def enter_password(self,passwordvalue2):
        self.driver.find_element(By.XPATH, "//input[@name='password']").send_keys(passwordvalue2)


    def signin(self,driver):
        signin=self.driver.find_element(By.XPATH, "//button[@type='submit']")
        self.waitutility.wait_until_clickable(self.driver,signin)
        signin.click()



