from selenium.webdriver.common.by import By
from Web.Locators.Shipping_Loocators import ShippingLocators
from Web.Pages.commonQuestion_Page import CommonQuePage
from Web.Utils.utils import Utils


class ShipPage(CommonQuePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.shippingLink = ShippingLocators.shipping_link
        self.shippingTxT = ShippingLocators.ship_txt
        self.shipXpath = ShippingLocators.ship_link
        self.uiX = ShippingLocators.ui_link
        self.uitxt = ShippingLocators.ui_txt

    def clicking_onShipping(self):
        self.driver.find_element(By.XPATH, self.shippingLink).click()

    def moving_to_shippingPage(self):
        self.clicking_onShipping()
        Util = Utils(self.driver)
        Util.validation(self.shippingTxT, self.assert_txt(self.shipXpath))
        Util.validation(self.uitxt, self.assert_txt(self.uiX))
