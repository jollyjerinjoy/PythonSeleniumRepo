from selenium.webdriver.common.by import By

from PythonSeleniumBasics.BasicsSelenium11 import BasicsSelenium11

class HandleBrowserCommands(BasicsSelenium11):
    def verify(self):
        self.driver.get("https://selenium.qabible.in/simple-form-demo.php")
        self.driver.find_elemment(By.ID,"single - input - field")    #tagname[attribute='attribute value']
        self.driver.find_elemment(By.CLASS_NAME,"form-control")
        self.driver.find_elemment(By.TAG_NAME,"button")
        self.driver.find_elemment(By.LINK_TEXT,"Checkbox Demo")
        self.driver.find_element(By.PARTIAL_LINK_TEXT,"Checkbox ")
        self.driver.find_element(By.CSS_SELECTOR,"button[id='button-one']") #from mouse selection it start to find
          # / html / body / section / div / div / div[2] / div[1] / div / div[2] / form / button   xpath might change -absolute path
          # relativexpath   //tagname[@attribute='attribute value']   entire dom can be searched
        self.driver.find_element(By.XPATH,"//button@[id='button-one']")
        #Xpath of element to be located//child::xpath of element that can  be uniquely identified
        self.driver.find_element(By.XPATH,"//div[@class='card']//child::button[@id='button-one']")
        # XPath access using following
        self.driver.find_element(By.XPATH, "//button[@id='button-one']//following::div[@class='card']")

        # XPath access using preceding
        self.driver.find_element(By.XPATH, "//button[@id='button-one']//preceding::div[@class='card']")
        # XPath access using ancestor
        self.driver.find_element(By.XPATH, "//div/ancestor::div[@class='card']")

        # XPath access using descendant
        self.driver.find_element(By.XPATH, "//div[@class='card']//descendant::div")
