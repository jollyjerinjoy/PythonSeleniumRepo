from selenium import webdriver
class BasicsSelenium:
    def __init__(self):
        self.driver = None
    def initialiseBrowser(self):
        self.driver = webdriver.Chrome
        self.driver.get("https://selenium.qabible.in/")
        self.driver.maximize_window()
        title=self.driver.title
        print(title)
        url=self.driver.current_url
        print(url)
        handleID=self.driver.current_window_handle
        print(handleID)
    def closeBrowser(self):
        #self.driver.close()
        self.driver.quit()
if __name__ == "__main__":
    base = BasicsSelenium()
    base.initialiseBrowser()
    base.closeBrowser()