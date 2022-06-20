import allure
import pytest
from Web.Pages.commonQuestion_Page import CommonQuePage
from Web.Utils.PreConditions.precondition import Pre_Condition


@pytest.mark.usefixtures('login_betty')
class Test(Pre_Condition):

    @allure.description('Validates moving to "common question page"')
    @allure.severity(allure.severity_level.MINOR)
    def test_moving_to_CommonQuestionPage(self):

        """Validates moving to "common question page" """
        driver = self.driver
        clicking = CommonQuePage(driver)
        clicking.clicking_allLinks()
