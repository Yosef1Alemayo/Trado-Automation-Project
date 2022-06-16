import allure
import pytest
from Web.Pages.maxBussinesPages import MaxBussinesPage
from Web.Utils.PreConditions.pre_condition_yosef import Precondition_Chrome
from Web.Utils.utils import Utils


@pytest.mark.usefixtures('login_correctly')
class TestSigninMaxBussiness(Precondition_Chrome):

    @allure.description('Validating MAX signin page is open')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_signin_correctly(self, login_correctly):

        """The Driver And The PreCondition("Login Correctly") - What is the Requirements for ?"""
        driver = self.driver
        signin = MaxBussinesPage(driver)
        signin.click_link()
        Utils.validation()


    @allure.description('Validating creating new business account with valid details')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_signin_correctly(self, login_correctly):

        """The Driver And The PreCondition("Login Correctly") - What is the Requirements for ?"""
        driver = self.driver
        signin = MaxBussinesPage(driver)
        signin.signin_maxBussines("Betty", "Melaku", "0505864555", "Ashdod", "23", "chocolate", "256", "112365")
        Utils.validation()

    @allure.description('Validating creating new business account with invalid phone number')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_signin_correctly(self, login_correctly):

        """The Driver And The PreCondition("Login Correctly") - What is the Requirements for ?"""
        driver = self.driver
        signin = MaxBussinesPage(driver)
        signin.signin_maxBussines("Betty", "Melaku", "050hdjunm55", "Ashdod", "23", "chocolate", "256", "112365")
        Utils.validation()

    @allure.description('Validating creating new business account with NULL phone number')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_signin_correctly(self, login_correctly):

        """The Driver And The PreCondition("Login Correctly") - What is the Requirements for ?"""
        driver = self.driver
        signin = MaxBussinesPage(driver)
        signin.signin_maxBussines("Betty", "Melaku", "", "Ashdod", "23", "chocolate", "256", "112365")
        Utils.validation()

    @allure.description('Validating creating new business account with invalid first name')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_signin_correctly(self, login_correctly):

        """The Driver And The PreCondition("Login Correctly") - What is the Requirements for ?"""
        driver = self.driver
        signin = MaxBussinesPage(driver)
        signin.signin_maxBussines("123", "Melaku", "0505864555", "Ashdod", "23", "chocolate", "256", "112365")
        Utils.validation()

    @allure.description('Validating creating new business account with invalid last name')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_signin_correctly(self, login_correctly):

        """The Driver And The PreCondition("Login Correctly") - What is the Requirements for ?"""
        driver = self.driver
        signin = MaxBussinesPage(driver)
        signin.signin_maxBussines("Betty", "456", "0505864555", "Ashdod", "23", "chocolate", "256", "112365")
        Utils.validation()

    @allure.description('Validating creating new business account with invalid city or address')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_signin_correctly(self, login_correctly):

        """The Driver And The PreCondition("Login Correctly") - What is the Requirements for ?"""
        driver = self.driver
        signin = MaxBussinesPage(driver)
        signin.signin_maxBussines("Betty", "Melaku", "0505864555", "458", "23", "chocolate", "256", "112365")
        Utils.validation()

    @allure.description('Validating creating new business account with invalid street number')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_signin_correctly(self, login_correctly):

        """The Driver And The PreCondition("Login Correctly") - What is the Requirements for ?"""
        driver = self.driver
        signin = MaxBussinesPage(driver)
        signin.signin_maxBussines("Betty", "Melaku", "0505864555", "Ashdod", "ADC", "chocolate", "256", "112365")
        Utils.validation()

    @allure.description('Validating creating new business account with invalid business name')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_signin_correctly(self, login_correctly):

        """The Driver And The PreCondition("Login Correctly") - What is the Requirements for ?"""
        driver = self.driver
        signin = MaxBussinesPage(driver)
        signin.signin_maxBussines("Betty", "Melaku", "0505864555", "Ashdod", "23", "88974", "256", "112365")
        Utils.validation()

    @allure.description('Validating creating new business account with invalid business ID')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_signin_correctly(self, login_correctly):

        """The Driver And The PreCondition("Login Correctly") - What is the Requirements for ?"""
        driver = self.driver
        signin = MaxBussinesPage(driver)
        signin.signin_maxBussines("Betty", "Melaku", "0505864555", "Ashdod", "23", "chocolate", "ABC", "112365")
        Utils.validation()

    @allure.description('Validating creating new business account with invalid zipCode')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_signin_correctly(self, login_correctly):

        """The Driver And The PreCondition("Login Correctly") - What is the Requirements for ?"""
        driver = self.driver
        signin = MaxBussinesPage(driver)
        signin.signin_maxBussines("Betty", "Melaku", "0505864555", "Ashdod", "23", "chocolate", "256", "ABCDE")
        Utils.validation()

    @allure.description('Validating creating new business account with invalid credentials')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_signin_correctly(self, login_correctly):

        """The Driver And The PreCondition("Login Correctly") - What is the Requirements for ?"""
        driver = self.driver
        signin = MaxBussinesPage(driver)
        signin.signin_maxBussines("123", "u", "05055", "54", "BV", "3365$", "ACDV", "CDCSD")
        Utils.validation()

    @allure.description('Validating creating new business account when all the fields are NULL')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_signin_correctly(self, login_correctly):

        """The Driver And The PreCondition("Login Correctly") - What is the Requirements for ?"""
        driver = self.driver
        signin = MaxBussinesPage(driver)
        signin.signin_maxBussines("", "", "", "", "", "", "", "")
        Utils.validation()