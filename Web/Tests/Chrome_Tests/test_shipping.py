import allure
import pytest
from Web.Pages.Shipping_Page import ShipPage
from Web.Utils.PreConditions.precondition_betty import Pre_Condition_Betty


@pytest.mark.usefixtures('login_correctly')
class TestShippingPage(Pre_Condition_Betty):

    @allure.description('Validating moving into shipping page correctly')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_signin_correctly(self, login_correctly):

        """The Driver And The PreCondition("Login Correctly") - What is the Requirements for ?"""
        driver = self.driver
        ship = ShipPage(driver)
        ship.moving_to_shippingPage()
