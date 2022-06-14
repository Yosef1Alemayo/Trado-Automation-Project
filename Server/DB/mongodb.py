from pymongo import MongoClient

class DataBase:
    def __init__(self, connection_string):
        self.connection_string = connection_string
        self.client = self.connect()

    def connect(self):
        self.client = MongoClient(self.connection_string)
        return self.client

    def db_and_collection(self, collection_name):
        database = self.client['trado_qa']
        collection = database[collection_name]
        return collection


