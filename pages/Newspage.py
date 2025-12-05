from selenium.webdriver.common.by import By

from utility.WaitUtility import WaitUtility


class NewsPage:
    def __init__(self,driver):
        self.driver = driver
        self.waitutility = WaitUtility()
    def newslist(self,driver):
        self.driver.find_element(By.XPATH, "//a[@href='https://groceryapp.uniqassosiates.com/admin/list-news']").click()
    def newsnewbutton(self,driver):
        self.driver.find_element(By.XPATH, "//a[@class='btn btn-rounded btn-danger']").click()
    def newsaddtestarea(self,text):
        self.driver.find_element(By.XPATH, "//textarea[@name='news']").send_keys("Rainingss1")
    def newscreate(self,driver):
        self.driver.find_element(By.XPATH, "// button[ @ name = 'create']").click()
    def newssearch1(self,driver):
        self.driver.find_element(By.XPATH, "//a[@onclick='click_button(2)']").click()
    def newsSearchManage(self,text):
        #self.driver.find_element(By.XPATH, "//input[@name='un']").send_keys("Rainingss1")
        self.driver.find_element(By.XPATH, "//input[@type='text']").send_keys("Rainingss1")
    def newssearch(self,driver):
        newssearchclick=self.driver.find_element(By.XPATH, "// button[ @ name = 'Search1']")
        self.waitutility.wait_until_clickable1(self.driver, newssearchclick)
        newssearchclick.click()