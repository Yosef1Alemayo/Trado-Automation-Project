from selenium.webdriver.common.by import By

from Web.Locators.Shipping_Loocators import ShippingLocators
from Web.Utils.utils import Utils


class ShipPage:

    def __init__(self, driver):
        self.driver = driver
        self.shippingLink = ShippingLocators.ship_link
        self.shippingTxT = ShippingLocators.ship_txt
        self.shiplink = ShippingLocators.ship_linktxt
        self.uiX = ShippingLocators.ship_link
        self.uitxt = ShippingLocators.ship_txt


    def clicking_onShipping(self):
        self.driver.find_element(By.XPATH, self.shippingLink).click()

    def moving_to_shippingPage(self):
        self.clicking_onShipping()
        Util = Utils(self.driver)
        Util.validation(self.shippingTxT, self.shippingLink)
        Util.validation(self.uitxt, self.uiX)
