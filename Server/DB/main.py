from Server.DB.mongodb import DataBase
''' Pre Condition for All The Tests'''

def query_for_login_code(phone_number):
    string_connection = 'mongodb+srv://test_dev:AtmNf7Iz5BIs0dzc@cluster0.qnr3p.mongodb.net/?retryWrites=true&w=majority'
    user = DataBase(string_connection)
    collection = user.db_and_collection('users')
    query = collection.find_one({'phone': f'{phone_number}'})
    sms_code = query['loginCode']
    return sms_code

def query_for_products_details(product_name, key):
    string_connection = 'mongodb+srv://test_dev:AtmNf7Iz5BIs0dzc@cluster0.qnr3p.mongodb.net/?retryWrites=true&w=majority'
    user = DataBase(string_connection)
    collection = user.db_and_collection('products')
    query = collection.find_one({'name': f'{product_name}'})
    value = query[f'{key}']
    return value

def query_for_products_with_2_keys(prod_name, key, key2):
    string_connection = 'mongodb+srv://test_dev:AtmNf7Iz5BIs0dzc@cluster0.qnr3p.mongodb.net/?retryWrites=true&w=majority'
    user = DataBase(string_connection)
    collection = user.db_and_collection('products')
    query = collection.find_one({'name': prod_name})
    value = query[key]
    return value[key2]

def query_for_collection_len(section_name):
    string_connection = 'mongodb+srv://test_dev:AtmNf7Iz5BIs0dzc@cluster0.qnr3p.mongodb.net/?retryWrites=true&w=majority'
    user = DataBase(string_connection)
    collection = user.db_and_collection('products')
    query = collection.count_documents({"$and": [{"sectionName": f"{section_name}"}, {"active": True}]})
    return str(query)


