import allure
import pytest
from Web.Pages.upload_new_product_page import Upload_New_Product_Page
from Web.Utils.PreConditions.precondition import Pre_Condition
from Web.Utils.utils import Utils

@pytest.mark.usefixtures('login_tsiona')
class Test_Upload_New_Product(Pre_Condition):

    @allure.description('Upload a product incorrectly when the user does not have a store')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_upload_product_incorrectly_without_store(self):
        driver = self.driver
        utils = Utils(driver)
        upload_product = Upload_New_Product_Page(driver)

        upload_product.click_add_new_product_section()
        upload_product.enter_data_to_inputs(['1', 'Brands', '0555555555', 'a@trado.com', 'Brands.com', 'Tel-Aviv',
                                             'Herzel', '1'])
        upload_product.click_add_new_product_button()
        driver.implicitly_wait(5)
        utils.validation(upload_product.store_validation_failed_message(), "Store Validation Failed")

    @allure.description('Upload a product incorrectly when the user does not have a store and storeID is null')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_upload_product_incorrectly_1(self):
        driver = self.driver
        utils = Utils(driver)
        upload_product = Upload_New_Product_Page(driver)

        upload_product.click_add_new_product_section()
        upload_product.enter_data_to_inputs(['', 'Brands', '0555555555', 'a@trado.com', 'Brands.com', 'Tel-Aviv',
                                             'Herzel', '1'])
        upload_product.click_add_new_product_button()
        driver.implicitly_wait(5)
        utils.validation(upload_product.js_messages_for_all_the_fields(0), 'Please fill out this field.')
        utils.validation(upload_product.enter_the_field_message(0), "נא למלא שדה זה")

    @allure.description('Upload a product incorrectly when the user does not have a store and storeName is null')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_upload_product_incorrectly_2(self):
        driver = self.driver
        utils = Utils(driver)
        upload_product = Upload_New_Product_Page(driver)

        upload_product.click_add_new_product_section()
        upload_product.enter_data_to_inputs(['1', '', '0555555555', 'a@trado.com', 'Brands.com', 'Tel-Aviv',
                                             'Herzel', '1'])
        upload_product.click_add_new_product_button()
        driver.implicitly_wait(5)
        utils.validation(upload_product.js_messages_for_all_the_fields(1), 'Please fill out this field.')
        utils.validation(upload_product.enter_the_field_message(1), "נא למלא שדה זה")

    @allure.description('Upload a product incorrectly when the user does not have a store and phoneNumber is null')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_upload_product_incorrectly_3(self):
        driver = self.driver
        utils = Utils(driver)
        upload_product = Upload_New_Product_Page(driver)

        upload_product.click_add_new_product_section()
        upload_product.enter_data_to_inputs(['1', 'Brands', '', 'a@trado.com', 'Brands.com', 'Tel-Aviv',
                                             'Herzel', '1'])
        upload_product.click_add_new_product_button()
        driver.implicitly_wait(5)
        utils.validation(upload_product.js_messages_for_all_the_fields(2), 'Please fill out this field.')
        utils.validation(upload_product.enter_the_field_message(2), "נא למלא שדה זה")

    @allure.description('Upload a product incorrectly when the user does not have a store and email is null')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_upload_product_incorrectly_4(self):
        driver = self.driver
        utils = Utils(driver)
        upload_product = Upload_New_Product_Page(driver)

        upload_product.click_add_new_product_section()
        upload_product.enter_data_to_inputs(['1', 'Brands', '0555555555', '', 'Brands.com', 'Tel-Aviv',
                                             'Herzel', '1'])
        upload_product.click_add_new_product_button()
        driver.implicitly_wait(5)
        utils.validation(upload_product.js_messages_for_all_the_fields(3), 'Please fill out this field.')
        utils.validation(upload_product.enter_the_field_message(3), "נא למלא שדה זה")

    @allure.description('Upload a product incorrectly when the user does not have a store and webLink is null')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_upload_product_incorrectly_5(self):
        driver = self.driver
        utils = Utils(driver)
        upload_product = Upload_New_Product_Page(driver)

        upload_product.click_add_new_product_section()
        upload_product.enter_data_to_inputs(['1', 'Brands', '0555555555', 'a@trado.com', '', 'Tel-Aviv',
                                             'Herzel', '1'])
        upload_product.click_add_new_product_button()
        driver.implicitly_wait(5)
        utils.validation(upload_product.js_messages_for_all_the_fields(4), 'Please fill out this field.')
        utils.validation(upload_product.enter_the_field_message(4), "נא למלא שדה זה")

    @allure.description('Upload a product incorrectly when the user does not have a store and cityName is null')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_upload_product_incorrectly_6(self):
        driver = self.driver
        utils = Utils(driver)
        upload_product = Upload_New_Product_Page(driver)

        upload_product.click_add_new_product_section()
        upload_product.enter_data_to_inputs(['1', 'Brands', '0555555555', 'a@trado.com', 'Brands.com', '',
                                             'Herzel', '1'])
        upload_product.click_add_new_product_button()
        driver.implicitly_wait(5)
        utils.validation(upload_product.js_messages_for_all_the_fields(5), 'Please fill out this field.')
        utils.validation(upload_product.enter_the_field_message(5), "נא למלא שדה זה")

    @allure.description('Upload a product incorrectly when the user does not have a store and addressName is null')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_upload_product_incorrectly_7(self):
        driver = self.driver
        utils = Utils(driver)
        upload_product = Upload_New_Product_Page(driver)

        upload_product.click_add_new_product_section()
        upload_product.enter_data_to_inputs(['1', 'Brands', '0555555555', 'a@trado.com', 'Brands.com', 'Tel-Aviv',
                                             '', '1'])
        upload_product.click_add_new_product_button()
        driver.implicitly_wait(5)
        utils.validation(upload_product.js_messages_for_all_the_fields(6), 'Please fill out this field.')
        utils.validation(upload_product.enter_the_field_message(6), "נא למלא שדה זה")

    @allure.description('Upload a product incorrectly when the user does not have a store and streetNumber is null')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_upload_product_incorrectly_8(self):
        driver = self.driver
        utils = Utils(driver)
        upload_product = Upload_New_Product_Page(driver)

        upload_product.click_add_new_product_section()
        upload_product.enter_data_to_inputs(['1', 'Brands', '0555555555', 'a@trado.com', 'Brands.com', 'Tel-Aviv',
                                             'Herzel', ''])
        upload_product.click_add_new_product_button()
        driver.implicitly_wait(5)
        utils.validation(upload_product.js_messages_for_all_the_fields(7), 'Please fill out this field.')
        utils.validation(upload_product.enter_the_field_message(7), "נא למלא שדה זה")