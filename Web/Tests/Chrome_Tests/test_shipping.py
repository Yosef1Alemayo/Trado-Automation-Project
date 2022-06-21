import allure
import pytest
from Web.Pages.Shipping_Page import ShipPage
from Web.Utils.PreConditions.precondition import Pre_Condition


@pytest.mark.usefixtures('login_betty')
class TestShippingPage(Pre_Condition):

    @pytest.mark.regression
    @allure.description('Validating moving into shipping page correctly')
    @allure.severity(allure.severity_level.MINOR)
    def test_signin_correctly(self):

        """Validating moving into shipping page correctly"""
        driver = self.driver
        ship = ShipPage(driver)
        ship.moving_to_shippingPage()
