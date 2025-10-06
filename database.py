from pymongo import MongoClient

MONGO_URI = "mongodb://mongo:27017"
DB_NAME = "face_recognition_db"

client = MongoClient(MONGO_URI)
db = client[DB_NAME]

def get_user_collection():
    return db["users"]