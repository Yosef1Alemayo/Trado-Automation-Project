from Web.Locators.personalArea_Locators import LocatorArea
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from Web.Utils.utils import Utils


class PageArea:
    def __init__(self, driver):
        self.driver = driver
        self.Personal_area_button = LocatorArea.Personal_area_button
        self.first_name = LocatorArea.first_name
        self.last_name = LocatorArea.last_name
        self.phone = LocatorArea.phone
        self.email = LocatorArea.email
        self.id = LocatorArea.id
        self.city = LocatorArea.city
        self.number = LocatorArea.number
        self.Edit_button = LocatorArea.Edit_button
        self.Save_button = LocatorArea.Save_button

    def Click_Personal_Area(self):
        self.driver.find_element(By.XPATH, self.Personal_area_button).click()

    def enter_first_name(self, first_name1):
        utils = Utils(self.driver)
        first_name = self.driver.find_element(By.XPATH, self.first_name)
        first_name.clear()
        first_name.send_keys(first_name1)
        utils.validation(first_name.get_attribute('value'), first_name1)

    def enter_last_name(self, last_name1):
        utils = Utils(self.driver)
        last_name = self.driver.find_element(By.XPATH, self.last_name)
        last_name.clear()
        last_name.send_keys(last_name1)
        time.sleep(3)
        utils.validation(last_name.get_attribute('value'), last_name1)

    def enter_phone(self, phone1):
        utils = Utils(self.driver)
        phone = self.driver.find_element(By.XPATH,self.phone)
        phone.clear()
        phone.send_keys(phone1)
        utils.validation(phone.get_attribute('value'), phone1)

    def enter_email(self, email1):
        utils = Utils(self.driver)
        email = self.driver.find_element(By.XPATH,self.email)
        email.clear()
        email.send_keys(email1)
        utils.validation(email.get_attribute('value'), email1)

    def enter_id(self, id1):
        utils = Utils(self.driver)
        id = self.driver.find_element(By.XPATH,self.id)
        id.clear()
        id.send_keys(id1)
        utils.validation(id.get_attribute('value'), id1)


    def enter_city(self, city1):
        utils = Utils(self.driver)
        city = self.driver.find_element(By.XPATH,self.city)
        city.clear()
        city.send_keys(city1)
        utils.validation(city.get_attribute('value'), city1)

    def enter_number(self, number1):
        utils = Utils(self.driver)
        number = self.driver.find_element(By.XPATH,self.number)
        number.clear()
        number.send_keys(number1)
        utils.validation(number.get_attribute('value'), number1)

    def click_Edit_button(self):
        self.driver.find_element(By.XPATH, self.Edit_button).click()

    def click_Save_button(self):
        self.driver.find_element(By.XPATH, self.Save_button).click()




