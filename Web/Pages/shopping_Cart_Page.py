import time

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

        self.count_adding_product= ShoppingCartLocators.count_adding_product

        self.plus_button = ShoppingCartLocators.plus_button
        self.minus_button = ShoppingCartLocators.minus_button
        self.delete_product_from_cart = ShoppingCartLocators.delete_product_from_cart
        self.empty_the_cart = ShoppingCartLocators.empty_the_cart
        self.payment_button = ShoppingCartLocators.payment_button

        self.prod_name_in_cart = ShoppingCartLocators.prod_name_in_cart
        self.num_of_cartons_in_cart = ShoppingCartLocators.num_of_cartons_in_cart
        self.prod_price_in_cart = ShoppingCartLocators.prod_price_in_cart
        self.quntity_per_product_in_cart = ShoppingCartLocators.quntity_per_product_in_cart

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

    ''' ### Get product details form web for assertion: ###  '''

    def get_product_name(self):
        prodName = self.driver.find_element(By.XPATH,self.product_name).get_attribute("innerText")
        return prodName

    def get_product_price_per_unit(self):
        prodPrice= self.driver.find_element(By.XPATH,self.product_price_per_unit).get_attribute("innerText").split("₪")
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


    '''### Get prod details in cart for assertion### '''

    def get_prod_name_in_cart(self):
        prodNameInCart = self.driver.find_element(By.XPATH, self.prod_name_in_cart).get_attribute("innerText")
        return prodNameInCart
        # print(prodNameInCart)

    def get_num_of_cartons_in_cart(self):
        cartonNum = self.driver.find_element(By.XPATH, self.num_of_cartons_in_cart).get_attribute("outerText").split(" ")
        return cartonNum[0]

    def get_prod_price_in_cart(self):
        prodPriceInCart = self.driver.find_element(By.XPATH, self.prod_price_in_cart).get_attribute("innerText").split("₪")
        return prodPriceInCart[1]
        # print(prodPriceInCart[1])

    def get_quntity_per_product_in_cart(self):
        quntity = self.driver.find_element(By.XPATH, self.quntity_per_product_in_cart).get_attribute("valueAsNumber")
        return int(quntity)

    ''' ### Actions in cart :### '''

    #Adding prod(1 per click)
    def click_on_plus_button(self,num):
        for i in range(num):
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH,self.plus_button)))
            self.driver.find_element(By.XPATH,self.plus_button).click()
            time.sleep(2)
        return num

    #Reduce from quantity(1 per click)
    def click_on_minus_button(self,num):
        for i in range(num):
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH,self.minus_button)))
            self.driver.find_element(By.XPATH,self.minus_button).click()
            time.sleep(2)
        return num

    #Delete sepcific prod from cart
    def click_on_delete_prod_from_cart(self):
        self.driver.find_element(By.XPATH,self.delete_product_from_cart).click()

    #Empty all the cart
    def click_on_empty_the_cart(self):
        self.driver.find_element(By.XPATH,self.empty_the_cart).click()

    def click_on_payment_button(self):
        self.driver.find_element(By.XPATH, self.payment_button).click()



    ''' ### Calculations : ### '''
    #price per unit X unit in carton = carton_price
    def calculating_carton_price(self):
        pricePerUnit = self.get_product_price_per_unit()
        unitInCarton = self.get_unit_in_carton()
        cartonPrice = float(pricePerUnit)*float(unitInCarton)
        return ("%.2f" % cartonPrice)
        #".2f"% - מחזיר 2 מספרים אחרי הנקודות במספר עשרוני
        # print("%.2f" % cartonPrice)

    #price in cart(per product) = carton price X num of cartons in cart :
    def calculating_price_in_cart_to_each_prod(self):
        cartonPrice = self.calculating_carton_price()
        numOfCartonIncart = self.get_num_of_cartons_in_cart()
        price = float(cartonPrice)*float(numOfCartonIncart)
        return "%.2f" %price
        #".2f"% - מחזיר 2 מספרים אחרי הנקודות במספר עשרוני
        # print("%.2f" % price)

    #This function calculates how much quantity should remain after reduction from the product:
    #and we used this for assertion:
    #num = how meny we want to reduce
    def calculating_quantity_after_reduce_quantity(self,num):
        a = self.get_num_of_cartons_in_cart()
        b = self.click_on_minus_button(num)
        cal = int(a) - int(b)
        return cal

    ''' ###  Assertion product details in DB : ###'''
    #פונקציות להשוואת נתונים של מוצר מול הDB
    #1
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
        cartonpriceInWeb = self.get_product_price_per_carton()
        #get price from DB
        dbQuery= query_for_products_details("אקדיה", 'price')
        #get price from web
        unitPrice = self.get_product_price_per_unit()
        #get_unit in carton from web
        unitIncarton = self.get_unit_in_carton()
        #calaulation price per carton :
        calculation_based_on_DB  = self.calculating_carton_price(dbQuery,unitIncarton)
        calculation_based_on_web = self.calculating_carton_price(unitPrice,unitIncarton)
        #assertion:
        utils.validation(calculation_based_on_DB,calculation_based_on_web)      ###unstable
        print(calculation_based_on_DB)
        print(calculation_based_on_web)

        # 4
        # Verify price per carton:
        # חישוב : מחיר לקרטון = מחיר ליחידה X מס' יחידות שיש בקרטון
        # cartonpriceInWeb = cart.get_product_price_per_carton()
        # unitPrice = cart.get_product_price_per_unit()
        # unitIncarton = cart.get_unit_in_carton()
        # expected_carton_price = cart.calculating_carton_price(unitPrice,unitIncarton)
        # utils.validation(expected_carton_price,cartonpriceInWeb)    #unstable

        # print("carton price from web: ",cartonpriceInWeb)
        # print("unit price",unitPrice)
        # print("unit in carton:",unitIncarton)
        # print("calculation:",expected_carton_price)

    # 5
    #Verify barcode :
    def verify_barcode(self):
        utils = Utils(self.driver)
        barcode = self.get_product_barcode()
        dbQuery = query_for_products_details("אקדיה","barcode")
        utils.validation(dbQuery,barcode)          #### PASSED
        print(dbQuery)
        print(barcode)

    # 6
    # Verify minimum order:
    def verify_minium_order(self):
        utils = Utils(self.driver)
        minOrder = self.get_minimum_order()
        dbQuery = query_for_products_with_2_keys("אקדיה","units","minimumOrderCartonsCount")
        utils.validation(dbQuery,minOrder)                ####PASSED
        print(dbQuery)
        print(minOrder)


    # def pra(self):
    #     a = self.driver.find_element(By.CSS_SELECTOR, 'div[class="productBtn_amount"]')
    #     b = a.find_element(By.TAG_NAME, 'input')
    #     return b.get_attribute('valueAsNumber')

    # def get_quntity_of_product(self):
    #     counter = self.driver.find_element(By.XPATH,"//div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/input[1]").get_attribute("valueAsNumber")
    #     return counter
