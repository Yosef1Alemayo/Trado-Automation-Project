import allure
import pytest
from Web.Pages.commonQuestion_Page import CommonQuePage
from Web.Utils.PreConditions.precondition_betty import Pre_Condition_Betty


@pytest.mark.usefixtures('login_correctly')
class Test(Pre_Condition_Betty):

    @allure.description('Upload a product when the user does not have a store')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_moving_to_CommonQuPage(self, login_correctly):

        """The Driver And The PreCondition("Login Correctly") - What is the Requirements for ?"""
        driver = self.driver
        clicking = CommonQuePage(driver)
        clicking.clicking_allLinks()
