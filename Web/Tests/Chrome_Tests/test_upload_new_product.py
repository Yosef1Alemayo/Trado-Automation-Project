import allure
import pytest
from Web.Pages.upload_new_product_page import Upload_New_Product_Page
from Web.Utils.PreConditions.precondition_tsiona import Pre_Condition_Tsiona
from Web.Utils.utils import Utils

@pytest.mark.usefixtures('login')
class Test_Upload_New_Product(Pre_Condition_Tsiona):

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


    def test1(self):
        pass

    def test2(self):
        pass

    def test11(self):
        pass

    def test21(self):
        pass
