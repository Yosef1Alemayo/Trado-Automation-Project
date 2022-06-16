from Web.Base.ChromeBase.chrome_base import Base_Chrome
from Web.Locators.shooping_Cart_Locators import ShoppingCartLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Server.DB.main import query_for_products_details
from Server.DB.main import query_for_products_with_2_keys
from Web.Utils.utils import Utils


class ShoppingCartPage():

    def __init__(self,driver):
        self.driver = driver
        self.canabis_page = ShoppingCartLocators.canbis_page
        self.canabis_product_list = ShoppingCartLocators.canabis_product_list

        self.product_name = ShoppingCartLocators.product_name
        self.product_price_per_unit = ShoppingCartLocators.product_price_per_unit
        self.carton_price = ShoppingCartLocators.carton_price
        self.unit_in_carton = ShoppingCartLocators.unit_in_carton
        self.product_barcode = ShoppingCartLocators.product_barcode
        self.minimum_order = ShoppingCartLocators.minimum_order

        self.plus_button = ShoppingCartLocators.plus_button
        self.minus_button = ShoppingCartLocators.minus_button
        self.delete_product_from_cart = ShoppingCartLocators.delete_product_from_cart
        self.empty_the_cart = ShoppingCartLocators.empty_the_cart
        self.payment_button = ShoppingCartLocators.payment_button

        self.prod_name_in_cart = ShoppingCartLocators.prod_name_in_cart
        self.prod_price_in_cart = ShoppingCartLocators.prod_price_in_cart
        self.quantity_per_product = ShoppingCartLocators.quantity_per_product

### precondition ###
    def click_on_canabis_page(self):
        WebDriverWait(self.driver,20).until(EC.element_to_be_clickable((By.XPATH,self.canabis_page)))
        self.driver.find_element(By.XPATH,self.canabis_page).click()

    def get_canabis_product_list(self):
        prodList= self.driver.find_elements(By.XPATH,self.canabis_product_list)
        return prodList
        # print(len(prodList))

    def click_on_product_from_list(self, num):     #בהמשך צריך להחליף את NUM ל-מספר אקראי (RANDOM.RANDIT )
        prodList = self.get_canabis_product_list()
        prodList[num].click()


    '''Preconditin to all tests : Enter to canabis page and click on product'''
    def precondition_all_tests(self):
        self.click_on_canabis_page()
        self.click_on_product_from_list(4)


### Get product details: for assertion ###
    def get_product_name(self):
        prodName = self.driver.find_element(By.XPATH,self.product_name).get_attribute("innerText")
        return prodName

    def get_product_price_per_unit(self):
        prodPrice= self.driver.find_element(By.XPATH,self.product_price_per_unit).get_attribute("innerText").split(".")
        return float(prodPrice[0])

    def get_unit_in_carton(self):
        unitInCarton = self.driver.find_element(By.XPATH, self.unit_in_carton).get_attribute("innerText").split("י")
        return unitInCarton[0]

    def get_product_price_per_carton(self):
        cartonPrice = self.driver.find_element(By.XPATH,self.carton_price).get_attribute("innerText").split("/")
        return float(cartonPrice[0])

    def get_product_barcode(self):
        barcode = self.driver.find_element(By.XPATH,self.product_barcode).get_attribute("innerText").split(": ")
        return barcode[1]

    def get_minimum_order(self):
        minOrder = self.driver.find_element(By.XPATH,self.minimum_order).get_attribute("innerText").split(" ")
        return minOrder[2]

###Actions :

    #Adding prod(1 per click)
    def click_on_plus_button(self):
        self.driver.find_element(By.XPATH,self.plus_button).click()
        self.driver.implicitly_wait(5)

    #Reduce from quantity(1 per click)
    def click_on_minus_button(self):
        self.driver.find_element(By.XPATH,self.minus_button).click()

    #Delete sepcific prod from cart
    def click_on_delete_prod_from_cart(self):
        self.driver.find_element(By.XPATH,self.delete_product_from_cart).click()

    #Empty all the cart
    def click_on_empty_the_cart(self):
        self.driver.find_element(By.XPATH,self.empty_the_cart).click()

    def click_on_payment_button(self):
        self.driver.find_element(By.XPATH, self.payment_button).click()

