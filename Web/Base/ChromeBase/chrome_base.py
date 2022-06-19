import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class Base_Chrome:
    @pytest.fixture(autouse=True)
    def set_up_chrome(self):
        print('\n----------------------')
        print('Initialing Chrome Driver')
        print('-------------------------')
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        print('\n----------------------')
        print('Test is Started')
        print('------------------------')
        self.driver.implicitly_wait(20)
        self.driver.get('https://qa.trado.co.il/')
        self.driver.maximize_window()

        yield self.driver
        if self.driver is not None:
            print("\n----------------------------")
            print("Tests is finished")
            print('------------------------------')
            self.driver.close()
            self.driver.quit()
