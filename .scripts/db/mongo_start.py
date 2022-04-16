from pymongo import MongoClient

client = MongoClient('mongodb://root:root@localhost:27017/')
db = client['portfolio']

db.create_collection('contacts')