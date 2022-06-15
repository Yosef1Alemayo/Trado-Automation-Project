from time import sleep
from selenium.webdriver.common.by import By
from Web.Locators.NavBar_Locators import NavBarLocators
# from Web.Pages.commonQuestion_Page import CommonQuePage
# from Web.Utils.utils import Utils


class NavBarPage:

    def __init__(self, driver):
        self.driver = driver
        self.Window = NavBarLocators.window
        self.button_x = NavBarLocators.Button_x

    def clicking_links(self, link, classname):
        buttons = self.driver.find_elements(By.XPATH, link)
        p = 0
        # clicking buttons in syllabus
        while p < len(buttons):
            sleep(3)
            html_link = self.driver.find_elements(By.CLASS_NAME, classname)
            html_link[p].click()
            sleep(3)
            self.driver.back()
            # if self.Window == True:
            #     self.driver.finf_element(By.XPATH, self.button_x).click()
            #     sleep(3)
            #     self.driver.back()
            sleep(3)
            p += 1