### Get prod details in cart :
    def get_prod_name_in_cart(self):
        prodNameInCart = self.driver.find_element(By.XPATH,self.prod_name_in_cart).get_attribute("innerText")
        return prodNameInCart
        # print(prodNameInCart)

    def get_prod_price_in_cart(self):
        prodPriceInCart = self.driver.find_element(By.XPATH,self.prod_price_in_cart).get_attribute("innerText")
        return prodPriceInCart
        # print(prodPriceInCart)

    def get_quantity_per_product_in_cart(self):
        quantity = self.driver.find_element(By.XPATH,self.quantity_per_product).get_attribute("innerText")
        return quantity
        # print(quantity)



#Calculations :
    #= price per unit X unit in carton = carton_price
    def calculating_carton_price(self,num1,num2):
        cal = float(num1)*float(num2)
        return cal



#פונקציות להשוואת נתונים של מוצר מול הDB
#ואז לעשות פונקציה אחת גדולה
    #!1
    #Verify name:
    def verify_product_name(self):
        utils = Utils(self.driver)
        name = self.get_product_name()
        dbQuery = query_for_products_details("אקדיה", 'name')
        utils.validation(dbQuery, name)  ####PASSED
        print(name)
        print(dbQuery)

    #2
    #Verify price per unit:
    def verify_price_per_unit(self):
        utils = Utils(self.driver)
        price = self.get_product_price_per_unit()
        dbQuery = query_for_products_details("אקדיה" ,'price')
        utils.validation(dbQuery, price)       #Assertion Error טסט תקין - אבל נופל בגלל
        print(price)
        print(dbQuery)

    #3
    #Verify units in carton:
    def verify_unit_in_carton(self):
        utils = Utils(self.driver)
        units = self.get_unit_in_carton()
        dbQuery = query_for_products_with_2_keys("אקדיה",'units','unitsInCarton')
        utils.validation(dbQuery, units)              ####PASSED
        print(units)
        print(dbQuery)

    #4
    # Verify price per carton:
    # פונקציה שמחשבת מחיר לקרטון : מחיר לקרטון = מחיר ליחידה X מס' יחידות שיש בקרטון
    def verify_price_per_carton(self):
        utils = Utils(self.driver)
        # cart = ShoppingCartPage(driver)
        cartonpriceInWeb = self.get_product_price_per_carton()
        dbQuery= query_for_products_details("אקדיה", 'price')

        unitPrice = self.get_product_price_per_unit()   #האם לחשב לפי מחיר בדאטה בייס או לפי המחיר באתר ????

        unitIncarton = self.get_unit_in_carton()

        calculation_from_web = self.calculating_carton_price(unitPrice,unitIncarton)
        calculation_from_DB = self.calculating_carton_price(dbQuery,unitIncarton)


        utils.validation(calculation_from_DB,calculation_from_web)    #unstable
        print(calculation_from_web)
        print(calculation_from_DB)

        #לעשות 2 טסטים ולהשוות בניהם:





####פונקציה אחת גדולה לכל האימות נתונים##
    def verify_products_details(self):
        driver = self.driver
        utils = Utils(driver)
        cart = ShoppingCartPage(driver)
        #name:
        name = cart.get_product_name()
        dbQuery = query_for_products_details("אקדיה", 'name')
        utils.validation(dbQuery, name)  ####PASSED
        print(name)
        print(dbQuery)
        #price:
        price = cart.get_product_price_per_unit()
        dbQuery = query_for_products_details("אקדיה" ,'price')
        utils.validation(dbQuery, price)       #Assertion Error טסט תקין - אבל נופל בגלל
        print(price)
        print(dbQuery)
        #units:
        units = cart.get_unit_in_carton()
        dbQuery = query_for_products_with_2_keys("אקדיה", 'units', 'unitsInCarton')
        utils.validation(dbQuery, units)  ####PASSED
        print(units)
        print(dbQuery)



    def number(self):
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(By.XPATH, ShoppingCartPage.elem))
        number = self.driver.find_element(By.XPATH, ShoppingCartPage.elem).get_attribute('value')
        print(number)
