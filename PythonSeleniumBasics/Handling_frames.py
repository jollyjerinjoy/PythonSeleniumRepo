from selenium.webdriver.common.by import By

from PythonSeleniumBasics.BasicsSelenium11 import BasicsSelenium11


class handling_frames(BasicsSelenium11):
    def verify_iframe(self):
        self.driver.get("https://demoqa.com/frames")
        # Find all iframe elements
        total_frames = self.driver.find_elements(By.TAG_NAME, "iframe")
        # Print the number of frames
        print(len(total_frames))
        frame1 = self.driver.find_element(By.XPATH, "//iframe[@id='frame1']")
        # switching the focus
        self.driver.switch_to.frame(frame1)
        frametext = self.driver.find_element(By.XPATH, "//h1[@id='sampleHeading']")
        print(frametext.text)
        # releasing the focus form current frame
        self.driver.switch_to.default_content()

handling_frames_obj= handling_frames()
handling_frames_obj.initialize_browser()
handling_frames_obj.verify_iframe()
