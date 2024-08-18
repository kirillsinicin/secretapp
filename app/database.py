from pymongo import MongoClient

mongo_client = MongoClient("mongodb://localhost:27017/")

db = mongo_client.secret_db

secrets_collection = db.secrets
