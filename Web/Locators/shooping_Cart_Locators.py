

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
    product_price= "//div[2]/div[1]/div[1]/div[1]/div[1]/span[1]"


    units_in_stuck = "//div[1]/div[1]/div[1]/div[2]/div[3]/div[1]/div[1]/div[1]"

    #shopping cart
    prod_name_in_cart = " //div[1]/a[1]/div[1]/div[2]/div[1]"
    prod_price_in_cart = "//div[3]/div[1]/div[1]/div[1]/div[1]/span[1]"
    quantity_per_product = "//div[2]/div[3]/div[1]/div[1]/div[1]/input[1]"    # Per Product

    payment_button = "//button[contains(text(),'תשלום')]"

    #mooving to shippment details page:
    shippment_deatails_page_name = "//div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/span[1]"
