import time
import pytest
from selenium.webdriver.common.by import By
from Server.DB.main import query_for_login_code
from Web.Utils.PreConditions.pre_conditions_locators import PreCondition_Locators
from Web.Base.ChromeBase.chrome_base import Base_Chrome

@pytest.mark.usefixtures('set_up_chrome')
class Pre_Condition_Betty(Base_Chrome):
    @pytest.fixture(autouse=True)
    def login_correctly(self, set_up_chrome):
        driver = self.driver
        driver.find_element(By.XPATH, PreCondition_Locators.RESTAURANTS).click()
        driver.find_element(By.XPATH, PreCondition_Locators.COCKTAILS).click()
        driver.find_element(By.CSS_SELECTOR, PreCondition_Locators.SAVE_BUTTON).click()
        driver.find_element(By.XPATH, PreCondition_Locators.LOGIN_SECTION).click()
        driver.find_element(By.XPATH, PreCondition_Locators.PHONE_FIELD).send_keys('0505864555')
        connect = driver.find_element(By.CSS_SELECTOR, PreCondition_Locators.CONNECT_BUTTON)
        connect.click()
        sms_code = query_for_login_code('0505864555')
        time.sleep(3)
        driver.find_element(By.XPATH, PreCondition_Locators.PASSWORD_FIELD).send_keys(sms_code)
        time.sleep(3)
        driver.find_element(By.CSS_SELECTOR, PreCondition_Locators.CONNECT_BUTTON).click()
        time.sleep(5)
