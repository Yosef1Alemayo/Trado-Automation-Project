

class ShoppingCartLocators:

#By - XPATH :
    canbis_page = "//div[1]/div[1]/div[1]/div[2]/a[2]"
    canabis_product_list = "//div[1]/div[2]/div[1]/div[2]/div[2]/a"


    sales_product_list = "//div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[3]/a"
    plus_button = "//div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/span[1]"
    minus_button = "//div[2]/div[2]/div[1]/div[1]/span[2]"
    delete_product_from_cart = "//div[1]/a[1]/div[1]/div[3]/div[2]"  # Delete specific product
    empty_the_cart = "//div[2]/div[1]/div[2]/div[1]/div[1]/div[2]"  # Empty the all cart.

    #products description:
    product_name = "//div[1]/div[1]/div[2]/div[1]/h1"
    carton_price = "//div[1]/div[1]/div[2]/div[3]/div[1]/div[3]/div[1]"
    product_price_per_unit = "//div[1]/div[1]/div[1]/span[1]/span[1]"
    unit_in_carton = "//div[1]/div[1]/div[1]/div[2]/div[3]/div[1]/div[2]/div[1]"
    product_barcode = "//div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]"
    minimum_order = "//div[1]/div[1]/div[1]/div[2]/div[3]/span[1]"

    #count each click on plus button:
    count_adding_product = "//div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/input[1]"


    #shopping cart
    count_prod_in_cart = "//div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]"
    prod_name_in_cart = " //div[1]/a[1]/div[1]/div[2]/div[1]"
    prod_price_in_cart = "//div[3]/div[1]/div[1]/div[1]/div[1]/span[1]"
    quantity_per_product = "//div[2]/div[3]/div[1]/div[1]/div[1]/input[1]"    #לא תקין להביא נתיב חדש
    payment_button = "//button[contains(text(),'תשלום')]"

    #mooving to shippment details page:
    shippment_deatails_page_name = "//div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/span[1]"
