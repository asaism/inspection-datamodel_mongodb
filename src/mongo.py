from pymongo import MongoClient

def get_mongo():
  mongo_client = MongoClient('api_mongo', 27017)
  mongo_client['admin'].authenticate("root", "password")
  return mongo_client
