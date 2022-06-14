import allure
import pytest
from Web.Pages.upload_new_product_page import Upload_New_Product_Page
from Web.Utils.PreConditions.pre_condition import Precondition_Chrome
from Web.Utils.utils import Utils

@pytest.mark.usefixtures('login_correctly')
class Test_Upload_New_Product(Precondition_Chrome):

    @allure.description('Upload a product when the user does not have a store')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_upload_product_incorrectly_without_store(self, login_correctly):
        """The Driver And The PreCondition("Login Correctly") - What is the Requirements for ?"""
        driver = self.driver
        utils = Utils(driver)
        upload_product = Upload_New_Product_Page(driver)

        upload_product.click_add_new_product_section()
        upload_product.enter_data_to_inputs(['1', 'Brands', '0555555555', 'a@trado.com', 'Brands.com', 'Tel-Aviv',
                                             'Herzel', '1'])
        upload_product.click_add_new_product_button()
        driver.implicitly_wait(5)
        utils.validation(upload_product.store_validation_failed_message(), "Store Validation Failed")

    def test_upload_product_incorrectly_when_store_id_is_null(self, login_correctly):
        """Need To add The errorMessage:נא למלא שדה זה """
        driver = self.driver
        utils = Utils(driver)
        upload_product = Upload_New_Product_Page(driver)

        upload_product.click_add_new_product_section()
        upload_product.enter_data_to_inputs(['', 'Brands', '0555555555', 'a@trado.com', 'Brands.com', 'Tel-Aviv',
                                             'Herzel', '1'])
        upload_product.click_add_new_product_button()
        utils.validation(upload_product.js_messages_for_the_fields(0), 'Please fill out this field.')

    def test_upload_product_incorrectly_when_store_name_is_null(self, login_correctly):
        """Need To add The errorMessage:נא למלא שדה זה """
        driver = self.driver
        utils = Utils(driver)
        upload_product = Upload_New_Product_Page(driver)

        upload_product.click_add_new_product_section()
        upload_product.enter_data_to_inputs(['1', '', '0555555555', 'a@trado.com', 'Brands.com', 'Tel-Aviv',
                                             'Herzel', '1'])
        upload_product.click_add_new_product_button()
        utils.validation(upload_product.js_messages_for_the_fields(1), 'Please fill out this field.')

    def test_upload_product_incorrectly_when_phone_is_null(self, login_correctly):
        """Need To add The errorMessage:נא למלא שדה זה and add test on the phone len"""
        driver = self.driver
        utils = Utils(driver)
        upload_product = Upload_New_Product_Page(driver)

        upload_product.click_add_new_product_section()
        upload_product.enter_data_to_inputs(['1', 'Brands', '', 'a@trado.com', 'Brands.com', 'Tel-Aviv',
                                             'Herzel', '1'])
        upload_product.click_add_new_product_button()
        utils.validation(upload_product.js_messages_for_the_fields(2), 'Please fill out this field.')

    def test_upload_product_incorrectly_when_email_is_null(self, login_correctly):
        """Need To add The errorMessage:נא למלא שדה זה """
        driver = self.driver
        utils = Utils(driver)
        upload_product = Upload_New_Product_Page(driver)

        upload_product.click_add_new_product_section()
        upload_product.enter_data_to_inputs(['1', 'Brands', '0555555555', '', 'Brands.com', 'Tel-Aviv',
                                             'Herzel', '1'])
        upload_product.click_add_new_product_button()
        utils.validation(upload_product.js_messages_for_the_fields(3), 'Please fill out this field.')

    def test_upload_product_incorrectly_when_web_link_is_null(self, login_correctly):
        """Need To add The errorMessage:נא למלא שדה זה """
        driver = self.driver
        utils = Utils(driver)
        upload_product = Upload_New_Product_Page(driver)

        upload_product.click_add_new_product_section()
        upload_product.enter_data_to_inputs(['1', 'Brands', '0555555555', 'a@trado.com', '', 'Tel-Aviv',
                                             'Herzel', '1'])
        upload_product.click_add_new_product_button()
        utils.validation(upload_product.js_messages_for_the_fields(4), 'Please fill out this field.')

    def test_upload_product_incorrectly_when_city_name_is_null(self, login_correctly):
        driver = self.driver
        utils = Utils(driver)
        upload_product = Upload_New_Product_Page(driver)

        upload_product.click_add_new_product_section()
        upload_product.enter_data_to_inputs(['1', 'Brands', '0555555555', 'a@trado.com', 'Brands.com', '',
                                             'Herzel', '1'])
        upload_product.click_add_new_product_button()
        utils.validation(upload_product.js_messages_for_the_fields(5), 'Please fill out this field.')

    def test_upload_product_incorrectly_when_address_is_null(self, login_correctly):
        driver = self.driver
        utils = Utils(driver)
        upload_product = Upload_New_Product_Page(driver)

        upload_product.click_add_new_product_section()
        upload_product.enter_data_to_inputs(['1', 'Brands', '0555555555', 'a@trado.com', 'Brands.com', 'Tel-Aviv',
                                             '', '1'])
        upload_product.click_add_new_product_button()
        utils.validation(upload_product.js_messages_for_the_fields(6), 'Please fill out this field.')

    def test_upload_product_incorrectly_when_number_address_is_null(self, login_correctly):
        driver = self.driver
        utils = Utils(driver)
        upload_product = Upload_New_Product_Page(driver)

        upload_product.click_add_new_product_section()
        upload_product.enter_data_to_inputs(['1', 'Brands', '0555555555', 'a@trado.com', 'Brands.com', 'Tel-Aviv',
                                             'Herzel', ''])
        upload_product.click_add_new_product_button()
        utils.validation(upload_product.js_messages_for_the_fields(7), 'Please fill out this field.')

    def test1(self, login_correctly):
        pass



