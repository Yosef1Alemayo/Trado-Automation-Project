class MaxBussinesLocators:

    maxLink = "//body/div[@id='root']/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]" \
              "/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[10]/a[1]"

    firstName_field = "first name"
    lastName_field = "last name"
    phone = "phone"
    city_street = "הכנס עיר/רחוב"
    street_number = "number"
    bussines_name = "buisness name"
    bussines_id = "id"
    postal_code = "zipcode"

    send_button = "form_submitBtn"

    # assertions
    max_business = "//h3[contains(text(),'רוצים לשמוע עוד על אפשרות התשלום של MAX b2b ?')]"
    txt_maxbusiness = "רוצים לשמוע עוד על אפשרות התשלום של MAX B2b ?"
