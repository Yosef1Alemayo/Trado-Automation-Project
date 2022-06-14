from Web.Locators.personalArea_Locators import LocatorArea
from selenium.webdriver.common.by import By
import pytest


class PageArea:
    def __init__(self,driver):
        self.driver = driver
        self.Login = LocatorArea.Login
        self.Phone = LocatorArea.Phone
        self.Click_login = LocatorArea.Click_login
        self.Sms_code = LocatorArea.Sms_code
        self.Verify_button = LocatorArea.Verify_button
        self.Personal_area_button = LocatorArea.Personal_area_button
        self.Edit_button = LocatorArea.Edit_button
        self.Save_button = LocatorArea.Save_button
        self.Search = LocatorArea.Search

    def test_login(self):
        self.driver.fined_element(By.XPATH,self.Login).click()
        self.driver.fined_element(By.XPATH,self.Phone).send_keys('0522578853')
        self.driver.fined_element(By.XPATH,self.Click_login).click()
        # data base
        self.driver.fined_element(By.XPATH,self.Sms_code).send_keys('')
        self.driver.fined_element(By.XPATH,self.Verify_button).click()


    def test_delivery_details(self):
        self.driver.fined_element(By.ID,self.Personal_area_button).click()
        a = self.driver.find_elemnets(By.XPATH,"//input")
        for i in range(len(a)):
            if i == 1:
                a[i].send_keys('Jonathan')
            elif i == 2:
                a[i].send_keys('Elias')
            elif i == 3:
                a[i].send_keys('0522578853')
            elif i == 4:
                a[i].send_keys('gonathan46@gmail.com')
            elif i == 5:
                a[i].send_keys('205593718')
            elif i == 6:
                a[i].send_keys('Holon')
            elif i == 7:
                a[i].send_keys('10')
        self.driver.fined_element(By.XPATH,self.Edit_button).click()
        self.driver.fined_element(By.XPATH,self.Save_button).click()


    def test_search(self,):
        self.driver.fined_element(By.XPATH,self.Search).send_keys()
