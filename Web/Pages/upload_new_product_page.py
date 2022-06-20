import time

from selenium.webdriver.chrome.webdriver import WebDriver
from Web.Utils.utils import Utils
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Web.Locators.upload_product_locators import Upload_New_Product_Locators


class Upload_New_Product_Page:

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.addProductPage = Upload_New_Product_Locators.ADD_PRODUCT_PAGE  # Add Project Page Class
        self.Inputs = Upload_New_Product_Locators.NEW_PRODUCT_FIELDS  # 8 Inputs
        self.addNewProductSection = Upload_New_Product_Locators.ADD_NEW_PRODUCT_SECTION  # Navigate to Add Product
        self.addNewProductButton = Upload_New_Product_Locators.ADD_NEW_PRODUCT_BUTTON  # Add Button
        self.validationFailed = Upload_New_Product_Locators.STORE_VALIDATION_FAILED  # Error Message (No Store)
        self.fieldError = Upload_New_Product_Locators.FILL_THE_FIELD  # Error Message for all The Fields

    def click_add_new_product_section(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, self.addNewProductSection)))
        self.driver.find_element(By.CSS_SELECTOR, self.addNewProductSection).click()
        div = self.driver.find_element(By.CSS_SELECTOR, self.addProductPage)
        wait.until(EC.visibility_of(div))

    def inputs_fields(self):
        utils = Utils(self.driver)
        fields = self.driver.find_elements(By.CSS_SELECTOR, self.Inputs)
        utils.validation(len(fields), 8)
        return fields

    def click_add_new_product_button(self):
        utils = Utils(self.driver)
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, self.addNewProductButton)))
        button = self.driver.find_element(By.CSS_SELECTOR, self.addNewProductButton)
        utils.validation(button.get_attribute('defaultValue'), 'הוספה')
        button.click()

    def enter_data_to_inputs(self, data: list):
        utils = Utils(self.driver)
        fields = self.inputs_fields()
        if len(fields) and len(data) == 8:
            for field in range(len(fields)):
                fields[field].clear()
                fields[field].send_keys(data[field])
                utils.validation(fields[field].get_attribute('value'), data[field])
        else:
            raise ValueError

    """ Messages: """
    def js_messages_for_all_the_fields(self, num):
        fields = self.inputs_fields()
        return fields[num].get_attribute('validationMessage')

    def store_validation_failed_message(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.validationFailed)))
        return self.driver.find_element(By.CSS_SELECTOR, self.validationFailed).get_attribute('innerText')

    def enter_the_field_message(self, num):
        messages = self.driver.find_elements(By.XPATH, self.fieldError)
        return messages[num].get_attribute('innerText')

    @staticmethod
    def js_email_msg_point(text):
        for letter in range(len(text)):
            if text[letter] == '@':
                new = text[letter + 1:]
                return new


class Upload_Product_with_Store:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.addProductPage = Upload_New_Product_Locators.ADD_PRODUCT_PAGE  # Add Project Page Class
        self.Inputs = Upload_New_Product_Locators.NEW_PRODUCT_FIELDS  # 8 Inputs
        self.addNewProductSection = Upload_New_Product_Locators.ADD_NEW_PRODUCT_SECTION  # Navigate to Add Product
        self.addNewProductButton = Upload_New_Product_Locators.ADD_NEW_PRODUCT_BUTTON  # Add Button
        self.validationFailed = Upload_New_Product_Locators.STORE_VALIDATION_FAILED  # Error Message (No Store)
        self.fieldError = Upload_New_Product_Locators.FILL_THE_FIELD  # Error Message for all The Fields
        self.uploadImage = Upload_New_Product_Locators.IMAGE  # Image(need to be with OS)
        self.fillingCheckBox = Upload_New_Product_Locators.CHECKBOX  # Filling The CheckBox
        self.unitsOrWeight = Upload_New_Product_Locators.UNIT_AND_WEIGHT  # Filtering for Upload Product
        self.plusButton = Upload_New_Product_Locators.PLUS_BUTTON  # Click Plus For Business Days
        self.minusButton = Upload_New_Product_Locators.MINUS_BUTTON  # Click Minus For Business Days
        self.amountOfDays = Upload_New_Product_Locators.AMOUNT_OF_DAYS  # The Total Of Business Days

    def click_add_new_product_section(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, self.addNewProductSection)))
        self.driver.find_element(By.CSS_SELECTOR, self.addNewProductSection).click()
        div = self.driver.find_element(By.CSS_SELECTOR, self.addProductPage)
        wait.until(EC.visibility_of(div))

    def inputs_fields(self, length: int):
        utils = Utils(self.driver)
        fields = self.driver.find_elements(By.CSS_SELECTOR, self.Inputs)
        utils.validation(len(fields), length)
        return fields

    def click_add_new_product_button(self):
        utils = Utils(self.driver)
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, self.addNewProductButton)))
        button = self.driver.find_element(By.CSS_SELECTOR, self.addNewProductButton)
        utils.validation(button.get_attribute('defaultValue'), 'הוספה')
        button.click()

    def enter_data_to_inputs(self, length: int, data: list):
        utils = Utils(self.driver)
        fields = self.inputs_fields(length)
        if len(fields) and len(data) == length:
            for field in range(len(fields)):
                fields[field].clear()
                fields[field].send_keys(data[field])
                utils.validation(fields[field].get_attribute('value'), data[field])
        else:
            raise ValueError

    def click_on_upload_image(self):
        image = self.driver.find_element(By.CSS_SELECTOR, self.uploadImage)
        image.click()
        image.send_keys(r'''C:/Users/yossi/Desktop/Image.png''')

    def fill_checkbox(self):
        checkbox = self.driver.find_element(By.XPATH, self.fillingCheckBox)
        checkbox.click()

    """ Product Units/Weight"""

    def filter_products(self, choice: int):
        div = self.driver.find_elements(By.XPATH, self.unitsOrWeight)
        div[choice].click()

    """ Product Details2"""
    def click_plus_button(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.element_to_be_clickable((By.XPATH, self.plusButton)))
        button = self.driver.find_element(By.XPATH, self.plusButton)
        button.click()

    def click_minus_button(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.element_to_be_clickable((By.XPATH, self.minusButton)))
        button = self.driver.find_element(By.XPATH, self.minusButton)
        button.click()

    def amount_of_days(self):
        return self.driver.find_element(By.XPATH, self.amountOfDays).get_attribute('valueAsNumber')

