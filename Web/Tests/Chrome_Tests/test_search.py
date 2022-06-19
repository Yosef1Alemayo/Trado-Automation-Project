import pytest
from Web.Utils.PreConditions.pre_condition import Precondition_Chrome
from Web.Pages.searchPage import PageSearch
from Web.Utils.PreConditions.precondition_Jonathan import Pre_Condition_Jonathan

@pytest.mark.usefixtures('login_correctly')
class Test2(Pre_Condition_Jonathan):
    #Test search for an existing product
    def test_1(self, login_correctly):
            driver = self.driver
            ps = PageSearch(driver)
            ps.search_area("אקדיה ")


    #Test Product search does not exist
    def test_2(self, login_correctly):
            driver = self.driver
            ps = PageSearch(driver)
            ps.search_area("lamon")


    #Test Search with characters
    def test_3(self, login_correctly):
            driver = self.driver
            ps = PageSearch(driver)
            ps.search_area("%$#")

    #Test Search with numbers
    def test_4(self, login_correctly):
        driver = self.driver
        ps = PageSearch(driver)
        ps.search_area("1586")