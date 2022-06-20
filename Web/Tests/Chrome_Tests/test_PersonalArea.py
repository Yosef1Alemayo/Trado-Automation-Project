import time
import pytest
from Web.Pages.personalAreaPage import PageArea
from Web.Utils.PreConditions.precondition import Pre_Condition
from Web.Utils.utils import Utils


@pytest.mark.usefixtures('login_jonathan')
class Test1(Pre_Condition):
    #Test when all fields are valid
    def test_1(self):
            driver = self.driver
            pa = PageArea(driver)
            pa.Click_Personal_Area()
            pa.click_Edit_button()
            pa.enter_first_name("Jonathan")
            pa.enter_last_name("Elias")
            pa.enter_phone("0522578853")
            pa.enter_email("gonathan46@gmail.com")
            pa.enter_id("205598745")
            pa.enter_number('5')
            pa.enter_city('Holon')
            pa.click_Save_button()


# Test when all fields are empty
    def test_2(self):
            driver = self.driver
            pa = PageArea(driver)
            pa.Click_Personal_Area()
            pa.click_Edit_button()
            pa.enter_first_name("")
            pa.enter_last_name("")
            pa.enter_phone("")
            pa.enter_email("")
            pa.enter_id("")
            pa.enter_number('')
            pa.enter_city('')
            pa.click_Save_button()


#Test when no first name is entered in the field

    def test_3(self):
            driver = self.driver
            pa = PageArea(driver)
            pa.Click_Personal_Area()
            pa.click_Edit_button()
            pa.enter_first_name("")
            pa.enter_last_name("Elias")
            pa.enter_phone("0522578853")
            pa.enter_email("gonathan46@gmail.com")
            pa.enter_id("205598745")
            pa.enter_number('5')
            pa.enter_city('Holon')
            pa.click_Save_button()

# Test when no last name is entered in the field
    def test_4(self):
            driver = self.driver
            pa = PageArea(driver)
            pa.Click_Personal_Area()
            pa.click_Edit_button()
            pa.enter_first_name("Jonathan")
            pa.enter_last_name("")
            pa.enter_phone("0522578853")
            pa.enter_email("gonathan46@gmail.com")
            pa.enter_id("205598745")
            pa.enter_number('5')
            pa.enter_city('Holon')
            pa.click_Save_button()

#Test when not putting a phone in the field

    def test_5(self):
            driver = self.driver
            pa = PageArea(driver)
            pa.Click_Personal_Area()
            pa.click_Edit_button()
            pa.enter_first_name("Jonathan")
            pa.enter_last_name("Elias")
            pa.enter_phone("0522578853")
            pa.enter_email("gonathan46@gmail.com")
            pa.enter_id("205598745")
            pa.enter_number('5')
            pa.enter_city('Holon')
            pa.click_Save_button()


#Test when no id is entered in the field
    def test_6(self):
            driver = self.driver
            pa = PageArea(driver)
            pa.Click_Personal_Area()
            pa.click_Edit_button()
            pa.enter_first_name("Jonathan")
            pa.enter_last_name("Elias")
            pa.enter_phone("0522578853")
            pa.enter_email("gonathan46@gmail.com")
            pa.enter_id("")
            pa.enter_number('5')
            pa.enter_city('Holon')
            pa.click_Save_button()

# Test when not entering a street number in the field
    def test_7(self):
            driver = self.driver
            pa = PageArea(driver)
            pa.Click_Personal_Area()
            pa.click_Edit_button()
            pa.enter_first_name("Jonathan")
            pa.enter_last_name("Elias")
            pa.enter_phone("0522578853")
            pa.enter_email("gonathan46@gmail.com")
            pa.enter_id("205598745")
            pa.enter_number('5')
            pa.enter_city('Holon')
            pa.click_Save_button()

# Test when not entering a city in the field
    def test_8(self):
            driver = self.driver
            pa = PageArea(driver)
            pa.Click_Personal_Area()
            pa.click_Edit_button()
            pa.enter_first_name("Jonathan")
            pa.enter_last_name("Elias")
            pa.enter_phone("0522578853")
            pa.enter_email("gonathan46@gmail.com")
            pa.enter_id("205598745")
            pa.enter_number('5')
            pa.enter_city('')
            pa.click_Save_button()


# Test when email is not entered in the field
    def test_9(self):
            driver = self.driver
            pa = PageArea(driver)
            pa.Click_Personal_Area()
            pa.click_Edit_button()
            pa.enter_first_name("Jonathan")
            pa.enter_last_name("Elias")
            pa.enter_phone("0522578853")
            pa.enter_email("")
            pa.enter_id("205598745")
            pa.enter_number('5')
            pa.enter_city("holon")
            pa.click_Save_button()

