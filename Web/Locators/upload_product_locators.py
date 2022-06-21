class Upload_New_Product_Locators:
    # CSS:
    ADD_PRODUCT_PAGE = 'div[class="addProduct_page"]'
    NEW_PRODUCT_FIELDS = 'input[class="add_product_page_form_item"]'
    ADD_NEW_PRODUCT_BUTTON = 'input[class="form_submitBtn"]'
    ADD_NEW_PRODUCT_SECTION = 'a[class="verticalMenu_addProduct"]'
    IMAGE = "//input[@id='files']"
    # Xpath:
    CHECKBOX = '//div[1]/div[2]/div[3]/div[1]/input[1]'
    UNIT_AND_WEIGHT = '//div[1]/div[2]/div[3]/div[1]/span'
    PLUS_BUTTON = '//div[3]/div[1]/div[1]/div[1]/span[1]'
    MINUS_BUTTON = '//div[3]/div[1]/div[1]/div[1]/span[2]'
    AMOUNT_OF_DAYS = '//div[1]/input[1]'

    # Messages
    STORE_VALIDATION_FAILED = 'div[class="form_message"]'
    FILL_THE_FIELD = "//form[1]/div[2]/div/div/div/div"
    ERROR_FIELD_IS_EMPTY = 'div[class="form_note "]'


