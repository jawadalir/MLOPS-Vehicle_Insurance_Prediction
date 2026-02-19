from pymongo import MongoClient
from src.constants import MONGODB_URL_KEY

client = MongoClient(MONGODB_URL_KEY)
print(client.list_database_names())