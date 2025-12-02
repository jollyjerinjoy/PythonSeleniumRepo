from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from PythonSeleniumBasics.BasicsSelenium11 import BasicsSelenium11


class handle_dropdown(BasicsSelenium11):
    def verify_dropdown(self):
        self.driver.get("https://www.webdriveruniversity.com/Dropdown-Checkboxes-RadioButtons/index.html")
        dropdown1=self.driver.find_element(By.XPATH,"//select[@id='dropdowm-menu-1']")
        select=Select(dropdown1)
        #select.select_by_index(1)
        #select.select_by_value("python")
        #<option value="sql">SQL</option>   sql is visible text
        select.select_by_visible_text("SQL")
        self.driver.back()
        self.driver.forward()
        self.driver.refresh()

    def verify_check_box(self):
        # Navigate to the URL
        self.driver.get("https://www.webdriveruniversity.com/Dropdown-Checkboxes-RadioButtons/index.html")

        # Find the checkbox element and click
        check_box = self.driver.find_element(By.XPATH, "//input[@value='option-1']")
        check_box.click()

        # Check if checkbox is selected and enabled
        print(check_box.is_selected())  #by default false
        print(check_box.is_enabled())   #by default false
        print(check_box.is_displayed())

    def verify_radio_button(self):
        # Navigate to the URL
        self.driver.get("https://www.webdriveruniversity.com/Dropdown-Checkboxes-RadioButtons/index.html")
        green_input = self.driver.find_element(By.XPATH, "//input[@value=\"green\"]")
        green_input.click()
        print(green_input.is_selected())
        print(green_input.is_enabled())
        print(green_input.is_displayed())








handle_dropdown_obj1=handle_dropdown()
handle_dropdown_obj1.initialize_browser()
handle_dropdown_obj1.verify_dropdown()





