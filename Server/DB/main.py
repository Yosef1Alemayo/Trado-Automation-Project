from Server.DB.mongodb import DataBase
''' Pre Condition for All The Tests'''

string_connection = 'mongodb+srv://test_dev:AtmNf7Iz5BIs0dzc@cluster0.qnr3p.mongodb.net/?retryWrites=true&w=majority'
user = DataBase(string_connection)

def query_for_login_code():
    collection = user.db_and_collection('users')
    query = collection.find_one({'phone': '0526050731'})
    sms_code = query['loginCode']
    return sms_code

def query_for_products_details():
    collection = user.db_and_collection('products')
    query = collection.find_one({'name': 'קורונה'})
    barcode = query['barcode']
    return barcode

