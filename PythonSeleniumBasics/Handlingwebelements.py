from selenium.webdriver.common.by import By

from PythonSeleniumBasics.BasicsSelenium11 import BasicsSelenium11


class handlingwebelements(BasicsSelenium11):
    def verify_web_element_commands(self):
        self.driver.get("https://selenium.qabible.in/simple-form-demo.php")
        messagebox=self.driver.find_element(By.XPATH,"//input[@id='single-input-field']")
        messagebox.send_keys("Hello World")
        self.driver.find_element(By.XPATH,"//button[@id='button-one']").click()
        message_print=self.driver.find_element(By.XPATH,"//div[@id='message-one']")
        #print(message_print.is_displayed())
        print(message_print.text)
        print(message_print.is_displayed())   #by default its false, when element present, its true.
        print(message_print.is_enabled())    #by default its false, when element enabled its true.
        messagebox.clear()


obj1 = handlingwebelements()
obj1.initialize_browser()
obj1.verify_web_element_commands()



