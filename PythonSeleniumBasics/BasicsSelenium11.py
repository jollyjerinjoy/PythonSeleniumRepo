from selenium import webdriver

from PythonSelenium.BasicsSelenium import BasicsSelenium


#Parent class
class BasicsSelenium11:
    def __init__(self):
        self.driver = None
    def initialize_browser(self):
        #self.driver=webdriver.Chrome()
        self.driver=webdriver.Firefox()
        self.driver.get("https://selenium.qabible.in/")
        self.driver.maximize_window()
    def close_browser(self):
        self.driver.close()
        #self.driver.quit()


if __name__ =="__main__":
    base = BasicsSelenium11()
    base.initialize_browser()
    base.close_browser()