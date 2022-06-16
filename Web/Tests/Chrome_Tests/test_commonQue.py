import allure
import pytest
from Web.Pages.commonQuestion_Page import CommonQuePage
from Web.Utils.PreConditions.precondition_tsiona import Pre_Condition_Tsiona


@pytest.mark.usefixtures('login')
class Test(Pre_Condition_Tsiona):

    @allure.description('Upload a product when the user does not have a store')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_moving_to_CommonQuPage(self):

        """The Driver And The PreCondition("Login Correctly") - What is the Requirements for ?"""
        driver = self.driver
        clicking = CommonQuePage(driver)
        clicking.clicking_allLinks()
