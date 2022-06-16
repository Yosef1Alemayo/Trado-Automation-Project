import allure
import pytest
from Web.Pages.navBar_Page import NavBarPage
from Web.Utils.PreConditions.precondition import Pre_Condition
from Web.Locators.NavBar_Locators import NavBarLocators


@pytest.mark.usefixtures('login_betty')
class TestNavBer(Pre_Condition):

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("Validates links opening correctly")
    def test_links(self):

        """Validates links opening correctly"""
        driver = self.driver
        headers = NavBarPage(driver)
        headers.clicking(NavBarLocators.header1, NavBarLocators.list2, NavBarLocators.list_txt2)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("Validates menu buttons opening correctly")


    def test_menuButtons(self):

        """Validates menu buttons opening correctly"""
        driver = self.driver
        headers = NavBarPage(driver)
        headers.clicking(NavBarLocators.header2, NavBarLocators.list1, NavBarLocators.list_txt)

