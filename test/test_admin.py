import time
from re import search

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pages.Adminpage import Adminpage
from pages.Loginpage import Loginpage
#from pages.Adminpage import Adminpage

from utility.ExcelUtility import ExcelUtility


class TestAdmin:
    def test_return_to_home(self,browser_instance):
        self.driver = browser_instance
        excelUtility = ExcelUtility()
        usernamevalue2 = excelUtility.read_user_data(2, 1)
        passwordvalue2 = excelUtility.read_user_data(2, 2)
        self.driver.get("https://groceryapp.uniqassosiates.com/admin/login")
        #self.driver.find_element(By.XPATH, "//input[@name='username']").send_keys(usernamevalue2)
        #self.driver.find_element(By.XPATH, "//input[@name='password']").send_keys(passwordvalue2)
        #self.driver.find_element(By.XPATH, "//button[@type='submit']").click()

        loginpage = Loginpage(self.driver)  #object create for class Loginpage
        loginpage.enter_username(usernamevalue2).enter_password(passwordvalue2)
        #loginpage.enter_password(passwordvalue2)
        homepagechain=loginpage.signin(self.driver)     #return homepage
        print("test_return_to_home")
        from pages.Homepage import Homepage
        adminpagechain=homepagechain.list_admin(self.driver)    #moved list_admin to test_home.py
        print("moves to admin page")
        #adminpage = Adminpage(self.driver)
        #adminpagechain=adminpage.list_admin(self.driver)

        adminpagechain.home(self.driver)

        #self.driver.find_element(By.XPATH, "//a[@href='https://groceryapp.uniqassosiates.com/admin/list-admin' and @class='small-box-footer']").click()
        #self.driver.find_element(By.XPATH,"//a[text()='Home']").click()
        #//a[@href='https://groceryapp.uniqassosiates.com/admin/home' and text()='Home']
        # assert
        nav=self.driver.current_url
        assert nav == "https://groceryapp.uniqassosiates.com/admin/home"


    def test_create_user(self,browser_instance):
        self.driver = browser_instance

        excelUtility = ExcelUtility()
        usernamevalue2 = excelUtility.read_user_data(2, 1)
        passwordvalue2 = excelUtility.read_user_data(2, 2)
        self.driver.get("https://groceryapp.uniqassosiates.com/admin/login")
       #self.driver.find_element(By.XPATH, "//input[@name='username']").send_keys(usernamevalue2)
        #self.driver.find_element(By.XPATH, "//input[@name='password']").send_keys(passwordvalue2)
        #self.driver.find_element(By.XPATH, "//button[@type='submit']").click()

        loginpage = Loginpage(self.driver)  #object create for class Loginpage
        loginpage.enter_username(usernamevalue2).enter_password(passwordvalue2)
        #loginpage.enter_password(passwordvalue2)
        homepagechain=loginpage.signin(self.driver)
        time.sleep(2)
        print("test_create_user")
        adminpagechain=homepagechain.list_admin(self.driver).newbutton(self.driver).inputusername(self.driver).inputpassword(self.driver)

        #adminpagechain = Adminpage(self.driver)
        #time.sleep(2)

        #adminpagechain=adminpage.list_admin(self.driver)
        #adminpagechain.newbutton(self.driver)
        #self.driver.find_element(By.XPATH, "//a[@href='https://groceryapp.uniqassosiates.com/admin/list-admin' and @class='small-box-footer']").click()
        #self.driver.find_element(By.XPATH,"//a[@class='btn btn-rounded btn-danger']").click()

        #adminpagechain.inputusername(self.driver)
        #adminpagechain.inputpassword(self.driver)
        #self.driver.find_element(By.XPATH,"//input[@id = 'username']").send_keys("Jollyjkj")
        #self.driver.find_element(By.XPATH,"//input[@id = 'password']").send_keys("Jollyjkj")
        #dropdownlist=self.driver.find_element(By.XPATH,"//select[@id='user_type']")
        #select = Select(dropdownlist)
        #select.select_by_visible_text("Staff")
        adminpagechain.dropdown(self.driver).createAdmin(self.driver)
        #self.driver.find_element(By.XPATH,"//button[@name='Create']").click()
        #adminpagechain.createAdmin(self.driver)
        # assert
        time.sleep(2)
        alert_message=self.driver.find_elements(By.XPATH, "//div[@class='alert alert-success alert-dismissible']")
        time.sleep(2)
        alert_message1=self.driver.find_elements(By.XPATH, "//div[@class='alert alert-danger alert-dismissible']")
        #assert "User Created Successfully" in alert_message.text
        assert (
                (alert_message and "User Created Successfully" in alert_message[0].text)
                or (alert_message1 and "Username already exists." in alert_message1[0].text)
        )
        #assert alert_message.is_displayed()
    def test_reset(self,browser_instance):
        self.driver = browser_instance
        excelUtility = ExcelUtility()
        usernamevalue2 = excelUtility.read_user_data(2, 1)
        passwordvalue2 = excelUtility.read_user_data(2, 2)
        self.driver.get("https://groceryapp.uniqassosiates.com/admin/login")
        loginpage = Loginpage(self.driver)  # object create for class Loginpage

        loginpage.enter_username(usernamevalue2).enter_password(passwordvalue2)
        #loginpage.enter_username(usernamevalue2)
        #loginpage.enter_password(passwordvalue2)
        homepagechain =loginpage.signin(self.driver)

        #self.driver.find_element(By.XPATH, "//input[@name='username']").send_keys(usernamevalue2)
        #self.driver.find_element(By.XPATH, "//input[@name='password']").send_keys(passwordvalue2)
        #self.driver.find_element(By.XPATH, "//button[@type='submit']").click()

        print("test_reset")
        #self.driver.find_element(By.XPATH, "//a[@href='https://groceryapp.uniqassosiates.com/admin/list-admin' and @class='small-box-footer']").click()
        #self.driver.find_element(By.XPATH,"//a[@class='btn btn-rounded btn-danger']").click()
        adminpagechain = homepagechain.list_admin(self.driver).newbutton(self.driver).resetAdmin(self.driver)
        #adminpage = Adminpage(self.driver)
       # time.sleep(4)
        #adminpagechain=adminpage.list_admin(self.driver)
        #adminpagechain.newbutton(self.driver)
        #adminpagechain.resetAdmin(self.driver)
        #self.driver.find_element(By.XPATH,"//a[text() = ' Reset']").click()

        print("test_reset done")
        # assert
        nav=self.driver.current_url
        assert nav == "https://groceryapp.uniqassosiates.com/admin/list-admin"


    def test_search(self, cross_browser):
        self.driver = cross_browser
        excelUtility = ExcelUtility()
        usernamevalue2 = excelUtility.read_user_data(2, 1)
        passwordvalue2 = excelUtility.read_user_data(2, 2)
        self.driver.get("https://groceryapp.uniqassosiates.com/admin/login")
        #self.driver.find_element(By.XPATH, "//input[@name='username']").send_keys(usernamevalue2)
        #self.driver.find_element(By.XPATH, "//input[@name='password']").send_keys(passwordvalue2)
        #self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        loginpage = Loginpage(self.driver)  # object create for class Loginpage
        loginpage.enter_username(usernamevalue2).enter_password(passwordvalue2)
        #loginpage.enter_password(passwordvalue2)
        homepagechain=loginpage.signin(self.driver)
        print("test_reset homepage")
        #adminpage = Adminpage(self.driver)

        adminpagechain=homepagechain.list_admin(self.driver).newbutton(self.driver).resetAdmin(self.driver).searchAdmin(self.driver).inputtext(self.driver).utdropdownlist(self.driver).search(self.driver)
        #adminpage.newbutton(self.driver)
        #adminpage.resetAdmin(self.driver)
        #self.driver.find_element(By.XPATH, "//a[@href='https://groceryapp.uniqassosiates.com/admin/list-admin' and @class='small-box-footer']").click()
        #self.driver.find_element(By.XPATH,"//a[@class='btn btn-rounded btn-danger']").click()
        #self.driver.find_element(By.XPATH,"//a[text() = ' Reset']").click()
        print("test_reset admin page")
        #self.driver.find_element(By.XPATH, "//a[text() = ' Search']").click()
        #self.driver.find_element(By.XPATH, "//input[@type = 'text']").send_keys("Jolly")
        #search_dropdown_list=self.driver.find_element(By.XPATH,"//select[@id='ut']")
        #select=Select(search_dropdown_list)
        #select.select_by_visible_text("Staff")
        #self.driver.find_element(By.XPATH, "//button[@type= 'submit' and @value='sr' and @name='Search']").click()
        #adminpage.searchAdmin(self.driver)
        #adminpage.inputtext(self.driver)
        #adminpage.utdropdownlist(self.driver)
        #adminpage.search(self.driver)

        print("test_search_assert start")
        #assert
        #news_table = self.driver.find_element(By.XPATH, "//table[@class ='table table-bordered table-hover table-sm']")
        #assert "Jolly" in news_table.text

        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC

        wait = WebDriverWait(self.driver, 15)

        news_table = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//table[@class='table table-bordered table-hover table-sm']")
            )
        )

        assert "Jolly" in news_table.text









