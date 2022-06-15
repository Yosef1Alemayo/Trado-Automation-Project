from Server.DB.mongodb import DataBase
''' Pre Condition for All The Tests'''

string_connection = 'mongodb+srv://test_dev:AtmNf7Iz5BIs0dzc@cluster0.qnr3p.mongodb.net/?retryWrites=true&w=majority'
user = DataBase(string_connection)

def query_for_login_code():
    collection = user.db_and_collection('users')
    query = collection.find_one({'phone': '0525393079'})
    sms_code = query['loginCode']
    return sms_code

def query_for_products_details(product_name, key):
    collection = user.db_and_collection('products')
    query = collection.find_one({'name': f'{product_name}'})
    value = query[f'{key}']
    return value

def query_for_products_with_2_keys(prod_name, key, key2):
    collection = user.db_and_collection('products')
    query = collection.find_one({'name': prod_name})
    value = query[key]
    return value[key2]


