import time
import allure
import pytest
from Web.Pages.searchPage import PageSearch
from Web.Utils.PreConditions.precondition import Pre_Condition

@pytest.mark.usefixtures('login_jonathan')
class Test2(Pre_Condition):
    @pytest.mark.sanity
    @allure.description('Test search for an existing product')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_1(self):
            driver = self.driver
            ps = PageSearch(driver)
            ps.search_area("אקדיה")


    @allure.description('Test Product search does not exist')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_2(self):
            driver = self.driver
            ps = PageSearch(driver)
            ps.search_area("lamon")



    @allure.description('Test Search with characters')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_3(self):
            driver = self.driver
            ps = PageSearch(driver)
            ps.search_area("%$#")



    @allure.description('Test Search with numbers')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_4(self):
            driver = self.driver
            ps = PageSearch(driver)
            ps.search_area("1586")