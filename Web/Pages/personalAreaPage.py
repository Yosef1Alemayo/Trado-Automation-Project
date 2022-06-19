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

    def enter_first_name(self, first_name):
        self.driver.find_element(By.XPATH, self.first_name).clear()
        self.driver.find_element(By.XPATH, self.first_name).send_keys(first_name)
        # Util = Utils(self.driver)
        # Util.validation(self.enter_first_name())
        time.sleep(3)

    def enter_last_name(self, last_name):
        self.driver.find_element(By.XPATH, self.last_name).clear()
        self.driver.find_element(By.XPATH, self.last_name).send_keys(last_name)
        time.sleep(3)

    def enter_phone(self, phone):
        # self.driver.find_element(By.XPATH, self.phone).clear()
        self.driver.find_element(By.XPATH, self.phone).send_keys(phone)
        Util = Utils(self.driver)
        Util.validation(self.phone)

    def enter_email(self, email):
        self.driver.find_element(By.XPATH, self.email).clear()
        self.driver.find_element(By.XPATH, self.email).send_keys(email)

    def enter_id(self, id):
        self.driver.find_element(By.XPATH, self.id).clear()
        self.driver.find_element(By.XPATH, self.id).send_keys(id)
        # time.sleep(3)

    def enter_city(self, city):
        self.driver.find_element(By.XPATH, self.city).clear()
        self.driver.find_element(By.XPATH, self.city).send_keys(city)
        # time.sleep(3)

    def enter_number(self, number,select):
        self.driver.find_element(By.XPATH, self.number).clear()

        # self.driver.execute_script(f"document.getElementsByClassName('input_input ')[2].value = '{number}'")

        # self.Select(self.driver.find_element(By.XPATH, number))
        # select.select_by_index(2)

        # self.driver.find_element(By.XPATH,self.number).send_keys(number)
        time.sleep(3)

    def click_Edit_button(self):
        self.driver.find_element(By.XPATH, self.Edit_button).click()

    def click_Save_button(self):
        self.driver.find_element(By.XPATH, self.Save_button).click()




