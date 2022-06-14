from Web.Base.ChromeBase.chrome_base import Base_Chrome
from Web.Locators.shooping_Cart_Locators import ShoppingCartLocators
from selenium.webdriver.common.by import By


class ShoppingCartPage():

    def __init__(self,driver):
        self.driver = driver
        self.canabis_page = ShoppingCartLocators.canbis_page
        self.canabis_product_list = ShoppingCartLocators.canabis_product_list
        self.products_list_sales = ShoppingCartLocators.sales_product_list
        self.plus_button = ShoppingCartLocators.plus_button
        self.minus_button = ShoppingCartLocators.minus_button
        self.delete_product_from_cart = ShoppingCartLocators.delete_product_from_cart
        self.empty_the_cart = ShoppingCartLocators.empty_the_cart
        self.product_name = ShoppingCartLocators.product_name
        self.product_price = ShoppingCartLocators.product_price
        self.prod_name_in_cart = ShoppingCartLocators.prod_name_in_cart
        self.prod_price_in_cart = ShoppingCartLocators.prod_price_in_cart
        self.quantity_per_product = ShoppingCartLocators.quantity_per_product
        self.payment_button = ShoppingCartLocators.payment_button


    def click_on_canabis_page(self):
        self.driver.find_element(By.XPATH,self.canabis_page).click()

    def get_canabis_product_list(self):
        prodList= self.driver.find_elements(By.XPATH,self.canabis_product_list)
        return prodList

    def click_on_product_from_list(self, num):
        prodList = self.get_canabis_product_list()
        prodList[num].click()

    # def get_sales_products_list(self):
    #     prodList =self.driver.find_elements(By.XPATH,self.products_list_sales)
    #     return prodList

### Get product details: for assertion ###
    def get_product_name(self):
        prodName = self.driver.find_element(By.XPATH,self.product_name).get_attribute("innerText")
        return prodName
        # print(prodName)

    def get_product_price(self):
        prodPrice = self.driver.find_element(By.XPATH,self.product_price).get_attribute("innerText")
        return prodPrice
        # print(prodPrice)

    #Adding prod(1 per click)
    def click_on_plus_button(self):
        self.driver.find_element(By.XPATH,self.plus_button).click()

    #Reduce from quantity(1 per click)
    def click_on_minus_button(self):
        self.driver.find_element(By.XPATH,self.minus_button).click()

    #Delete sepcific prod from cart
    def click_on_delete_prod_from_cart(self):
        self.driver.find_element(By.XPATH,self.delete_product_from_cart).click()

    def click_on_empty_the_cart(self):
        self.driver.find_element(By.XPATH,self.empty_the_cart).click()

    def click_on_payment_button(self):
        self.driver.find_element(By.XPATH, self.payment_button).click()

### Get prod details in cart :
    def get_prod_name_in_cart(self):
        prodNameInCart = self.driver.find_element(By.XPATH,self.prod_name_in_cart).get_attribute("innerText")
        return prodNameInCart
        # print(prodNameInCart)

    def get_prod_price_in_cart(self):
        prodPriceInCart = self.driver.find_element(By.XPATH,self.prod_price_in_cart).get_attribute("innerText")
        return prodPriceInCart
        # print(prodPriceInCart)

    def get_quantity_per_product_in_cart(self):
        quantity = self.driver.find_element(By.XPATH,self.quantity_per_product).get_attribute("innerText")
        return quantity
        # print(quantity)
