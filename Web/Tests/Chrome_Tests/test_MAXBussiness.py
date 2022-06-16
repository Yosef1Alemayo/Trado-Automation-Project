import allure
import pytest
from Web.Pages.maxBussinesPages import MaxBussinesPage
from Web.Utils.PreConditions.precondition_betty import Pre_Condition_Betty


@pytest.mark.usefixtures('login_correctly')
class TestSigninMaxBussiness(Pre_Condition_Betty):

    @allure.description('Validating creating new business account with valid details')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_signin_correctly(self, login_correctly):

        """Validating creating new business account with valid details"""
        driver = self.driver
        signin = MaxBussinesPage(driver)
        signin.signin_maxBussines("Betty", "Melaku", "0505864555", "Ashdod", "23", "chocolate", "256", "112365")

    @allure.description('Validating creating new business account with invalid phone number')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_signin_invalidCredntials(self, login_correctly):

        """Validating creating new business account with invalid phone number"""
        driver = self.driver
        signin = MaxBussinesPage(driver)
        signin.signin_maxBussines("Betty", "Melaku", "050hdjunm55", "Ashdod", "23", "chocolate", "256", "112365")

    @allure.description('Validating creating new business account with NULL phone number')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_signin_invalidCredntials1(self, login_correctly):

        """Validating creating new business account with NULL phone number"""
        driver = self.driver
        signin = MaxBussinesPage(driver)
        signin.signin_maxBussines("Betty", "Melaku", "", "Ashdod", "23", "chocolate", "256", "112365")

    @allure.description('Validating creating new business account with invalid first name')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_signin_invalidCredntials2(self, login_correctly):

        """Validating creating new business account with invalid first name"""
        driver = self.driver
        signin = MaxBussinesPage(driver)
        signin.signin_maxBussines("123", "Melaku", "0505864555", "Ashdod", "23", "chocolate", "256", "112365")

    @allure.description('Validating creating new business account with invalid last name')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_signin_invalidCredntials3(self, login_correctly):

        """Validating creating new business account with invalid last name"""
        driver = self.driver
        signin = MaxBussinesPage(driver)
        signin.signin_maxBussines("Betty", "456", "0505864555", "Ashdod", "23", "chocolate", "256", "112365")

    @allure.description('Validating creating new business account with invalid city or address')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_signin_invalidCredntials3(self, login_correctly):

        """Validating creating new business account with invalid city or address"""
        driver = self.driver
        signin = MaxBussinesPage(driver)
        signin.signin_maxBussines("Betty", "Melaku", "0505864555", "458", "23", "chocolate", "256", "112365")

    @allure.description('Validating creating new business account with invalid street number')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_signin_invalidCredntials4(self, login_correctly):

        """Validating creating new business account with invalid street number"""
        driver = self.driver
        signin = MaxBussinesPage(driver)
        signin.signin_maxBussines("Betty", "Melaku", "0505864555", "Ashdod", "ADC", "chocolate", "256", "112365")

    @allure.description('Validating creating new business account with invalid business name')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_signin_invalidCredntials5(self, login_correctly):

        """Validating creating new business account with invalid business name"""
        driver = self.driver
        signin = MaxBussinesPage(driver)
        signin.signin_maxBussines("Betty", "Melaku", "0505864555", "Ashdod", "23", "88974", "256", "112365")

    @allure.description('Validating creating new business account with invalid business ID')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_signin_invalidCredntials6(self, login_correctly):

        """Validating creating new business account with invalid business ID"""
        driver = self.driver
        signin = MaxBussinesPage(driver)
        signin.signin_maxBussines("Betty", "Melaku", "0505864555", "Ashdod", "23", "chocolate", "ABC", "112365")

    @allure.description('Validating creating new business account with invalid zipCode')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_signin_invalidCredntials7(self, login_correctly):

        """Validating creating new business account with invalid zipCode"""
        driver = self.driver
        signin = MaxBussinesPage(driver)
        signin.signin_maxBussines("Betty", "Melaku", "0505864555", "Ashdod", "23", "chocolate", "256", "ABCDE")

    @allure.description('Validating creating new business account with invalid credentials')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_signin_invalidCredntials8(self, login_correctly):

        """Validating creating new business account with invalid credentials"""
        driver = self.driver
        signin = MaxBussinesPage(driver)
        signin.signin_maxBussines("123", "u", "05055", "54", "BV", "3365$", "ACDV", "CDCSD")

    @allure.description('Validating creating new business account when all the fields are NULL')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_signin_invalidCredntials9(self, login_correctly):

        """Validating creating new business account when all the fields are NULL"""
        driver = self.driver
        signin = MaxBussinesPage(driver)
        signin.signin_maxBussines("", "", "", "", "", "", "", "")
