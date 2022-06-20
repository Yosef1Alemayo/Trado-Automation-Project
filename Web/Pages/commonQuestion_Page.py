from time import sleep
import allure
from selenium.webdriver.common.by import By
from Web.Locators.CommonQuestion_Locators import CommonQueLocators
from Web.Utils.utils import Utils


class CommonQuePage:

    def __init__(self, driver):
        self.driver = driver
        self.commonQue_links = CommonQueLocators.commonQue_Button
        self.productsPage_button = CommonQueLocators.productsPage_Button
        self.uploadProduct_button = CommonQueLocators.uploadProduct_Button
        self.commonQue_xpath = CommonQueLocators.commonQue_innertext
        self.productPage_xpath = CommonQueLocators.productpage_innertext
        self.uploadproduct_xpath = CommonQueLocators.uploadProduct_innertext
        self.commonQue_text = CommonQueLocators.commonQue_txt
        self.productPage_text = CommonQueLocators.product_pageTXT
        self.uploadproduct_text = CommonQueLocators.uploadproduct_txt

    @allure.step("Click on common question button")
    def click_onlink(self):
        self.driver.find_element(By.XPATH, self.commonQue_links).click()

    @allure.step("Click on 'move to products page' button")
    def click_productsPage(self):
        self.driver.find_element(By.XPATH, self.productsPage_button).click()

    @allure.step("Click on 'upload product page' button")
    def click_uploadProduct(self):
        self.driver.find_element(By.XPATH, self.uploadProduct_button).click()

    def assert_txt(self,locator):
        value =self.driver.find_element(By.XPATH,locator).get_attribute("innerText")
        return value

    def clicking_allLinks(self):
        self.click_onlink()
        Util = Utils(self.driver)
        Util.validation(self.commonQue_text, self.assert_txt(self.commonQue_xpath))
        self.click_productsPage()
        Util.validation(self.productPage_text, self.assert_txt(self.productPage_xpath))
        self.driver.back()
        self.click_uploadProduct()
        Util.validation(self.uploadproduct_text, self.assert_txt(self.uploadproduct_xpath))
        self.driver.back()
