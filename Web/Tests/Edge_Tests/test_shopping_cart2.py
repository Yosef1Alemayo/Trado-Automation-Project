import allure
import pytest
from Web.Utils.PreConditions.precondition import Pre_Condition1
from Web.Utils.utils import Utils
from Web.Pages.shopping_Cart_Page import ShoppingCartPage
from Server.DB.main import *


@pytest.mark.usefixtures('login_tsiona')
class TestShoppingCart(Pre_Condition1):

    @pytest.mark.regression
    @pytest.mark.sanity
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
        cart.click_on_plus_button(1)
        #Get product name - Expected result
        name = cart.get_product_name()
        #Get product name appears in cart : Actual result
        nameIncart = cart.get_prod_name_in_cart()
        #Assertion -the both names are matching:
        utils.validation(name,nameIncart)       ###PASSED

        #Get price based on calculting: ( price = num of carton X carton price ) - Expected result
        price = cart.calculating_price_in_cart_to_each_prod()
        #Get price in cart : Actual Result
        priceInCart=cart.get_prod_price_in_cart()
        #Assertion- the both price  are matching :
        utils.validation(price, priceInCart )       ###PASSED

    @pytest.mark.regression
    @pytest.mark.sanity
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

    @pytest.mark.regression
    @pytest.mark.sanity
    @allure.description('Verify you can delete the en cart' )
    @allure.severity(allure.severity_level.CRITICAL)
    def test_delete_the_entire_shopping_cart(self):
        ''' Verify you can delete all the cart after adding two different products '''
        driver = self.driver
        utils = Utils(driver)
        cart = ShoppingCartPage(driver)
        cart.precondition_all_tests()
        cart.click_on_plus_button(1)
        driver.back()
        cart.get_canabis_product_list()
        cart.click_on_product_from_list(5)
        cart.click_on_plus_button(1)
        cart.click_on_empty_the_cart()
        expected = "העגלה שלך ריקה"
        actual = cart.get_message_when_cart_is_empty()
        utils.validation(expected,actual)       ###PASSED

    @pytest.mark.regression
    @pytest.mark.sanity
    @allure.description('Verify you can move to payment page')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_verify_moving_to_payment_page(self):
        ''' Verify you can move to payment page '''
        driver = self.driver
        utils = Utils(driver)
        cart = ShoppingCartPage(driver)
        cart.precondition_all_tests()
        cart.click_on_plus_button(1)
        driver.back()
        cart.get_canabis_product_list()
        cart.click_on_product_from_list(5)
        cart.click_on_payment_button()
        excpected = "פרטים לחשבונית"
        actual = cart.get_payment_page_title()
        utils.validation(excpected,actual)      ###PASSED


    '''DB TESTS '''
    ###  Assertion product details in DB : ###

    @allure.description('Verify product name in Web matching to name in DB')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_verify_product_name(self):
        driver = self.driver
        utils = Utils(self.driver)
        cart = ShoppingCartPage(driver)
        cart.precondition_all_tests()

        name = cart.get_product_name()
        dbQuery = query_for_products_details("אקדיה", 'name')
        utils.validation(dbQuery, name)  ####PASSED

    @pytest.mark.sanity
    @allure.description('Verify unit price in Web matching unit price  in DB')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_verify_product_price_per_unit(self):
        driver = self.driver
        utils = Utils(self.driver)
        cart = ShoppingCartPage(driver)
        cart.precondition_all_tests()

        price = cart.get_product_price_per_unit()
        dbQuery = query_for_products_details("אקדיה", 'price')
        utils.validation(dbQuery, price)     ### FAILDE

    @pytest.mark.sanity
    @allure.description('Verify unit in carton in Web matching to unit in carton in DB')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_verify_unit_in_carton(self):
        driver = self.driver
        utils = Utils(self.driver)
        cart = ShoppingCartPage(driver)
        cart.precondition_all_tests()

        units = cart.get_unit_in_carton()
        dbQuery = query_for_products_with_2_keys("אקדיה", 'units', 'unitsInCarton')
        utils.validation(dbQuery, units)  ####PASSED

    @allure.description('Verify barcode in Web matching to barcode in DB')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_verify_barcode(self):
        driver = self.driver
        utils = Utils(self.driver)
        cart = ShoppingCartPage(driver)
        cart.precondition_all_tests()

        barcode = cart.get_product_barcode()
        dbQuery = query_for_products_details("אקדיה", "barcode")
        utils.validation(dbQuery, barcode)  #### PASSED

    @allure.description('Verify minimum to order in Web matching to minimum to order in DB')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_verify_minimum_to_order(self):
        driver = self.driver
        utils = Utils(self.driver)
        cart = ShoppingCartPage(driver)
        cart.precondition_all_tests()

        minOrder = cart.get_minimum_order()
        dbQuery = query_for_products_with_2_keys("אקדיה", "units", "minimumOrderCartonsCount")
        utils.validation(dbQuery, minOrder)  ####PASSED

    @pytest.mark.sanity
    @allure.description('Verify price per carton in Web matching to calculation base on DB')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_verify_price_per_carton(self):
        driver = self.driver
        utils = Utils(self.driver)
        cart = ShoppingCartPage(driver)
        cart.precondition_all_tests()

        # get price from DB
        dbQuery = query_for_products_details("אקדיה", 'price')
        # get price from web
        unitPrice = cart.get_product_price_per_unit()
        # get_unit in carton from web
        unitIncarton = cart.get_unit_in_carton()
        # calaulation price per carton :
        calculation_based_on_DB = (float(dbQuery)*float(unitIncarton))
        calculation_based_on_web = cart.calculating_carton_price()
        # assertion:
        utils.validation(calculation_based_on_DB, calculation_based_on_web)


































































