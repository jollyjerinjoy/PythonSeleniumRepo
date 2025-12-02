from selenium import webdriver
class BasicsSelenium:
    def __init__(self):
        self.driver = None
    def initialiseBrowserfunction(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://selenium.qabible.in/")
        self.driver.maximize_window()
if __name__ == "__main__":
    base = BasicsSelenium()
    base.initialiseBrowserfunction()