import allure
import pytest
from Web.Pages.upload_new_product_page import Upload_New_Product_Page
from Web.Pages.upload_new_product_page import Upload_Product_with_Store
from Web.Utils.PreConditions.precondition import Pre_Condition
from Server.DB.main import query_for_products_details
from Web.Utils.utils import Utils

""" All the Tests when User Hasn't Store """
@pytest.mark.usefixtures('login_tsiona')
class Test_Upload_New_Product0(Pre_Condition):
    @pytest.mark.sanity
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

    @pytest.mark.regression
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

    @pytest.mark.regression
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

    @pytest.mark.regression
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

    @allure.description('Upload a product incorrectly when the user does not have a store and email is Invalid(Chars)')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_upload_product_incorrectly_9(self):
        driver = self.driver
        utils = Utils(driver)
        upload_product = Upload_New_Product_Page(driver)

        upload_product.click_add_new_product_section()
        data = ['1', 'Brands', '0555555555', 'aaa', 'Brands.com', 'Tel-Aviv', 'Herzel', '1']
        upload_product.enter_data_to_inputs(data)
        upload_product.click_add_new_product_button()
        driver.implicitly_wait(5)
        utils.validation(upload_product.js_messages_for_all_the_fields(3), "Please include an '@' in the email "
                                                                           f"address. '{data[3]}' is missing an '@'.")
        utils.validation(upload_product.enter_the_field_message(3), "דוא״ל לא תקין")

    @allure.description('Upload a product incorrectly when the user does not have a store and email is Invalid(Chars@)')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_upload_product_incorrectly_10(self):
        driver = self.driver
        utils = Utils(driver)
        upload_product = Upload_New_Product_Page(driver)

        upload_product.click_add_new_product_section()
        data = ['1', 'Brands', '0555555555', 'aaa@', 'Brands.com', 'Tel-Aviv', 'Herzel', '1']
        upload_product.enter_data_to_inputs(data)
        upload_product.click_add_new_product_button()
        driver.implicitly_wait(5)
        utils.validation(upload_product.js_messages_for_all_the_fields(3),
                         f"Please enter a part following '@'. '{data[3]}' is incomplete.")
        utils.validation(upload_product.enter_the_field_message(3), "דוא״ל לא תקין")

    @allure.description('Upload a product incorrectly when the user does not have a store and email is Invalid(Chars+.')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_upload_product_incorrectly_11(self):
        driver = self.driver
        utils = Utils(driver)
        upload_product = Upload_New_Product_Page(driver)

        upload_product.click_add_new_product_section()
        data = ['1', 'Brands', '0555555555', 'aaa@as.', 'Brands.com', 'Tel-Aviv', 'Herzel', '1']
        upload_product.enter_data_to_inputs(data)
        upload_product.click_add_new_product_button()
        driver.implicitly_wait(5)
        utils.validation(upload_product.js_messages_for_all_the_fields(3),
                         f"'.' is used at a wrong position in '{upload_product.js_email_msg_point(data[3])}'.")
        utils.validation(upload_product.enter_the_field_message(3), "דוא״ל לא תקין")

    @allure.description('Upload a product incorrectly when the user does not have a store and phone is Invalid (+) ')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_upload_product_incorrectly_12(self):
        driver = self.driver
        utils = Utils(driver)
        upload_product = Upload_New_Product_Page(driver)

        upload_product.click_add_new_product_section()
        data = ['1', 'Brands', '11111111111', 'av@d.ff', 'Brands.com', 'Tel-Aviv', 'Herzel', '1']
        upload_product.enter_data_to_inputs(data)
        upload_product.click_add_new_product_button()
        driver.implicitly_wait(5)
        utils.validation(upload_product.enter_the_field_message(2), "מס׳ טלפון לא תקין")

    @allure.description('Upload a product incorrectly when the user does not have a store and phone is Invalid (-)')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_upload_product_incorrectly_13(self):
        driver = self.driver
        utils = Utils(driver)
        upload_product = Upload_New_Product_Page(driver)

        upload_product.click_add_new_product_section()
        data = ['1', 'Brands', '12', 'av@d.ff', 'Brands.com', 'Tel-Aviv', 'Herzel', '1']
        upload_product.enter_data_to_inputs(data)
        upload_product.click_add_new_product_button()
        driver.implicitly_wait(5)
        utils.validation(upload_product.enter_the_field_message(2), "מס׳ טלפון לא תקין")


