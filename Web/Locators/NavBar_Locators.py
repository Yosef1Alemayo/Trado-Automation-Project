class NavBarLocators:

    header1 = "//header/div[1]/div[1]/a"
    className1 = 'header_header_container'

    header2 = "//div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/a"
    className2 = "verticalMenu_verticalMenuList"

    # asserttion
    a1 = "//h1[contains(text(),'מבצעים')]"
    a2 = "//h1[contains(text(),'חטיפים')]"
    a3 = "//h1[contains(text(),'קנאביס')]"
    a4 = "//h1[contains(text(),'משקאות')]"
    a5 = "//h2[contains(text(),'הוספת מוצר חדש')]"

    personal_area = "//div[2]/div[1]/div[2]/div[1]/div[1]/div[1]"
    login = "//header/div[1]/div[1]/a[1]"

    # txt assertion
    a1_txt = "מבצעים"
    a2_txt = "חטיפים"
    a3_txt = "קנאביס"
    a4_txt = "משקאות"
    a5_txt = "הוספת מוצר חדש"

    personal_areatxt = "0 מוצרים שהעלת לזירה"
    login_txt = "שלום אורח,\nהתחברות"

    list1 = [a1, a2, a3, a4, a5]
    list_txt = [a1_txt, a2_txt, a3_txt, a4_txt, a5_txt]

    list2 = [personal_area, login, a1]
    list_txt2 = [personal_areatxt, login_txt, a1_txt]


