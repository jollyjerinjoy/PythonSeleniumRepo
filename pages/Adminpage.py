import random
import string

from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v140.target import send_message_to_target
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from pages.Homepage import Homepage
from utility.WaitUtility import WaitUtility
from utility.page_utility import Page_Utility

def generate_random_username():
    return "user_" + ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))

class Adminpage:
        def __init__(self, driver):  # invoke driver
            self.driver = driver
            self.waitutility = WaitUtility()
            self.pageutility = Page_Utility()
        def list_admin(self,driver):
            pageutility_list_admin=self.driver.find_element(By.XPATH, "//a[@href='https://groceryapp.uniqassosiates.com/admin/list-admin' and @class='small-box-footer']")   #.click()
            self.pageutility.click_on_element(pageutility_list_admin)
            return Adminpage(self.driver)
        def home(self,driver):
            pageutility_home=self.driver.find_element(By.XPATH,"//a[text()='Home']")   #.click()
            self.pageutility.click_on_element(pageutility_home)
            return Homepage(self.driver)
        def newbutton(self,driver):
            #self.driver.find_element(By.XPATH,"//a[@onclick='click_button(1)']").click()
            pageutility_newbutton=self.driver.find_element(By.XPATH,"//a[@onclick='click_button(1)']")
            self.pageutility.click_on_element(pageutility_newbutton)
            return self
        def inputusername(self,text):
            #self.driver.find_element(By.XPATH, "//input[@id = 'username']").send_keys("Jollyjkj23")
            pageutilty_inputusername=self.driver.find_element(By.XPATH, "//input[@id = 'username']")
            self.pageutility.send_data_to_element(pageutilty_inputusername,generate_random_username())
            return self
        def inputpassword(self,text):
            pageutilty_inputpassword=self.driver.find_element(By.XPATH, "//input[@id = 'password']")  #.send_keys("Jollyjkj23")
            self.pageutility.send_data_to_element(pageutilty_inputpassword,"Jollyjkj27")
            return self
        def dropdown(self,driver):
            pageutilty_dropdownlist = self.driver.find_element(By.XPATH, "//select[@id='user_type']")
            #select = Select(pageutilty_dropdownlist)
            #select.select_by_visible_text("Staff")
            self.pageutility.select_by_visible_text(pageutilty_dropdownlist,"Staff")
            return self
        def createAdmin(self, driver):
            pageutilty_createAdmin=self.driver.find_element(By.XPATH,"//button[@name='Create']")  #.click()
            self.pageutility.click_on_element(pageutilty_createAdmin)
            return self
        def resetAdmin(self,driver):
            pageutilty_resetAdmin=self.driver.find_element(By.XPATH, "//a[text() = ' Reset']")   #.click()
            self.pageutility.click_on_element(pageutilty_resetAdmin)
            return self
        def searchAdmin(self, driver):
            pageutilty_searchAdmin=self.driver.find_element(By.XPATH, "//a[text() = ' Search']")   #.click()
            self.pageutility.click_on_element(pageutilty_searchAdmin)
            return self

        def inputtext(self,text):
            #self.driver.find_element(By.XPATH, "//input[@type = 'text']").send_keys("Jolly")
            pageutility_inputtext=self.driver.find_element(By.XPATH, "//input[@type = 'text']")
            self.pageutility.send_data_to_element(pageutility_inputtext,"jolly")
            return self
        def utdropdownlist(self,driver):
            #search_dropdown_list = self.driver.find_element(By.XPATH, "//select[@id='ut']")
            #select = Select(search_dropdown_list)
            #select.select_by_visible_text("Staff")
            pageutility_utdropdownlist=self.driver.find_element(By.XPATH, "//select[@id='ut']")
            #select = Select(pageutility_utdropdownlist)
            self.pageutility.select_by_visible_text(pageutility_utdropdownlist,"Staff")
            return self
        def search(self,driver):
            #searchclick=self.driver.find_element(By.XPATH, "//button[@type= 'submit' and @value='sr' and @name='Search']")
            #self.waitutility.wait_until_clickable(self.driver, searchclick)
            #searchclick.click()
            pageutility_searchclick=self.driver.find_element(By.XPATH, "//button[@type= 'submit' and @value='sr' and @name='Search']")
            self.waitutility.wait_until_clickable(self.driver, pageutility_searchclick)
            self.pageutility.click_on_element(pageutility_searchclick)
            return self