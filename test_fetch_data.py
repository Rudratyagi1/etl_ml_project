import pymongo
from dotenv import load_dotenv
import os

load_dotenv()
MONGO_DB_URL = os.getenv("MONGO_DB_URL")
client = pymongo.MongoClient(MONGO_DB_URL)
db = client["RUDRA1"]
collection = db["Network_data"]
print(collection.count_documents({}))  # Should print 11055
