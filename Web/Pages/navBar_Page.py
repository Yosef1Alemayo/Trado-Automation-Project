from time import sleep
from selenium.webdriver.common.by import By
from Web.Locators.NavBar_Locators import NavBarLocators
from Web.Pages.commonQuestion_Page import CommonQuePage
from Web.Utils.utils import Utils


class NavBarPage(CommonQuePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def clicking(self, link, list_locator, list_txt):
        buttons = self.driver.find_elements(By.XPATH, link)
        util = Utils(self.driver)
        xpath = list_locator
        txt = list_txt

        # clicking buttons
        for button, i, j in zip(buttons, xpath, txt):
            button.click()
            x = self.assert_txt(i)
            util.validation(j, x)
            print(x, j)
            self.driver.back()
