from time import sleep
from selenium.webdriver.common.by import By
from Server.DB.main import *
from Server.DB.main import query_for_products_details
from Web.Locators.NavBar_Locators import NavBarLocators
from Web.Pages.commonQuestion_Page import CommonQuePage
from Web.Pages.shopping_Cart_Page import ShoppingCartPage
from Web.Utils.utils import Utils


class NavBarPage(CommonQuePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.BT = NavBarLocators.list_buttons
        self.locator = NavBarLocators.assertion_listButtons
        self.txt = NavBarLocators.assertionTXT_listButtons
        self.section_name = NavBarLocators.list_sectionName
        self.assert_locator = NavBarLocators.list_locator
        self.collectionbuttons = NavBarLocators.list_collectionbuttons

    def clickON(self, locator):
        self.driver.find_element(By.XPATH, locator).click()

    def clicking_on_buttons(self, link, list_locator, list_txt):
        buttons = self.driver.find_elements(By.XPATH, link)
        util = Utils(self.driver)
        xpath = list_locator
        txt = list_txt

        # clicking buttons
        for button, i, j in zip(buttons, xpath, txt):
            button.click()
            x = self.assert_txt(i)
            util.validation(j, x)
            print(j, x)
            self.driver.back()

    def top_bar_click(self):
        clicks = self.BT
        assert_xpath = self.locator
        assert_txt = self.txt
        util = Utils(self.driver)

        for c,i,j in zip(clicks,assert_xpath,assert_txt):
            sleep(3)
            self.clickON(c)
            sleep(3)
            x = self.assert_txt(i)
            util.validation(j, x)
            print(j, x)
            self.driver.back()
            sleep(3)

    def check_in_DB(self):
        util = Utils(self.driver)
        collectionName = NavBarLocators.list_collectionName
        buttons = self.collectionbuttons

        for c, i, a in zip(buttons, collectionName, self.assert_locator):
            sleep(3)
            self.clickON(c)
            sleep(3)
            value = query_for_collection_len(i)
            print(i,value)
            x = self.assert_txt(a)
            util.validation(value, x)
            print(value, x)
