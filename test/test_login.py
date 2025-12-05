import time

import pytest
from selenium.webdriver.common.by import By

from pages.Loginpage import Loginpage
from utility.ExcelUtility import ExcelUtility


class Testloginclass:
    @pytest.mark.run(order=1)
    def test_loginwithvalidcredentails(self,browser_instance):
        # assigned to variable(driver) which hold instance of driver in browser_instance( created in conftest)
        self.driver=browser_instance
        excelUtility = ExcelUtility()
        usernamevalue2=excelUtility.read_user_data(2,1)
        passwordvalue2 = excelUtility.read_user_data(2, 2)
        self.driver.get("https://groceryapp.uniqassosiates.com/admin/login")
        self.driver.implicitly_wait(5) #impicit wait


        #invoke
        #self.driver.find_element(By.XPATH,"//input[@name='username']").send_keys(usernamevalue2)
        #self.driver.find_element(By.XPATH, "//input[@name='password']").send_keys(passwordvalue2)
        loginpage = Loginpage(self.driver)  #object create for class Loginpage
        loginpage.enter_username(usernamevalue2)
        loginpage.enter_password(passwordvalue2)
        loginpage.signin(self.driver)

        # assert
        nav=self.driver.current_url
        assert nav == "https://groceryapp.uniqassosiates.com/admin"

    @pytest.mark.run(order=4)
    def test_logininvalidpassword(self,browser_instance):
        self.driver=browser_instance
        excelUtility = ExcelUtility()
        #usernamevalue3=excelUtility.read_user_data(3,1)
        #passwordvalue3 = excelUtility.read_user_data(3, 2)
        usernamevalue2=excelUtility.read_user_data(3,1)
        passwordvalue2 = excelUtility.read_user_data(3, 2)
        self.driver.get("https://groceryapp.uniqassosiates.com/admin/login")
        #self.driver.find_element(By.XPATH,"//input[@name='username']").send_keys(usernamevalue3)
        #self.driver.find_element(By.XPATH, "//input[@name='password']").send_keys(passwordvalue3)
        #self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        loginpage = Loginpage(self.driver)  #object create for class Loginpage
        loginpage.enter_username(usernamevalue2)
        loginpage.enter_password(passwordvalue2)
        loginpage.signin(self.driver)
        print("loginwithvalid credentails pwd")
        # assert
        nav=self.driver.current_url
        assert nav == "https://groceryapp.uniqassosiates.com/admin/login"
        #time.sleep(3)

    @pytest.mark.run(order=3)
    def test_logininvalidusername(self,browser_instance):
        self.driver=browser_instance
        excelUtility = ExcelUtility()
        #usernamevalue4=excelUtility.read_user_data(4,1)
        #passwordvalue4 = excelUtility.read_user_data(4, 2)
        usernamevalue2=excelUtility.read_user_data(4,1)
        passwordvalue2 = excelUtility.read_user_data(4, 2)
        self.driver.get("https://groceryapp.uniqassosiates.com/admin/login")
        #self.driver.find_element(By.XPATH,"//input[@name='username']").send_keys(usernamevalue4)
        #self.driver.find_element(By.XPATH, "//input[@name='password']").send_keys(passwordvalue4)
        #self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        loginpage = Loginpage(self.driver)  #object create for class Loginpage
        loginpage.enter_username(usernamevalue2)
        loginpage.enter_password(passwordvalue2)
        loginpage.signin(self.driver)
        print("loginwithvalidcredentails username")
        # assert
        nav=self.driver.current_url
        assert nav == "https://groceryapp.uniqassosiates.com/admin/login"

    @pytest.mark.run(order=2)
    def test_loginininvalidusernamepwd(self, browser_instance):
        self.driver=browser_instance
        excelUtility = ExcelUtility()
        #usernamevalue5=excelUtility.read_user_data(5,1)
        #passwordvalue5 = excelUtility.read_user_data(5, 2)
        usernamevalue2=excelUtility.read_user_data(5,1)   # write usage usernamevalue
        passwordvalue2 = excelUtility.read_user_data(5, 2) # write usage passwordvalue
        self.driver.get("https://groceryapp.uniqassosiates.com/admin/login")
        #self.driver.find_element(By.XPATH,"//input[@name='username']").send_keys(usernamevalue5)
        #self.driver.find_element(By.XPATH, "//input[@name='password']").send_keys(passwordvalue5)
        #self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        loginpage = Loginpage(self.driver)  #object create for class Loginpage
        loginpage.enter_username(usernamevalue2)
        loginpage.enter_password(passwordvalue2)
        loginpage.signin(self.driver)
        print("loginwithvalid credentails username pwd")
        # assert
        nav=self.driver.current_url
        assert nav == "https://groceryapp.uniqassosiates.com/admin/login"

