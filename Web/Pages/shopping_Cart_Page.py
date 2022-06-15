from Web.Base.ChromeBase.chrome_base import Base_Chrome
from Web.Locators.shooping_Cart_Locators import ShoppingCartLocators
from selenium.webdriver.common.by import By


class ShoppingCartPage():

    def __init__(self,driver):
        self.driver = driver
        self.canabis_page = ShoppingCartLocators.canbis_page
        self.canabis_product_list = ShoppingCartLocators.canabis_product_list

        self.plus_button = ShoppingCartLocators.plus_button
        self.minus_button = ShoppingCartLocators.minus_button
        self.delete_product_from_cart = ShoppingCartLocators.delete_product_from_cart
        self.empty_the_cart = ShoppingCartLocators.empty_the_cart
        self.payment_button = ShoppingCartLocators.payment_button

        self.product_name = ShoppingCartLocators.product_name
        self.product_price_per_carton = ShoppingCartLocators.product_price_per_carton
        self.product_price_per_unit = ShoppingCartLocators.product_price_per_unit
        self.unit_in_carton = ShoppingCartLocators.unit_in_carton
        self.product_barcode = ShoppingCartLocators.product_barcode


        self.prod_name_in_cart = ShoppingCartLocators.prod_name_in_cart
        self.prod_price_in_cart = ShoppingCartLocators.prod_price_in_cart
        self.quantity_per_product = ShoppingCartLocators.quantity_per_product


    def click_on_canabis_page(self):
        self.driver.find_element(By.XPATH,self.canabis_page).click()

    def get_canabis_product_list(self):
        prodList= self.driver.find_elements(By.XPATH,self.canabis_product_list)
        return prodList
        # print(len(prodList))

    def click_on_product_from_list(self, num):
        prodList = self.get_canabis_product_list()
        prodList[num].click()

### Get product details: for assertion ###
    def get_product_name(self):
        prodName = self.driver.find_element(By.XPATH,self.product_name).get_attribute("innerText")
        return prodName
        # print(prodName)

    def get_product_price_per_carton(self):
        prodPrice = self.driver.find_element(By.XPATH,self.product_price_per_carton).get_attribute("innerText").split("/")
        return prodPrice[0]
        # print(prodPrice[0])

    def get_unit_in_carton(self):
        unitInCarton = self.driver.find_element(By.XPATH,self.unit_in_carton).get_attribute("innerText").split("י")
        return unitInCarton[0]

    def get_product_barcode(self):
        barcode = self.driver.find_element(By.XPATH,self.product_barcode).get_attribute("innerText").split(": ")
        return barcode[1]
        # print(barcode[1])

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
