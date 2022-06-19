import pytest
from Web.Utils.PreConditions.pre_condition import Precondition_Chrome
from Web.Pages.personalAreaPage import PageArea
from Web.Utils.PreConditions.precondition_Jonathan import Pre_Condition_Jonathan
from Web.Utils.utils import Utils


@pytest.mark.usefixtures('login_correctly')
class Test1(Pre_Condition_Jonathan):
    #Test when all fields are valid
    def test_1(self, login_correctly):
            driver = self.driver
            pa = PageArea(driver)
            utils = Utils(driver)
            pa.Click_Personal_Area()
            pa.click_Edit_button()
            pa.enter_first_name("Jonathan")
            pa.enter_last_name("Elias")
            # pa.enter_phone()
            pa.enter_email("gonathan46@gmail.com")
            pa.enter_id("205593718")
            # pa.number()
            pa.enter_city('Holon')
            pa.click_Save_button()
            utils.validation()


# Test when all fields are empty
    # def test_2(self, login_correctly):
    #         driver = self.driver
    #         pa = PageArea(driver)
    #         pa.Click_Personal_Area()
    #         pa.click_Edit_button()
    #         pa.enter_first_name("")
    #         pa.enter_last_name("")
    #         # pa.enter_phone("")
    #         pa.enter_email("")
    #         pa.enter_id("")
    #         # pa.number()
    #         pa.enter_city('')
    #         pa.click_Save_button()
    #         Utils.validation()


#Test when no first name is entered in the field

    # def test_3(self, login_correctly):
    #         driver = self.driver
    #         pa = PageArea(driver)
    #         pa.Click_Personal_Area()
    #         pa.click_Edit_button()
    #         pa.enter_first_name("")
    #         pa.enter_last_name("Elias")
    #         # pa.enter_phone()
    #         pa.enter_email("gonathan46@gmail.com")
    #         pa.enter_id("205593718")
    #         # pa.number()
    #         pa.enter_city('Holon')
    #         pa.click_Save_button()
    #         # Utils.validation()

# Test when no last name is entered in the field
#  def test_4(self, login_correctly):
#             driver = self.driver
#             pa = PageArea(driver)
#             pa.Click_Personal_Area()
#             pa.click_Edit_button()
#             pa.enter_first_name("Jonathan")
#             pa.enter_last_name("")
#             # pa.enter_phone()
#             pa.enter_email("gonathan46@gmail.com")
#             pa.enter_id("205593718")
#             # pa.number()
#             pa.enter_city('Holon')
#             pa.click_Save_button()
#             # Utils.validation()

#Test when not putting a phone in the field

 # def test_5(self, login_correctly):
 #            driver = self.driver
 #            pa = PageArea(driver)
 #            pa.Click_Personal_Area()
 #            pa.click_Edit_button()
 #            pa.enter_first_name("Jonathan")
 #            pa.enter_last_name("Elias")
 #            # pa.enter_phone()
 #            pa.enter_email("gonathan46@gmail.com")
 #            pa.enter_id("205593718")
 #            # pa.number()
 #            pa.enter_city('Holon')
 #            pa.click_Save_button()
 #            # Utils.validation()


#Test when no id is entered in the field
 # def test_6(self, login_correctly):
 #            driver = self.driver
 #            pa = PageArea(driver)
 #            pa.Click_Personal_Area()
 #            pa.click_Edit_button()
 #            pa.enter_first_name("Jonathan")
 #            pa.enter_last_name("Elias")
 #            # pa.enter_phone()
 #            pa.enter_email("gonathan46@gmail.com")
 #            pa.enter_id("")
 #            # pa.number()
 #            pa.enter_city('Holon')
 #            pa.click_Save_button()
 #            # Utils.validation()

# Test when not entering a street number in the field
#     def test_7(self, login_correctly):
#             driver = self.driver
#             pa = PageArea(driver)
#             pa.Click_Personal_Area()
#             pa.click_Edit_button()
#             pa.enter_first_name("Jonathan")
#             pa.enter_last_name("Elias")
#             # pa.enter_phone()
#             pa.enter_email("gonathan46@gmail.com")
#             pa.enter_id("205593718")
#             # pa.number()
#             pa.enter_city('Holon')
#             pa.click_Save_button()
#             # Utils.validation()

# Test when not entering a city in the field
#    def test_8(self, login_correctly):
#             driver = self.driver
#             pa = PageArea(driver)
#             pa.Click_Personal_Area()
#             pa.click_Edit_button()
#             pa.enter_first_name("Jonathan")
#             pa.enter_last_name("Elias")
#             # pa.enter_phone()
#             pa.enter_email("gonathan46@gmail.com")
#             pa.enter_id("205593718")
#             # pa.number()
#             pa.enter_city()
#             pa.click_Save_button()
#             # Utils.validation()


# Test when email is not entered in the field
#    def test_9(self, login_correctly):
#             driver = self.driver
#             pa = PageArea(driver)
#             pa.Click_Personal_Area()
#             pa.click_Edit_button()
#             pa.enter_first_name("Jonathan")
#             pa.enter_last_name("Elias")
#             # pa.enter_phone()
#             pa.enter_email("")
#             pa.enter_id("205593718")
#             # pa.number()
#             pa.enter_city("holon")
#             pa.click_Save_button()
#             # Utils.validation()