""" All the Tests when User has a Store """
@pytest.mark.usefixtures('login_yosef')
class Test_Upload_New_Product1(Pre_Condition):
    @pytest.mark.sanity
    @allure.description('Upload a product correctly when all the fields are full')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_upload_product_correctly1(self):
        driver = self.driver
        utils = Utils(driver)
        upload_product = Upload_Product_with_Store(driver)
        ''' Page1'''
        upload_product.click_add_new_product_section()
        upload_product.enter_data_to_inputs(6, ['261196', 'Galax', 'LG', 'LG-ELEC', '', '15'])
        upload_product.click_on_upload_image("C:/Users/yossi/Desktop/Image.jpg")
        upload_product.fill_checkbox()
        upload_product.click_add_new_product_button()
        ''' Page2'''
        upload_product.enter_data_to_inputs(3, ['15', '5', '3'])
        upload_product.click_add_new_product_button()
        ''' Page3'''
        upload_product.enter_data_to_inputs(8, ['רחובות', 'הרצל', '25', 'ב', 'יבואן מקביל', '3', 'אבי', '0521111111'])
        upload_product.click_plus_button(3)
        upload_product.click_minus_button(1)
        utils.validation(upload_product.amount_of_days(), 3-1)
        upload_product.click_add_new_product_button()
        ''' Asserts '''
        utils.validation(upload_product.upload_prod_successfully(), 'מוצר התווסף בהצלחה')
        db_query1 = query_for_products_details('Galax', 'name')
        db_query2 = query_for_products_details('Galax', 'barcode')
        db_query3 = query_for_products_details('Galax', 'price')
        utils.validation(db_query1, 'Galax')
        utils.validation(db_query2, '261196')
        utils.validation(db_query3, '15')

    @pytest.mark.sanity
    @allure.description('Upload a product correctly without Image')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_upload_product_correctly2(self):
        driver = self.driver
        utils = Utils(driver)
        upload_product = Upload_Product_with_Store(driver)
        '''Page1'''
        upload_product.click_add_new_product_section()
        upload_product.enter_data_to_inputs(6, ['261196', 'Betty', 'LG', 'LG-ELEC', '', '15'])
        upload_product.fill_checkbox()
        upload_product.click_add_new_product_button()
        '''Page2'''
        upload_product.enter_data_to_inputs(3, ['15', '5', '3'])
        upload_product.click_add_new_product_button()
        '''Page3'''
        upload_product.enter_data_to_inputs(8, ['רחובות', 'הרצל', '25', 'ב', 'יבואן מקביל', '3', 'אבי', '0521111111'])
        upload_product.click_plus_button(3)
        upload_product.click_minus_button(1)
        utils.validation(upload_product.amount_of_days(), 3-1)
        upload_product.click_add_new_product_button()
        '''Asserts'''
        utils.validation(upload_product.upload_prod_successfully(), 'מוצר התווסף בהצלחה')
        db_query1 = query_for_products_details('Betty', 'name')
        db_query2 = query_for_products_details('Betty', 'barcode')
        db_query3 = query_for_products_details('Betty', 'price')
        utils.validation(db_query1, 'Betty')
        utils.validation(db_query2, '261196')
        utils.validation(db_query3, '15')

    @pytest.mark.sanity
    @allure.description('Upload a product correctly without Image and without Business days')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_upload_product_correctly3(self):
        driver = self.driver
        utils = Utils(driver)
        upload_product = Upload_Product_with_Store(driver)
        '''Page1'''
        upload_product.click_add_new_product_section()
        upload_product.enter_data_to_inputs(6, ['261196', 'Floor', 'BMW', 'BMW-MOTORS', '', '1500'])
        upload_product.fill_checkbox()
        upload_product.click_add_new_product_button()
        '''Page2'''
        upload_product.enter_data_to_inputs(3, ['15', '5', '3'])
        upload_product.click_add_new_product_button()
        '''Page3'''
        upload_product.enter_data_to_inputs(8, ['רחובות', 'הרצל', '25', 'ב', 'יבואן מקביל', '3', 'אבי', '0521111111'])
        upload_product.click_add_new_product_button()
        '''Asserts'''
        utils.validation(upload_product.upload_prod_successfully(), "מוצר התווסף בהצלחה")
        db_query1 = query_for_products_details('Floor', 'name')
        db_query2 = query_for_products_details('Floor', 'barcode')
        db_query3 = query_for_products_details('Floor', 'price')
        utils.validation(db_query1, 'Floor')
        utils.validation(db_query2, '261196')
        utils.validation(db_query3, '1500')

    @pytest.mark.sanity
    @allure.description('Upload a product correctly only with the requirements fields')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_upload_product_correctly4(self):
        driver = self.driver
        utils = Utils(driver)
        upload_product = Upload_Product_with_Store(driver)
        '''Page1'''
        upload_product.click_add_new_product_section()
        upload_product.enter_data_to_inputs(6, ['261196', 'Rivka', '', '', '', '1500'])
        upload_product.fill_checkbox()
        upload_product.click_add_new_product_button()
        '''Page2'''
        upload_product.enter_data_to_inputs(3, ['15', '5', '3'])
        upload_product.click_add_new_product_button()
        '''Page3'''
        upload_product.enter_data_to_inputs(8, ['', '', '', '', 'יבואן מקביל', '', '', '0521111111'])
        upload_product.click_add_new_product_button()
        '''Asserts'''
        utils.validation(upload_product.upload_prod_successfully(), "מוצר התווסף בהצלחה")
        db_query1 = query_for_products_details('Rivka', 'name')
        db_query2 = query_for_products_details('Rivka', 'barcode')
        db_query3 = query_for_products_details('Rivka', 'price')
        utils.validation(db_query1, 'Rivka')
        utils.validation(db_query2, '261196')
        utils.validation(db_query3, '1500')

    @pytest.mark.sanity
    @allure.description('Upload a product correctly with Weight')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_upload_product_correctly5(self):
        driver = self.driver
        utils = Utils(driver)
        upload_product = Upload_Product_with_Store(driver)
        '''Page1'''
        upload_product.click_add_new_product_section()
        upload_product.enter_data_to_inputs(6, ['261196', 'Asaf', '1', '1', '', '150000'])
        upload_product.fill_checkbox()
        upload_product.click_add_new_product_button()
        '''Page2'''
        upload_product.filter_products(1)
        upload_product.enter_data_to_inputs(2, ['5', '3'])
        upload_product.click_add_new_product_button()
        '''Page3'''
        upload_product.enter_data_to_inputs(8, ['1', '1', '1', '1', 'יבואן מקביל', '1', '1', '0521111111'])
        upload_product.click_add_new_product_button()
        '''Asserts'''
        utils.validation(upload_product.upload_prod_successfully(), "מוצר התווסף בהצלחה")
        db_query1 = query_for_products_details('Asaf', 'name')
        db_query2 = query_for_products_details('Asaf', 'barcode')
        db_query3 = query_for_products_details('Asaf', 'price')
        utils.validation(db_query1, 'Asaf')
        utils.validation(db_query2, '261196')
        utils.validation(db_query3, '150000')

    @allure.description('Upload a product incorrectly - Page1, when barcode field is empty')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_upload_product_incorrectly1(self):
        driver = self.driver
        utils = Utils(driver)
        upload_product = Upload_Product_with_Store(driver)
        '''Page1'''
        upload_product.click_add_new_product_section()
        upload_product.enter_data_to_inputs(6, ['', 'Asaf', '1', '1', '', '150000'])
        upload_product.click_add_new_product_button()
        utils.validation(upload_product.js_messages_for_all_the_fields(6, 0), "Please fill out this field.")
        utils.validation(upload_product.error_message(0), "נא למלא שדה זה")

    @allure.description('Upload a product incorrectly - Page1, when ProductName field is empty')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_upload_product_incorrectly2(self):
        driver = self.driver
        utils = Utils(driver)
        upload_product = Upload_Product_with_Store(driver)
        '''Page1'''
        upload_product.click_add_new_product_section()
        upload_product.enter_data_to_inputs(6, ['123456', '', '1', '1', '', '150000'])
        upload_product.click_add_new_product_button()
        utils.validation(upload_product.js_messages_for_all_the_fields(6, 1), "Please fill out this field.")
        utils.validation(upload_product.error_message(0), "נא למלא שדה זה")

    @pytest.mark.regression
    @allure.description('Upload a product incorrectly - Page1, when Price field is empty')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_upload_product_incorrectly3(self):
        driver = self.driver
        utils = Utils(driver)
        upload_product = Upload_Product_with_Store(driver)
        '''Page1'''
        upload_product.click_add_new_product_section()
        upload_product.enter_data_to_inputs(6, ['123456', 'Joni', '1', '1', '', ''])
        upload_product.click_add_new_product_button()
        utils.validation(upload_product.js_messages_for_all_the_fields(6, 5), "Please fill out this field.")
        utils.validation(upload_product.error_message(0), "נא למלא שדה זה")

    @allure.description('Upload a product incorrectly - Page1, when all the Required field is empty')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_upload_product_incorrectly4(self):
        driver = self.driver
        utils = Utils(driver)
        upload_product = Upload_Product_with_Store(driver)
        '''Page1'''
        upload_product.click_add_new_product_section()
        upload_product.enter_data_to_inputs(6, ['', '', '1', '1', '', ''])
        upload_product.click_add_new_product_button()
        utils.validation(upload_product.js_messages_for_all_the_fields(6, 0), "Please fill out this field.")
        utils.validation(upload_product.js_messages_for_all_the_fields(6, 1), "Please fill out this field.")
        utils.validation(upload_product.js_messages_for_all_the_fields(6, 5), "Please fill out this field.")
        utils.validation(upload_product.error_message(0), "נא למלא שדה זה")
        utils.validation(upload_product.error_message(1), "נא למלא שדה זה")
        utils.validation(upload_product.error_message(2), "נא למלא שדה זה")

    @pytest.mark.regression
    @allure.description('Upload a product incorrectly - Page2, when cartonAmount field is empty')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_upload_product_incorrectly5(self):
        driver = self.driver
        utils = Utils(driver)
        upload_product = Upload_Product_with_Store(driver)
        '''Page1'''
        upload_product.click_add_new_product_section()
        upload_product.enter_data_to_inputs(6, ['261196', 'Floor', 'BMW', 'BMW-MOTORS', '', '1500'])
        upload_product.fill_checkbox()
        upload_product.click_add_new_product_button()
        '''Page2'''
        upload_product.enter_data_to_inputs(3, ['', '5', '3'])
        upload_product.click_add_new_product_button()
        utils.validation(upload_product.js_messages_for_all_the_fields(3, 0), "Please fill out this field.")
        utils.validation(upload_product.error_message(0), "נא למלא שדה זה")

    @allure.description('Upload a product incorrectly - Page2, when unitsInStock field is empty')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_upload_product_incorrectly6(self):
        driver = self.driver
        utils = Utils(driver)
        upload_product = Upload_Product_with_Store(driver)
        '''Page1'''
        upload_product.click_add_new_product_section()
        upload_product.enter_data_to_inputs(6, ['261196', 'Floor', 'BMW', 'BMW-MOTORS', '', '1500'])
        upload_product.fill_checkbox()
        upload_product.click_add_new_product_button()
        '''Page2'''
        upload_product.enter_data_to_inputs(3, ['1', '', '3'])
        upload_product.click_add_new_product_button()
        utils.validation(upload_product.js_messages_for_all_the_fields(3, 1), "Please fill out this field.")
        utils.validation(upload_product.error_message(0), "נא למלא שדה זה")

    @allure.description('Upload a product incorrectly - Page2, when minimumCartons field is empty')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_upload_product_incorrectly7(self):
        driver = self.driver
        utils = Utils(driver)
        upload_product = Upload_Product_with_Store(driver)
        '''Page1'''
        upload_product.click_add_new_product_section()
        upload_product.enter_data_to_inputs(6, ['261196', 'Floor', 'BMW', 'BMW-MOTORS', '', '1500'])
        upload_product.fill_checkbox()
        upload_product.click_add_new_product_button()
        '''Page2'''
        upload_product.enter_data_to_inputs(3, ['1', '1', ''])
        upload_product.click_add_new_product_button()
        utils.validation(upload_product.js_messages_for_all_the_fields(3, 2), "Please fill out this field.")
        utils.validation(upload_product.error_message(0), "נא למלא שדה זה")

    @allure.description('Upload a product incorrectly - Page2, when all the required fields is empty')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_upload_product_incorrectly8(self):
        driver = self.driver
        utils = Utils(driver)
        upload_product = Upload_Product_with_Store(driver)
        '''Page1'''
        upload_product.click_add_new_product_section()
        upload_product.enter_data_to_inputs(6, ['261196', 'Floor', 'BMW', 'BMW-MOTORS', '', '1500'])
        upload_product.fill_checkbox()
        upload_product.click_add_new_product_button()
        '''Page2'''
        upload_product.enter_data_to_inputs(3, ['', '', ''])
        upload_product.click_add_new_product_button()
        utils.validation(upload_product.js_messages_for_all_the_fields(3, 0), "Please fill out this field.")
        utils.validation(upload_product.js_messages_for_all_the_fields(3, 1), "Please fill out this field.")
        utils.validation(upload_product.js_messages_for_all_the_fields(3, 2), "Please fill out this field.")
        utils.validation(upload_product.error_message(0), "נא למלא שדה זה")
        utils.validation(upload_product.error_message(1), "נא למלא שדה זה")
        utils.validation(upload_product.error_message(2), "נא למלא שדה זה")

    @pytest.mark.regression
    @allure.description('Upload a product incorrectly - Page2 , when AverageWeight field is empty')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_upload_product_correctly9(self):
        driver = self.driver
        utils = Utils(driver)
        upload_product = Upload_Product_with_Store(driver)
        '''Page1'''
        upload_product.click_add_new_product_section()
        upload_product.enter_data_to_inputs(6, ['261196', 'Asaf', '1', '1', '', '150000'])
        upload_product.fill_checkbox()
        upload_product.click_add_new_product_button()
        '''Page2'''
        upload_product.filter_products(1)
        upload_product.enter_data_to_inputs(2, ['', '3'])
        upload_product.click_add_new_product_button()
        utils.validation(upload_product.js_messages_for_all_the_fields(2, 0), "Please fill out this field.")
        utils.validation(upload_product.error_message(0), "נא למלא שדה זה")

    @allure.description('Upload a product incorrectly - Page2 , when Unit of measure field is empty')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_upload_product_correctly10(self):
        driver = self.driver
        utils = Utils(driver)
        upload_product = Upload_Product_with_Store(driver)
        '''Page1'''
        upload_product.click_add_new_product_section()
        upload_product.enter_data_to_inputs(6, ['261196', 'Asaf', '1', '1', '', '150000'])
        upload_product.fill_checkbox()
        upload_product.click_add_new_product_button()
        '''Page2'''
        upload_product.filter_products(1)
        upload_product.enter_data_to_inputs(2, ['1', ''])
        upload_product.click_add_new_product_button()
        utils.validation(upload_product.js_messages_for_all_the_fields(2, 1), "Please fill out this field.")
        utils.validation(upload_product.error_message(0), "נא למלא שדה זה")

    @allure.description('Upload a product incorrectly - Page2 , when all the required fields is empty')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_upload_product_correctly11(self):
        driver = self.driver
        utils = Utils(driver)
        upload_product = Upload_Product_with_Store(driver)
        '''Page1'''
        upload_product.click_add_new_product_section()
        upload_product.enter_data_to_inputs(6, ['261196', 'Asaf', '1', '1', '', '150000'])
        upload_product.fill_checkbox()
        upload_product.click_add_new_product_button()
        '''Page2'''
        upload_product.filter_products(1)
        upload_product.enter_data_to_inputs(2, ['', ''])
        upload_product.click_add_new_product_button()
        utils.validation(upload_product.js_messages_for_all_the_fields(2, 0), "Please fill out this field.")
        utils.validation(upload_product.js_messages_for_all_the_fields(2, 1), "Please fill out this field.")
        utils.validation(upload_product.error_message(0), "נא למלא שדה זה")
        utils.validation(upload_product.error_message(1), "נא למלא שדה זה")
