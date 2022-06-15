import time
from Server.DB.main import query_for_products_details
import pytest
from Web.Utils.PreConditions.pre_condition import Precondition_Chrome
from Web.Utils.utils import Utils
from Web.Pages.shopping_Cart_Page import ShoppingCartPage


@pytest.mark.usefixtures('login_correctly')
class TestShoppingCart(Precondition_Chrome):

    def test_adding_product_to_cart_properly(self, login_correctly):
        driver = self.driver
        utils = Utils(driver)
        cart = ShoppingCartPage(driver)
        cart.click_on_canabis_page()
        cart.click_on_product_from_list(4)

        # Getting product details:

        #Verify name:
        name = cart.get_product_name()
        N = query_for_products_details("אקדיה",'name')
        utils.validation(N,name)               ####PASSED

        #Verify price per carton:
        # price = cart.get_product_price_per_carton() ### יש בעיה ה-SPLIT חוזר עם גרשיים
        # P = query_for_products_details("אקדיה" ,'price')
        # utils.validation(P,price)  #
        # print(price)
        # print(P)

        #Verify units in carton :
        units = cart.get_unit_in_carton()
        U = query_for_products_details("אקדיה",'units.unitsInCarton') ####חוזר עם כמה ערכים
        utils.validation(U,units)
        print(U)

        #Verify barcode :
        barcode = cart.get_product_barcode()
        B = query_for_products_details("אקדיה","barcode")
        utils.validation(B,barcode)          #### PASSDE
        print(B)
        print(barcode)


        # #Adding product to cart:
        # cart.click_on_plus_button()
        # #Getting prooduct details in cart- to verify if detthey are matching:
        # C = cart.get_prod_name_in_cart()
        # cart.get_prod_price_in_cart()
        # cart.get_quantity_per_product_in_cart()
        #
        # cart.click_on_payment_button()
        # time.sleep(5)
        # print(B)
        # print(C)
        # assert B == C






