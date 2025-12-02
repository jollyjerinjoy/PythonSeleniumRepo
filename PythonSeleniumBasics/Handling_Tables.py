from selenium.webdriver.common.by import By

from PythonSeleniumBasics.BasicsSelenium11 import BasicsSelenium11


class Table_handling(BasicsSelenium11):
    def handle_tables(self):
        self.driver.get("https://money.rediff.com/indices/nse")
        table_variable = self.driver.find_element(By.XPATH, "//table[@id='dataTable']")
        print(table_variable.text)
        table_row = self.driver.find_element(By.XPATH, "//table[@id='dataTable']/tbody/tr[3]")
        print("Third row text is ", table_row.text)  # Get the text of the row -tr
        table_column=self.driver.find_element(By.XPATH, "//table[@id='dataTable']/tbody/tr[3]/td[2]")
        print("Third row, second column text is ", table_column.text)
        table_last_row=self.driver.find_element(By.XPATH, "//table[@id='dataTable']/tbody/tr[last()]")
        print("Last row is ", table_last_row.text)
        table_last_column=self.driver.find_element(By.XPATH, "//table[@id='dataTable']/tbody/tr[3]/td[last()]")
        print("third row. Last column text is ", table_last_column.text)
        #find_elements - e.g count of element occurrence, collection of web elements, cannot find no such element exception,executes testcase
        #welement actions - keyboard and mouse actions - e.g click . drag, hover(move_, keyboard value enter




table_handle = Table_handling()
table_handle.initialize_browser()
table_handle.handle_tables()