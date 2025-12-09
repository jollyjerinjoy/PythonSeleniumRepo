import time
from time import sleep

import pytest
from selenium.webdriver.common.by import By

from pages.Homepage import Homepage
from pages.Loginpage import Loginpage
from test.conftest import cross_browser
from utility.ExcelUtility import ExcelUtility

class Testhome:
    @pytest.mark.timeout(30)
    def test_logout(self,cross_browser):
        # assigned to variable(driver) which hold instance of driver in browser_instance( created in conftest)
        self.driver=cross_browser  #cross browser - one after another tests executed, written fixture in conftest

        excelUtility = ExcelUtility()
        #usernamevalue2=excelUtility.read_user_data(2,1)
        #passwordvalue2 = excelUtility.read_user_data(2, 2)
        usernamevalue2=excelUtility.read_user_data(2,1)
        passwordvalue2 = excelUtility.read_user_data(2, 2)
        self.driver.get("https://groceryapp.uniqassosiates.com/admin/login")
        #self.driver.find_element(By.XPATH,"//input[@name='username']").send_keys(usernamevalue2)
        #self.driver.find_element(By.XPATH, "//input[@name='password']").send_keys(passwordvalue2)
        #self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        loginpage = Loginpage(self.driver)  #object create for class Loginpage
        loginpage.enter_username(usernamevalue2)
        loginpage.enter_password(passwordvalue2)
        loginpage.signin(self.driver)
        print("test_logout")
        time.sleep(2)
        homepage = Homepage(self.driver)
        time.sleep(2)
        homepage.nav_item_dropdown(self.driver)
        homepage.sign_out(self.driver)

        #self.driver.find_element(By.XPATH,"//li[@class='nav-item dropdown']").click()
        #self.driver.find_element(By.XPATH,"//a[@href='https://groceryapp.uniqassosiates.com/admin/logout']").click()
        # assert
        nav_url=self.driver.current_url
        assert nav_url == "https://groceryapp.uniqassosiates.com/admin/login"

