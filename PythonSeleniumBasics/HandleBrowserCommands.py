
from PythonSeleniumBasics.BasicsSelenium11 import BasicsSelenium11

#child class
class HandleBrowserCommands(BasicsSelenium11):
    def verify_commands(self):
        title = self.driver.title
        print(title)
        url=self.driver.current_url
        print(url)
        handle_id=self.driver.current_window_handle
        print(handle_id)


obj1 = HandleBrowserCommands()
obj1.initialize_browser()
obj1.verify_commands()
obj1.close_browser()

