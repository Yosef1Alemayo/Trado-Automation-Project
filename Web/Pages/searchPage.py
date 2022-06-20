
from Web.Locators.search_Locators import LocatorsSearch
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

class PageSearch:
    def __init__(self,driver):
        self.driver = driver
        self.Search_field = LocatorsSearch.Search_field
        self.click = LocatorsSearch.click

    def search_area(self,Search_field):
        self.driver.find_element(By.XPATH, self.Search_field).clear()
        self.driver.find_element(By.XPATH,self.Search_field) .send_keys(Search_field)
        self.driver.find_element(By.XPATH,self.Search_field).send_keys(Keys.RETURN)

