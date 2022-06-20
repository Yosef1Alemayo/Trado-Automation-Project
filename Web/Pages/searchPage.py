
from Web.Locators.search_Locators import LocatorsSearch
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select
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
        # time.sleep(8)


        # self.driver.find_element(By.XPATH, self.click).click()
        # time.sleep(3)

        # select = Select(self.driver.find_element(By.XPATH, "//header/div[1]/div[1]/div[1]/div[1]"))
        # select.select_by_index(1)
        # time.sleep(3)

        # dark = self.driver.find_elements(By.XPATH, "//header/div[1]/div[1]/div[1]/div[1]")
        # dark[2].click()
        # time.sleep(5)
