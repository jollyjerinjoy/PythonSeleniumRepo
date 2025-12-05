from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from utility.WaitUtility import WaitUtility


class Adminpage:
        def __init__(self, driver):  # invoke driver
            self.driver = driver
            self.waitutility = WaitUtility()

        def list_admin(self,driver):
            self.driver.find_element(By.XPATH, "//a[@href='https://groceryapp.uniqassosiates.com/admin/list-admin' and @class='small-box-footer']").click()
        def home(self,driver):
            self.driver.find_element(By.XPATH,"//a[text()='Home']").click()
        def newbutton(self,driver):
            self.driver.find_element(By.XPATH,"//a[@onclick='click_button(1)']").click()
        def inputusername(self,text):
            self.driver.find_element(By.XPATH, "//input[@id = 'username']").send_keys("Jollyjkj23")
        def inputpassword(self,text):
            self.driver.find_element(By.XPATH, "//input[@id = 'password']").send_keys("Jollyjkj23")
        def dropdown(self,driver):
            dropdownlist = self.driver.find_element(By.XPATH, "//select[@id='user_type']")
            select = Select(dropdownlist)
            select.select_by_visible_text("Staff")
        def createAdmin(self, driver):
            self.driver.find_element(By.XPATH,"//button[@name='Create']").click()
        def resetAdmin(self,driver):
            self.driver.find_element(By.XPATH, "//a[text() = ' Reset']").click()
        def searchAdmin(self, driver):
            self.driver.find_element(By.XPATH, "//a[text() = ' Search']").click()
        def inputtext(self,text):
            self.driver.find_element(By.XPATH, "//input[@type = 'text']").send_keys("Jolly")
        def utdropdownlist(self,driver):
            search_dropdown_list = self.driver.find_element(By.XPATH, "//select[@id='ut']")
            select = Select(search_dropdown_list)
            select.select_by_visible_text("Staff")
        def search(self,driver):
            searchclick=self.driver.find_element(By.XPATH, "//button[@type= 'submit' and @value='sr' and @name='Search']")
            self.waitutility.wait_until_clickable(self.driver, searchclick)
            searchclick.click()