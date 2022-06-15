import allure
import pytest
from Server.DB.main import query_for_products_details
from Server.DB.main import query_for_products_with_2_keys
from Web.Utils.PreConditions.precondition_tsiona import Pre_Condition_Tsiona
from Web.Utils.utils import Utils
from Web.Pages.shopping_Cart_Page import ShoppingCartPage


@pytest.mark.usefixtures('login_correctly')
class TestShoppingCart(Pre_Condition_Tsiona):

    @allure.description('Verify the product details in web matching to details in DB')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_verify_products_details_in_DB(self, login_correctly):

        ''' Verify the product details in web matching to details in DB'''
        driver = self.driver
        utils = Utils(driver)
        cart = ShoppingCartPage(driver)
        cart.click_on_canabis_page()
        cart.click_on_product_from_list(4)

        # #Verify name:
        # name = cart.get_product_name()
        # N = query_for_products_details("אקדיה",'name')
        # utils.validation(N,name)               ####PASSED

        #Verify price per unit:
        price = cart.get_product_price_per_unit()
        P = query_for_products_details("אקדיה" ,'price')
        utils.validation(P,price)

        # #Verify units in carton:
        # units = cart.get_unit_in_carton()
        # U = query_for_products_with_2_keys("אקדיה",'units','unitsInCarton')
        # utils.validation(U,units)              ####PASSED

#לא תקין! צריך לשנות את החישוב של מחיר לקרטון -
#מחיר לקרטון = מחיר ליחידהX מס יחידות בקרטון
#לעשות פונקציה שמחשבת ולהשוות פה עם הנתון שחוזר מהאתר
        # # Verify price per carton:
        # price = cart.get_product_price_per_carton()   ###FAILED

        # #Verify barcode :
        # barcode = cart.get_product_barcode()
        # B = query_for_products_details("אקדיה","barcode")
        # utils.validation(B,barcode)          #### PASSED

        #Verify minmum order:
        min = cart.get_minimum_order()
        M = query_for_products_with_2_keys("אקדיה","units","minimumOrderCartonsCount")
        utils.validation(M,min)                ####PASSED







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






