import allure
import pytest
from Web.Pages.Shipping_Page import ShipPage
from Web.Utils.PreConditions.precondition import Pre_Condition


@pytest.mark.usefixtures('login_betty')
class TestShippingPage(Pre_Condition):

    @allure.description('Validating moving into shipping page correctly')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_signin_correctly(self):

        """The Driver And The PreCondition("Login Correctly") - What is the Requirements for ?"""
        driver = self.driver
        ship = ShipPage(driver)
        ship.moving_to_shippingPage()
