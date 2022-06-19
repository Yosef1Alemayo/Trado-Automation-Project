import time

import pytest
from Web.Pages.searchPage import PageSearch
from Web.Utils.PreConditions.precondition import Pre_Condition

@pytest.mark.usefixtures('login_jonathan')
class Test2(Pre_Condition):
    #Test search for an existing product
    def test_1(self):
            driver = self.driver
            ps = PageSearch(driver)
            ps.search_area("אקדיה ")
            time.sleep(3)


    #Test Product search does not exist
    def test_2(self):
            driver = self.driver
            ps = PageSearch(driver)
            ps.search_area("lamon")


    #Test Search with characters
    def test_3(self):
            driver = self.driver
            ps = PageSearch(driver)
            ps.search_area("%$#")

    #Test Search with numbers
    def test_4(self):
        driver = self.driver
        ps = PageSearch(driver)
        ps.search_area("1586")