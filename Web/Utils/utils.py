import allure
from allure_commons.types import AttachmentType

class Utils:

    def __init__(self, driver):
        self.driver = driver

    def validation(self, expected, actual):
        driver = self.driver
        try:
            assert expected == actual
        except AssertionError:
            allure.attach(driver.get_screenshot_as_png(), name='screenShot',
                          attachment_type=AttachmentType.PNG)
            raise AssertionError

