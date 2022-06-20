class NavBarLocators:

    header1 = "//header/div[1]/div[1]/a"
    header2 = "//div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/a"

    # Buttons
    click_PersonalArea = "//header/div[1]/div[1]/a[1]"
    click_logout = "//header/div[1]/div[1]/a[2]"
    click_logo = "//header/div[1]/div[1]/a[3]"
    list_buttons = [click_logo, click_PersonalArea, click_logout]

    # asserttion
    Button1 = "//h1[contains(text(),'מבצעים')]"
    Button2 = "//h1[contains(text(),'חטיפים')]"
    Button3 = "//h1[contains(text(),'קנאביס')]"
    Button4 = "//h1[contains(text(),'משקאות')]"
    Button5 = "//h2[contains(text(),'הוספת מוצר חדש')]"
    productIN_arina = "//div[1]/div[2]/div[1]/div[1]/div[1]/h4[1]"
    login = "//div[1]/div[1]/a[1]/span[1]"

    # txt assertion
    Button1_txt = "מבצעים"
    Button2_txt = "חטיפים"
    Button3_txt = "קנאביס"
    Button4_txt = "משקאות"
    Button5_txt = "הוספת מוצר חדש"
    productIN_arina_txt = "0 מוצרים שהעלת לזירה"
    login_txt = "התחברות"

    list_collectionName = [Button2_txt, Button3_txt, Button4_txt]
    clickbutton2 = "//div[1]/div[1]/div[1]/div[1]/div[2]/a[2]"
    clickbutton3 = "//div[1]/div[1]/div[1]/div[1]/div[2]/a[3]"
    clickbutton4 = "//div[1]/div[1]/div[1]/div[1]/div[2]/a[4]"
    list_collectionbuttons = [clickbutton2,clickbutton3,clickbutton4]

    # List assertion
    assertion_listButtons = [Button1, productIN_arina, login]
    assertionTXT_listButtons = [Button1_txt, productIN_arina_txt, login_txt]

    list1 = [Button1, Button2, Button3, Button4, Button5]
    list2 = [productIN_arina,login,Button1]
    list_txt = [Button1_txt, Button2_txt, Button3_txt, Button4_txt, Button5_txt]
    list_txt2 = [productIN_arina_txt,login_txt,Button1_txt]

    # db
    amount_Xpath = "//div[1]/div[2]/div[2]/div[1]/h4[1]/span[1]/span[2]"

    list_sectionName = ["חטיפים","קנאביס","משקאות"]
    list_locator = ["//div[2]/div[1]/div[1]/h4[1]/span[1]/span[2]","//span[contains(text(),'11')]","//div[1]/div[1]/h4[1]/span[1]/span[2]"]