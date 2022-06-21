import allure
import pytest
from Web.Pages.navBar_Page import NavBarPage
from Web.Utils.PreConditions.precondition import Pre_Condition1
from Web.Locators.NavBar_Locators import NavBarLocators


@pytest.mark.usefixtures('login_betty')
class TestNavBer(Pre_Condition1):

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("Validates buttons opening correctly")
    def test_topBar(self):

        """"Validates buttons opening correctly"""
        driver = self.driver
        headers = NavBarPage(driver)
        headers.top_bar_click()

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("Validates menu buttons opening correctly")
    def test_menuButtons(self):

        """Validates menu buttons opening correctly"""
        driver = self.driver
        headers = NavBarPage(driver)
        headers.clicking_on_buttons(NavBarLocators.header2, NavBarLocators.list1, NavBarLocators.list_txt)


    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("Validates dataBase match the web page")
    def test_DB(self):

        """Validates dataBase match the web page"""
        driver = self.driver
        headers = NavBarPage(driver)
        headers.check_in_DB()
