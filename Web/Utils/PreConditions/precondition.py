from time import sleep
import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from Server.DB.main import query_for_login_code
from Web.Utils.PreConditions.pre_conditions_locators import PreCondition_Locators
from Web.Base.ChromeBase.chrome_base import Base_Chrome
from Web.Base.FireFoxBase.firefox_base import Base_FireFox
from Web.Utils.utils import Utils

class Pre_Condition(Base_Chrome):

    def click_restaurants(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.presence_of_element_located((By.XPATH, PreCondition_Locators.RESTAURANTS)))
        if None:
            self.driver.refresh()
        else:
            self.driver.find_element(By.XPATH, PreCondition_Locators.RESTAURANTS).click()

    def click_cocktails(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.presence_of_element_located((By.XPATH, PreCondition_Locators.COCKTAILS)))
        self.driver.find_element(By.XPATH, PreCondition_Locators.COCKTAILS).click()

    def click_save_button(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, PreCondition_Locators.SAVE_BUTTON)))
        self.driver.find_element(By.CSS_SELECTOR, PreCondition_Locators.SAVE_BUTTON).click()

    def click_login_section(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.presence_of_element_located((By.XPATH, PreCondition_Locators.LOGIN_SECTION)))
        self.driver.find_element(By.XPATH, PreCondition_Locators.LOGIN_SECTION).click()

    def enter_phone(self, phone_number):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.presence_of_element_located((By.XPATH, PreCondition_Locators.PHONE_FIELD)))
        self.driver.find_element(By.XPATH, PreCondition_Locators.PHONE_FIELD).send_keys(phone_number)

    def click_connect(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, PreCondition_Locators.CONNECT_BUTTON)))
        self.driver.find_element(By.CSS_SELECTOR, PreCondition_Locators.CONNECT_BUTTON).click()

    def enter_sms_code(self, sms_code):
        utils = Utils(self.driver)
        div = self.driver.find_element(By.CSS_SELECTOR, PreCondition_Locators.PASSWORD_FIELD)
        inputs = div.find_elements(By.TAG_NAME, 'input')
        for digit, place in zip(sms_code, inputs):
            place.send_keys(digit)
            utils.validation(place.get_attribute('value'), digit)

    @pytest.mark.usefixtures('set_up_chrome')
    @pytest.fixture
    def login_tsiona(self, set_up_chrome):
        self.click_restaurants()
        self.click_cocktails()
        self.click_save_button()
        self.click_login_section()
        self.enter_phone('0526050731')
        self.click_connect()
        sms = query_for_login_code('0526050731')
        sleep(5)
        self.enter_sms_code(sms)
        self.click_connect()

    @pytest.mark.usefixtures('set_up_chrome')
    @pytest.fixture
    def login_yosef(self, set_up_chrome):
        self.click_restaurants()
        self.click_cocktails()
        self.click_save_button()
        self.click_login_section()
        self.enter_phone('0525393079')
        self.click_connect()
        sms = query_for_login_code('0525393079')
        sleep(5)
        self.enter_sms_code(sms)
        self.click_connect()

    @pytest.mark.usefixtures('set_up_chrome')
    @pytest.fixture
    def login_betty(self, set_up_chrome):
        self.click_restaurants()
        self.click_cocktails()
        self.click_save_button()
        self.click_login_section()
        self.enter_phone('0505864555')
        self.click_connect()
        sms = query_for_login_code('0505864555')
        sleep(5)
        self.enter_sms_code(sms)
        self.click_connect()

    @pytest.mark.usefixtures('set_up_chrome')
    @pytest.fixture
    def login_jonathan(self, set_up_chrome):
        self.click_restaurants()
        self.click_cocktails()
        self.click_save_button()
        self.click_login_section()
        self.enter_phone('0522578853')
        self.click_connect()
        sms = query_for_login_code('0522578853')
        sleep(5)
        self.enter_sms_code(sms)
        self.click_connect()

class Pre_Condition1(Base_FireFox):
    def click_restaurants(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.presence_of_element_located((By.XPATH, PreCondition_Locators.RESTAURANTS)))
        if None:
            self.driver.refresh()
        else:
            self.driver.find_element(By.XPATH, PreCondition_Locators.RESTAURANTS).click()

    def click_cocktails(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.presence_of_element_located((By.XPATH, PreCondition_Locators.COCKTAILS)))
        self.driver.find_element(By.XPATH, PreCondition_Locators.COCKTAILS).click()

    def click_save_button(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, PreCondition_Locators.SAVE_BUTTON)))
        self.driver.find_element(By.CSS_SELECTOR, PreCondition_Locators.SAVE_BUTTON).click()

    def click_login_section(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.presence_of_element_located((By.XPATH, PreCondition_Locators.LOGIN_SECTION)))
        self.driver.find_element(By.XPATH, PreCondition_Locators.LOGIN_SECTION).click()

    def enter_phone(self, phone_number):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.presence_of_element_located((By.XPATH, PreCondition_Locators.PHONE_FIELD)))
        self.driver.find_element(By.XPATH, PreCondition_Locators.PHONE_FIELD).send_keys(phone_number)

    def click_connect(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, PreCondition_Locators.CONNECT_BUTTON)))
        self.driver.find_element(By.CSS_SELECTOR, PreCondition_Locators.CONNECT_BUTTON).click()

    def enter_sms_code(self, sms_code):
        utils = Utils(self.driver)
        div = self.driver.find_element(By.CSS_SELECTOR, PreCondition_Locators.PASSWORD_FIELD)
        inputs = div.find_elements(By.TAG_NAME, 'input')
        for digit, place in zip(sms_code, inputs):
            place.send_keys(digit)
            utils.validation(place.get_attribute('value'), digit)

    @pytest.mark.usefixtures('set_up_firefox')
    @pytest.fixture
    def login_tsiona(self, set_up_firefox):
        self.click_restaurants()
        self.click_cocktails()
        self.click_save_button()
        self.click_login_section()
        self.enter_phone('0526050731')
        self.click_connect()
        sms = query_for_login_code('0526050731')
        sleep(5)
        self.enter_sms_code(sms)
        self.click_connect()

    @pytest.mark.usefixtures('set_up_firefox')
    @pytest.fixture
    def login_yosef(self, set_up_firefox):
        self.click_restaurants()
        self.click_cocktails()
        self.click_save_button()
        self.click_login_section()
        self.enter_phone('0525393079')
        self.click_connect()
        sms = query_for_login_code('0525393079')
        sleep(5)
        self.enter_sms_code(sms)
        self.click_connect()

    @pytest.mark.usefixtures('set_up_firefox')
    @pytest.fixture
    def login_betty(self, set_up_firefox):
        self.click_restaurants()
        self.click_cocktails()
        self.click_save_button()
        self.click_login_section()
        self.enter_phone('0505864555')
        self.click_connect()
        sms = query_for_login_code('0505864555')
        sleep(5)
        self.enter_sms_code(sms)
        self.click_connect()

    @pytest.mark.usefixtures('set_up_firefox')
    @pytest.fixture
    def login_jonathan(self, set_up_firefox):
        self.click_restaurants()
        self.click_cocktails()
        self.click_save_button()
        self.click_login_section()
        self.enter_phone('0522578853')
        self.click_connect()
        sms = query_for_login_code('0522578853')
        sleep(5)
        self.enter_sms_code(sms)
        self.click_connect()








