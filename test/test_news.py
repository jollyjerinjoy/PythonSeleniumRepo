import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pages.Loginpage import Loginpage
from pages.Newspage import NewsPage
from utility.ExcelUtility import ExcelUtility
class Testnews:
    def test_create_news(self,browser_instance):
        self.driver = browser_instance
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

        newspage = NewsPage(self.driver)  # object create for class
        newspagechain=newspage.newslist(self.driver)
        newspagechain.newsnewbutton(self.driver).newsaddtestarea(self.driver).newscreate(self.driver)
        #newspage.newsnewbutton(self.driver)
        time.sleep(2)
        #newspage.newsaddtestarea(self.driver)
        time.sleep(2)
        #newspage.newscreate(self.driver)


        #self.driver.find_element(By.XPATH,"//a[@href='https://groceryapp.uniqassosiates.com/admin/list-news']").click()
        #self.driver.find_element(By.XPATH, "//a[@class='btn btn-rounded btn-danger']").click()
        #time.sleep(2)
        #self.driver.find_element(By.XPATH,"//textarea[@name='news']").send_keys("Rainingss1")
        #time.sleep(2)
        #self.driver.find_element(By.XPATH, "// button[ @ name = 'create']").click()
        # assert
        alert_message=self.driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissible']")
        time.sleep(2)
        #assert alert_message.text == "News Created Successfully"
        assert "News Created Successfully" in alert_message.text


    def test_search_news(self, browser_instance):
        self.driver = browser_instance
        excelUtility = ExcelUtility()
        usernamevalue2 = excelUtility.read_user_data(2, 1)
        passwordvalue2 = excelUtility.read_user_data(2, 2)
        self.driver.get("https://groceryapp.uniqassosiates.com/admin/login")
        loginpage = Loginpage(self.driver)  # object create for class Loginpage
        loginpage.enter_username(usernamevalue2).enter_password(passwordvalue2)
        #loginpage.enter_password(passwordvalue2)
        homepagechain=loginpage.signin(self.driver)

        #self.driver.find_element(By.XPATH, "//input[@name='username']").send_keys(usernamevalue2)
        #self.driver.find_element(By.XPATH, "//input[@name='password']").send_keys(passwordvalue2)
        #self.driver.find_element(By.XPATH, "//button[@type='submit']").click()

        #self.driver.find_element(By.XPATH,"//a[@href='https://groceryapp.uniqassosiates.com/admin/list-news']").click()
        #self.driver.find_element(By.XPATH, "//a[@class='btn btn-rounded btn-primary']").click()
        newspage = NewsPage(self.driver)  # object create for class
        newspagechain =newspage.newslist(self.driver).newssearch1(self.driver).newsSearchManage(self.driver).newssearch(self.driver)
        #newspage.newslist(self.driver)
        ##newspage.newsnewbutton(self.driver)
        time.sleep(2)
        #newspage.newssearch1(self.driver)
        #self.driver.find_element(By.XPATH, "//input[@name='un']").send_keys("Rainingss1")
        #time.sleep(2)
        #self.driver.find_element(By.XPATH, "// button[ @ name = 'Search']").click()
        #newspage.newsSearchManage(self.driver)
        time.sleep(2)
        #newspage.newssearch(self.driver)
        # assert
        news_table=self.driver.find_element(By.XPATH, "//table[@class ='table table-bordered table-hover table-sm']")
        assert "Rainingss1" in news_table.text


