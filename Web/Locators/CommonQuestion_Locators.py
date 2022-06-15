class CommonQueLocators:


    # buttons
    commonQue_Button = "//a[contains(text(),'לכל השאלות')]"

    productsPage_Button = "//button[contains(text(),'עמוד מוצרים')]"
    uploadProduct_Button = "//button[contains(text(),'העלאת מוצר')]"

    # assertion on commonQue link
    commonQue_innertext = "//body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/h4[1]"
    uploadProduct_innertext = "//h2[contains(text(),'הוספת מוצר חדש')]"
    productpage_innertext = "//h1[contains(text(),'מבצעים')]"

    # TXT to assert
    commonQue_txt = "יש לכם שאלות?\nהגעתם למקום הנכון"
    product_pageTXT = "מבצעים"
    uploadproduct_txt = "הוספת מוצר חדש"