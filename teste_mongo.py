from pymongo import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://jcrodriguesleite_db_user:dvXyqdkqcObqXofM@cluster0.gmuubrk.mongodb.net/"

client = MongoClient(uri, server_api=ServerApi('1'))

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db = client["sample_mflix"]

collection = db["movies"]

print(collection.find_one())

