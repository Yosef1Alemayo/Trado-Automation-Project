import time

import allure
import pytest
from Server.DB.main import query_for_products_details
from Server.DB.main import query_for_products_with_2_keys
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
        # utils = Utils(driver)
        cart = ShoppingCartPage(driver)
        cart.precondition_all_tests()

        #כל פונקציה בנפרד
        # cart.verify_product_name()
        # cart.verify_price_per_unit()
        # cart.verify_unit_in_carton()
        cart.verify_price_per_carton()












