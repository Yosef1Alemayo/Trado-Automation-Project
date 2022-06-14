import pytest
from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager

class Base_Edge:
    @pytest.fixture(autouse=True)
    def set_up_edge(self):
        print('\n----------------------')
        print('Initialing Edge Driver')
        print('-------------------------')
        self.driver = webdriver.Edge(EdgeChromiumDriverManager().install())
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