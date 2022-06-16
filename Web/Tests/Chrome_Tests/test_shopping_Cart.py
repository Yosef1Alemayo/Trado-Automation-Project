import time

import allure
import pytest
from Server.DB.main import query_for_products_details
from Server.DB.main import query_for_products_with_2_keys
from Web.Utils.PreConditions.precondition import Pre_Condition_Tsiona
from Web.Utils.utils import Utils
from Web.Pages.shopping_Cart_Page import ShoppingCartPage


@pytest.mark.usefixtures('login_correctly')
class TestShoppingCart(Pre_Condition_Tsiona):

    @allure.description('Verify the product details in web matching to details in DB')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_verify_products_details_in_DB(self, login_correctly):

        ''' Verify the product details in web matching to details in DB'''
        driver = self.driver
        # utils = Utils(driver)
        cart = ShoppingCartPage(driver)
        cart.precondition_all_tests()

        #כל פונקציה בנפרד
        cart.verify_product_name()
        cart.verify_price_per_unit()
        cart.verify_unit_in_carton()
        # cart.verify_price_per_carton()
        #
        # #פונקציה אחת שמריצה את הכל
        # cart.verify_products_details()



        #4
        # Verify price per carton:
        #חישוב : מחיר לקרטון = מחיר ליחידה X מס' יחידות שיש בקרטון
        # cartonpriceInWeb = cart.get_product_price_per_carton()
        # unitPrice = cart.get_product_price_per_unit()
        # unitIncarton = cart.get_unit_in_carton()
        # expected_carton_price = cart.calculating_carton_price(unitPrice,unitIncarton)
        # utils.validation(expected_carton_price,cartonpriceInWeb)    #unstable

        # print("carton price from web: ",cartonpriceInWeb)
        # print("unit price",unitPrice)
        # print("unit in carton:",unitIncarton)
        # print("calculation:",expected_carton_price)

        #5
        # #Verify barcode :
        # barcode = cart.get_product_barcode()
        # B = query_for_products_details("אקדיה","barcode")
        # utils.validation(B,barcode)          #### PASSED

        #6
        #Verify minimum order:
        # min = cart.get_minimum_order()
        # M = query_for_products_with_2_keys("אקדיה","units","minimumOrderCartonsCount")
        # utils.validation(M,min)                ####PASSED

# ------------------------------------------------------------

        #1
        # #Verify name:
        # name = cart.get_product_name()
        # N = query_for_products_details("אקדיה",'name')
        # utils.validation(N,name)               ####PASSED


        #2
        #Verify price per unit:
        # price = cart.get_product_price_per_unit()
        # P = query_for_products_details("אקדיה" ,'price')
        # utils.validation(P,price)       #  Assertion Error טסט תקין - אבל נופל בגלל


        #3
        # #Verify units in carton:
        # units = cart.get_unit_in_carton()
        # U = query_for_products_with_2_keys("אקדיה",'units','unitsInCarton')
        # utils.validation(U,units)              ####PASSED


    def test1(self,login_correctly):
        driver = self.driver
        # utils = Utils(driver)
        cart = ShoppingCartPage(driver)
        cart.precondition_all_tests()

        cart.click_on_plus_button()
        cart.click_on_plus_button()
        cart.click_on_plus_button()
        print(cart.number())


