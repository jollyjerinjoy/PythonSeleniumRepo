import time

from selenium.webdriver.common.by import By

from PythonSeleniumBasics.BasicsSelenium11 import BasicsSelenium11


class Executor(BasicsSelenium11):
    def verify_javascript_executor(self):
        self.driver.get("https://selenium.qabible.in/simple-form-demo.php")
        # Locate the button with XPath
        show_message_button = self.driver.find_element(By.XPATH, "//button[@id='button-one']")

        # JavaScript Executor(builtin) for clicking the button- integrating javascript in python
        self.driver.execute_script("arguments[0].click();", show_message_button)

        # Scroll down by 200px. Relative scrolling
        self.driver.execute_script("window.scrollBy(0, 200);")
        # Scroll up by 350px
        self.driver.execute_script("window.scrollBy(0, -350);")

        # 4. Scroll to the end using `scrollTo()` Absolute scrolling
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(10)
        self.driver.execute_script("window.scrollTo(0, 0);")
executor = Executor()
executor.initialize_browser()
executor.verify_javascript_executor()