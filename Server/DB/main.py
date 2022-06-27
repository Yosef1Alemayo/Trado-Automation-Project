from Server.DB.mongodb import DataBase
''' Pre Condition for All The Tests'''

class Main:
    string_connection = 'mongodb+srv://test_dev:AtmNf7Iz5BIs0dzc@cluster0' \
                        '.qnr3p.mongodb.net/?retryWrites=true&w=majority'

def query_for_login_code(phone_number):
    string_connection = Main.string_connection
    user = DataBase(string_connection)
    collection = user.db_and_collection('users')
    query = collection.find_one({'phone': f'{phone_number}'})
    sms_code = query['loginCode']
    return sms_code

def query_for_products_details(col, product_name, key):
    string_connection = Main.string_connection
    user = DataBase(string_connection)
    collection = user.db_and_collection(f'{col}')
    query = collection.find_one({'name': f'{product_name}'})
    value = query[f'{key}']
    return str(value)

def query_for_products_with_2_keys(col, prod_name, key, key2):
    string_connection = Main.string_connection
    user = DataBase(string_connection)
    collection = user.db_and_collection(f'{col}')
    query = collection.find_one({'name': prod_name})
    value = query[key]
    return value[key2]

def query_for_collection_len(col, key1, value1, key2, value2):
    string_connection = Main.string_connection
    user = DataBase(string_connection)
    collection = user.db_and_collection(f'{col}')
    query = collection.count_documents({"$and": [{f"{key1}": f"{value1}"}, {f"{key2}": {value2}}]})
    return str(query)


