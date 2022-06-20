import time
import allure
import pytest
from Web.Utils.PreConditions.precondition import Pre_Condition
from Web.Utils.utils import Utils
from Web.Pages.shopping_Cart_Page import ShoppingCartPage


@pytest.mark.usefixtures('login_tsiona')
class TestShoppingCart(Pre_Condition):

    @allure.description('Verify the product details in web matching to details in DB')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_verify_products_details_in_DB(self):
        ''' Verify the product details in web matching to details in DB'''
        driver = self.driver
        cart = ShoppingCartPage(driver)
        cart.precondition_all_tests()
        # ______________________________________
        cart.verify_product_name()
        cart.verify_price_per_unit()
        cart.verify_unit_in_carton()
        cart.verify_price_per_carton()
        cart.verify_barcode()
        cart.verify_minium_order()

    @allure.description('Verify you can add product to cart correctly')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_adding_product_to_cart_correctly(self):
        '''Verify you can add product to cart correctly '''
        driver = self.driver
        utils = Utils(driver)
        cart = ShoppingCartPage(driver)
        cart.precondition_all_tests()
        # ______________________________________
        #Add product to cart :
        cart.click_on_plus_button()
        #Get product name - Expected result
        name = cart.get_product_name()
        #Get product name appears in cart : Actual result
        nameIncart = cart.get_prod_name_in_cart()
        #verify the both names are matching:
        utils.validation(name,nameIncart)       ###PASSED

        #Get price based on calculting: ( price = num of carton X carton price ) - Expected result
        price = cart.calculating_price_in_cart_to_each_prod()
        #Get price in cart : Actual Result
        priceInCart=cart.get_prod_price_in_cart()
        #Verify the both price  are matching :
        utils.validation(price, priceInCart )       ###PASSED

    @allure.description('Verify that you can reduce from quantity of product ')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_reducing_the_amount_of_product_from_cart(self):
        '''Verify that you can reduce from quantity of product '''
        driver = self.driver
        utils = Utils(driver)
        cart = ShoppingCartPage(driver)
        cart.precondition_all_tests()
        '''Precondition : Adding the same product to cart '''
        cart.click_on_plus_button(4)
        # Reduce from the quantity : (insert how meny you want to reduce)
        A = cart.calculating_quantity_after_reduce_quantity(1)
        B = cart.get_quntity_per_product_in_cart()
        utils.validation(A, B)              ###PASSED
























































