import time

import pyautogui
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from PythonSeleniumBasics.BasicsSelenium11 import BasicsSelenium11


class Handling_webelement_Actions(BasicsSelenium11):
    def verify_mouse_hover(self):
        home=self.driver.find_element(By.XPATH, "//a[text()='Home']")
        actions=ActionChains(self.driver) #default ActionChain class provided by selenium, hand;e mouse actions
        actions.move_to_element(home).perform()
    def verify_right_click(self):
        home = self.driver.find_element(By.XPATH, "//a[text()='Home']")
        actions = ActionChains(self.driver)
        actions.context_click(home).perform()
    def verify_drag_and_drop(self):
        self.driver.get("https://demoqa.com/droppable")
        dragme=self.driver.find_element(By.XPATH,"//div[@id='draggable']")
        #//div[@id='droppable']/p[text()='Drop here']
        dropme1=self.driver.find_element(By.XPATH,"//div[@id='droppable']/p[text()='Drop here']")
        dropme = self.driver.find_element(By.XPATH, "//div[@id='droppable']")
        actions = ActionChains(self.driver)
        actions.drag_and_drop(dragme,dropme).perform()

        # move_to_element()
        #// a[text() = ' ']
        #// a[text() = 'Home']

    def verify_keyboard_action(self):
        # Simulate pressing Ctrl + T to open a new tab (using pyautogui)
        pyautogui.hotkey('ctrl', 't')
        time.sleep(2)  # hotkey function- to click more than one mouse key
        # Adding delay for visibility
        pyautogui.write('https://www.google.com')
        # Typing URL
        pyautogui.press('enter')  # Pressing Enter
        


obj1 =Handling_webelement_Actions()
obj1.initialize_browser()
#obj1.verify_mouse_hover()
#obj1.verify_right_click()
#obj1.verify_drag_and_drop()
obj1.verify_keyboard_action()

#https://www.webdriveruniversity.com/Dropdown-Checkboxes-
#https://money.rediff.com/indices/nse
#https://selenium.qabible.in/simple-form-demo.php
#https://ultimateqa.com/simple-html-elements-for-automation
#https://www.w3schools.com/html/html_tables.asp
#https://www.saucedemo.com/inventory.html
#https://www.tpointtech.com/selenium-webdriver
