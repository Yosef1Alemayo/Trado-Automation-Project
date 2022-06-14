import time
from Server.DB.main import query_for_products_details
import pytest
from Web.Utils.PreConditions.pre_condition import Precondition_Chrome
from Web.Pages.shopping_Cart_Page import ShoppingCartPage

@pytest.mark.usefixtures('login_correctly')
class TestShoppingCart(Precondition_Chrome):

    def test_adding_product_to_cart_properly(self, login_correctly):
        driver = self.driver
        cart = ShoppingCartPage(driver)
        time.sleep(3)
        cart.click_on_canabis_page()
        time.sleep(3)
        # cart.click_on_product_from_list(5)
        #
        # #Getting prouduct details:
        # B = cart.get_product_name()
        # N = query_for_productName('name')
        # assert B == N
        #
        # G= cart.get_product_price()
        # T = query_for_productName('price')
        #
        # d = False
        # A = query_for_productName('chsc')
        #
        #
        #
        #
        #
        # cart.get_product_price()
        # #Adding product to cart:
        # cart.click_on_plus_button()
        # #Getting prooduct details in cart- to vertify if they are matching:
        # C = cart.get_prod_name_in_cart()
        # cart.get_prod_price_in_cart()
        # cart.get_quantity_per_product_in_cart()
        #
        # cart.click_on_payment_button()
        # time.sleep(5)
        # print(B)
        # print(C)
        # assert B == C






