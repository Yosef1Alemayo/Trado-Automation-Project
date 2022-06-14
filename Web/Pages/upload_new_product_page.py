from Web.Utils.utils import Utils
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Web.Locators.upload_product_locators import Upload_New_Product_Locators

class Upload_New_Product_Page:

    def __init__(self, driver):
        self.driver = driver
        self.Inputs = Upload_New_Product_Locators.NEW_PRODUCT_FIELDS  # 8 Inputs
        self.addNewProductSection = Upload_New_Product_Locators.ADD_NEW_PRODUCT_SECTION  # Navigate to Add Product
        self.addNewProductButton = Upload_New_Product_Locators.ADD_NEW_PRODUCT_BUTTON  # Add Button
        self.validationFailed = Upload_New_Product_Locators.STORE_VALIDATION_FAILED

    def click_add_new_product_section(self):
        utils = Utils(self.driver)
        section = self.driver.find_element(By.XPATH, self.addNewProductSection)
        section.click()
        utils.validation(section.get_attribute('innerText'), "+ העלאת מוצר חדש")

    def inputs_fields(self):
        utils = Utils(self.driver)
        fields = self.driver.find_elements(By.CSS_SELECTOR, self.Inputs)
        utils.validation(len(fields), 8)
        return fields

    def click_add_new_product_button(self):
        add_button = self.driver.find_element(By.CSS_SELECTOR, self.addNewProductButton)
        add_button.click()

    def enter_data_to_inputs(self, data: list):
        utils = Utils(self.driver)
        fields = self.inputs_fields()
        if len(fields) == 8:
            for field in range(len(fields)):
                fields[field].clear()
                fields[field].send_keys(data[field])
                utils.validation(fields[field].get_attribute('value'), data[field])

    """ Messages: """
    def js_messages_for_the_fields(self, num):
        fields = self.inputs_fields()
        return fields[num].get_attribute('validationMessage')

    def store_validation_failed_message(self):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.validationFailed)))
        return self.driver.find_element(By.CSS_SELECTOR, self.validationFailed).get_attribute('innerText')
