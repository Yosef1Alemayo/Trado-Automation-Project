import time
import pytest
from Server.DB.main import query_for_login_code
from Web.Base.EdgeBase.edge_base import Base_Edge
from selenium.webdriver.common.by import By
from Web.Base.ChromeBase.chrome_base import Base_Chrome
from Web.Utils.PreConditions.pre_conditions_locators import PreCondition_Locators

@pytest.mark.usefixtures('set_up_chrome')
class Precondition_Chrome(Base_Chrome):
    @pytest.fixture(autouse=True)
    def login_correctly(self, set_up_chrome):
        driver = self.driver
        driver.find_element(By.XPATH, PreCondition_Locators.RESTAURANTS).click()
        driver.find_element(By.XPATH, PreCondition_Locators.COCKTAILS).click()
        driver.find_element(By.CSS_SELECTOR, PreCondition_Locators.SAVE_BUTTON).click()
        driver.find_element(By.XPATH, PreCondition_Locators.LOGIN_SECTION).click()
        driver.find_element(By.XPATH, PreCondition_Locators.PHONE_FIELD).send_keys('0526050731')
        connect = driver.find_element(By.CSS_SELECTOR, PreCondition_Locators.CONNECT_BUTTON)
        connect.click()
        sms_code = query_for_login_code()
        time.sleep(3)
        driver.find_element(By.XPATH, PreCondition_Locators.PASSWORD_FIELD).send_keys(sms_code)
        time.sleep(3)
        driver.find_element(By.CSS_SELECTOR, PreCondition_Locators.CONNECT_BUTTON).click()

@pytest.mark.usefixtures('set_up_edge')
class Precondition_Edge(Base_Edge):
    @pytest.fixture(autouse=True)
    def login_correctly(self, set_up_edge):
        driver = self.driver
        driver.find_element(By.CSS_SELECTOR, PreCondition_Locators.SAVE_BUTTON).click()
        driver.find_element(By.XPATH, PreCondition_Locators.LOGIN_SECTION).click()
        driver.find_element(By.XPATH, PreCondition_Locators.PHONE_FIELD).send_keys('0526050731')
        connect = driver.find_element(By.CSS_SELECTOR, PreCondition_Locators.CONNECT_BUTTON)
        connect.click()
        sms_code = query_for_login_code()
        time.sleep(3)
        driver.find_element(By.XPATH, PreCondition_Locators.PASSWORD_FIELD).send_keys(sms_code)
        time.sleep(3)
        driver.find_element(By.CSS_SELECTOR, PreCondition_Locators.CONNECT_BUTTON).click()
