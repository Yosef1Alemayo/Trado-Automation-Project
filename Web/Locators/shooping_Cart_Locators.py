

class ShoppingCartLocators:

#By - XPATH :
    canbis_page = "//div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/a[3]"
    canabis_product_list = "//div[1]/div[2]/div[1]/div[2]/div[2]/a"


    sales_product_list = "//div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[3]/a"
    plus_button = "//div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/span[1]"
    minus_button = "//div[2]/div[2]/div[1]/div[1]/span[2]"
    delete_product_from_cart = "//div[1]/a[1]/div[1]/div[3]/div[2]"  # Delete specific product
    empty_the_cart = "//div[2]/div[1]/div[2]/div[1]/div[1]/div[2]"  # Empty the all cart.
    message_when_cart_is_empty = "//div[2]/div[1]/div[2]/div[1]/h5[1]"

    #products description:
    product_name = "//div[1]/div[1]/div[2]/div[1]/h1"
    carton_price = "//div[1]/div[1]/div[2]/div[3]/div[1]/div[3]/div[1]"
    product_price_per_unit = "//div[1]/div[1]/div[1]/span[1]/span[1]"
    unit_in_carton = "//div[1]/div[1]/div[1]/div[2]/div[3]/div[1]/div[2]/div[1]"
    product_barcode = "//div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]"
    minimum_order = "//div[1]/div[1]/div[1]/div[2]/div[3]/span[1]"

    #shopping cart
    count_prod_in_cart = "//div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]"
    prod_name_in_cart = " //div[1]/a[1]/div[1]/div[2]/div[1]"
    num_of_cartons_in_cart = "//div[2]/div[1]/a[1]/div[1]/div[2]/div[2]/div[2]"
    prod_price_in_cart = "//div[3]/div[1]/div[1]/div[1]/div[1]/span[1]"
    quntity_per_product_in_cart = "//div[2]/div[1]/a[1]/div[1]/div[2]/div[3]/div[1]/div[1]/div[1]/input[1]"
    payment_button = "//button[contains(text(),'תשלום')]"
    payment_page_title = "//div[1]/div[2]/div[1]/div[2]/form[1]/section[1]/h1[1]"

