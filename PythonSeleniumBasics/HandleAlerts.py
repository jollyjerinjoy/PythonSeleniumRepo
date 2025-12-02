import time

from selenium.webdriver.common.by import By

from PythonSeleniumBasics.BasicsSelenium11 import BasicsSelenium11

class Handle_alerts(BasicsSelenium11):
    def verify_simple_alert(self):
        self.driver.get("https://demoqa.com/alerts")
        simple_alert_button=self.driver.find_element(By.XPATH, "//button[@id='alertButton']")
        simple_alert_button.click()


        # Switch to alert and accept it
        alert = self.driver.switch_to.alert
        alert_text = alert.text
        print(alert_text)
        alert.accept()
        time.sleep(10)

    def verify_confirm_alerts(self):
        self.driver.get("https://demoqa.com/alerts")
        confirm_alert_button = self.driver.find_element(By.XPATH, "//button[@id='confirmButton']")
        confirm_alert_button.click()
        alert1 = self.driver.switch_to.alert
        #alert1.accept()  #clickok
        alert1.dismiss()
        confirm_alert_msg= self.driver.find_element(By.XPATH, "#//span[@id='confirmResult']")
        print(confirm_alert_msg)
        time.sleep(10)
    def verify_prompt_alerts(self):
        self.driver.get("https://demoqa.com/alerts")
        prompt_alert_button = self.driver.find_element(By.XPATH, "//button[@id='promtButton']")
        prompt_alert_button.click()
        alert2 = self.driver.switch_to.alert
        alert2.send_keys("prompting")
        alert2.accept()
        time.sleep(10)


handle_alerts=Handle_alerts()
handle_alerts.initialize_browser()
#handle_alerts.verify_simple_alert()
#handle_alerts.verify_confirm_alerts()
handle_alerts.verify_prompt_alerts()