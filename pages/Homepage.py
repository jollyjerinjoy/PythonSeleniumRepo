from selenium.webdriver.common.by import By


class Homepage:
    def __init__(self,driver):   #invoke driver
        self.driver = driver     #assigning to class object, fectching driver value and assigining the self.driver object
    def signin(self,driver):
        self.driver.find_element(By.XPATH, "//a[@href='https://groceryapp.uniqassosiates.com/admin/list-admin' and @class='small-box-footer']").click()
    def Home(self,driver):
        self.driver.find_element(By.XPATH,"//a[text()='Home']").click()
    def nav_item_dropdown(self,driver):
        self.driver.find_element(By.XPATH, "//li[@class='nav-item dropdown']").click()
    def sign_out(self,driver):
        self.driver.find_element(By.XPATH, "//a[@href='https://groceryapp.uniqassosiates.com/admin/logout']").click()