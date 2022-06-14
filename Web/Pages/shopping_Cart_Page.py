from Web.Base.ChromeBase.chrome_base import Base_Chrome
from Web.Locators.shooping_Cart_Locators import ShoppingCartLocators
from selenium.webdriver.common.by import By


class ShoppingCart(Base_Chrome):

    def __init__(self,driver):
        self.driver = driver
        self.products_list = ShoppingCartLocators.products_list
        self.plus_button = ShoppingCartLocators.plus_button
        self.minus_button = ShoppingCartLocators.minus_button
        self.