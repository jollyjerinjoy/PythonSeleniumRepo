from selenium import webdriver
from selenium.webdriver.common.by import By


class QAbible:
    def __init__(self):
        self.driver=None
    def Open_browser(self):
        self.driver=webdriver.Firefox()
        self.driver.get("https://selenium.qabible.in/")
        self.driver.maximize_window()
    def Single_input(self):
        #self.driver.find_element(By.LINK_TEXT,"Input Form").click()
        # //a[@href='index.php']
        self.driver.get("https://selenium.qabible.in/simple-form-demo.php")
        self.driver.find_element(By.ID,"single-input-field").send_keys("welcome")
        self.driver.find_element(By.XPATH,"//button[@id='button-one']").click()
        self.driver.find_element(By.XPATH,"//input[@id='value-a']").send_keys(1)
        self.driver.find_element(By.XPATH,"//input[@id='value-b']").send_keys(2)
        value=self.driver.find_element(By.XPATH,"//button[@id='button-two']")
        value.click()
        print(value.text)
        #value1=// div[ @ id = 'message-two']



    def Close_Browser(self):
        self.driver.close()
    def Quit_Browser(self):
        self.driver.quit()

if __name__ == '__main__':
   a=QAbible()
   a.Open_browser()
   a.Single_input()
   a.Close_Browser()
   a.Quit_Browser()

