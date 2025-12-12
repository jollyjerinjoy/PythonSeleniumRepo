from selenium.webdriver.common.by import By

from utility.WaitUtility import WaitUtility
from utility.page_utility import Page_Utility


class NewsPage:
    def __init__(self,driver):
        self.driver = driver
        self.waitutility = WaitUtility()
        self.pageutility = Page_Utility()

    def newsnewbutton(self,driver):
        pageutility_newsnewbutton=self.driver.find_element(By.XPATH, "//a[@class='btn btn-rounded btn-danger']")
        self.pageutility.click_on_element(pageutility_newsnewbutton)
        # pageutility_newsnewbutton.click()
        return self
    def newsaddtestarea(self,text):
        #self.driver.find_element(By.XPATH, "//textarea[@name='news']").send_keys("Rainingss1")
        pageutility_newsaddtestarea=self.driver.find_element(By.XPATH, "//textarea[@name='news']")
        self.pageutility.send_data_to_element(pageutility_newsaddtestarea, "Rainingss1")
        return self
    def newscreate(self,driver):
        pageutility_newscreate=self.driver.find_element(By.XPATH, "//button[@name='create']")
        self.pageutility.click_on_element(pageutility_newscreate)
        #pageutility_newscreate.click()
        return self
    def newssearch1(self,driver):
        pageutility_newssearch1=self.driver.find_element(By.XPATH, "//a[@onclick='click_button(2)']")
        self.pageutility.click_on_element(pageutility_newssearch1)
        #pageutility_newssearch1.click()
        return self
    def newsSearchManage(self,text):
        #self.driver.find_element(By.XPATH, "//input[@name='un']").send_keys("Rainingss1")
        utilitynewsSearchManage=self.driver.find_element(By.XPATH, "//input[@type='text']") #.send_keys("Rainingss1")
        self.pageutility.send_data_to_element(utilitynewsSearchManage, "Rainingss1")
        #utilitynewsSearchManage.click()
        return self
    def newssearch(self,driver):
        newssearchclick=self.driver.find_element(By.XPATH, "// button[ @ name = 'Search']")
        self.waitutility.wait_until_clickable1(self.driver, newssearchclick)
        self.pageutility.click_on_element(newssearchclick)
        #newssearchclick.click()
        return self