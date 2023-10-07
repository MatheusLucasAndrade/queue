from pymongo import MongoClient
from pymongo.collection import Collection


class DatabaseConfig:
    def __init__(self, db_name: str, collection_name: str) -> None:
        self.client = MongoClient("mongodb://localhost:27017/")
        self.database = self.client[db_name]
        self.collection = self.database[collection_name]
