import allure
from selenium.webdriver.common.by import By
from Web.Locators.MaxBussines_Locators import MaxBussinesLocators
from Web.Pages.commonQuestion_Page import CommonQuePage
from Web.Utils.utils import Utils


class MaxBussinesPage(CommonQuePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.maxlink = MaxBussinesLocators.maxLink
        self.firstname = MaxBussinesLocators.firstName_field
        self.lastname = MaxBussinesLocators.lastName_field
        self.phoneNumber = MaxBussinesLocators.phone
        self.address = MaxBussinesLocators.city_street
        self.streetNumber = MaxBussinesLocators.street_number
        self.businesName = MaxBussinesLocators.bussines_name
        self.businesID = MaxBussinesLocators.bussines_name
        self.postalCode = MaxBussinesLocators.postal_code
        self.sendButton = MaxBussinesLocators.send_button
        self.max_Business = MaxBussinesLocators.max_business


    @allure.step("Click on 'Signin' to max business")
    def click_link(self):
        self.driver.find_element(By.XPATH, self.maxlink).click()

    @allure.step("Enter first name as {1}")
    def enter_firstname(self, fname):
        self.driver.find_element(By.XPATH, self.firstname).clear()
        self.driver.find_element(By.XPATH, self.firstname).send_keys(fname)

    @allure.step("Enter last name as {1}")
    def enter_lastname(self, lname):
        self.driver.find_element(By.XPATH, self.lastname).clear()
        self.driver.find_element(By.XPATH, self.lastname).send_keys(lname)

    @allure.step("Enter phone number as {1}")
    def enter_phoneNumber(self, Phone):
        self.driver.find_element(By.XPATH, self.phoneNumber).clear()
        self.driver.find_element(By.XPATH, self.phoneNumber).send_keys(Phone)

    @allure.step("Enter address as {1}")
    def enter_address(self, address):
        self.driver.find_element(By.XPATH, self.address).clear()
        self.driver.find_element(By.XPATH, self.address).send_keys(address)

    @allure.step("Enter street number as {1}")
    def enter_stNumber(self, stNumber):
        self.driver.find_element(By.XPATH, self.streetNumber).clear()
        self.driver.find_element(By.XPATH, self.streetNumber).send_keys(stNumber)

    @allure.step("Enter business name as {1}")
    def enter_bussinesName(self, bussinesname):
        self.driver.find_element(By.XPATH, self.businesName).clear()
        self.driver.find_element(By.XPATH, self.businesName).send_keys(bussinesname)

    @allure.step("Enter business ID as {1}")
    def enter_bussinesID(self, bussinesID):
        self.driver.find_element(By.XPATH, self.businesID).clear()
        self.driver.find_element(By.XPATH, self.businesID).send_keys(bussinesID)

    @allure.step("Enter postal code as {1}")
    def enter_postalCode(self, postalCode):
        self.driver.find_element(By.XPATH, self.postalCode).clear()
        self.driver.find_element(By.XPATH, self.postalCode).send_keys(postalCode)

    @allure.step("Click on send details")
    def click_send(self):
        self.driver.find_element(By.CLASS_NAME, self.sendButton).is_enabled()

    def signin_maxBussines(self, fname, lname, phone, address, stNumber, bussinesname, bussinesID, postalCode):
        util = Utils(self.driver)
        self.click_link()
        util.validation(self.maxlink, self.max_Business)
        self.enter_firstname(fname)
        self.enter_lastname(lname)
        self.enter_phoneNumber(phone)
        self.enter_address(address)
        self.enter_stNumber(stNumber)
        self.enter_bussinesName(bussinesname)
        self.enter_bussinesID(bussinesID)
        self.enter_postalCode(postalCode)
        self.click_send()
