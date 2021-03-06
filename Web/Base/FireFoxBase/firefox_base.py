import pytest
from selenium import webdriver

class Base_FireFox:
    @pytest.fixture(autouse=True)
    def set_up_firefox(self):
        print('\n----------------------')
        print('Initialing FireFox Driver')
        print('-------------------------')
        self.driver = webdriver.Firefox()
        print('\n----------------------')
        print('Test is Started')
        print('------------------------')
        self.driver.implicitly_wait(15)
        self.driver.get('https://qa.trado.co.il/')
        self.driver.maximize_window()

        yield self.driver
        if self.driver is not None:
            print("\n----------------------------")
            print("Tests is finished")
            print('------------------------------')
            self.driver.close()
            self.driver.quit()
