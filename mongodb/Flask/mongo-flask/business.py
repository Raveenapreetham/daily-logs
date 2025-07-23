from pymongo import MongoClient
from dotenv import load_dotenv
import os


load_dotenv()
mongo_url=os.getenv("mongodb+srv://Raveena_Preetham:<db_password>@cluster0.09xb7m2.mongodb.net/","mongodb://localhost:27017")
db_name=os.getenv('db_name')
client = MongoClient(mongo_url)
db = client[db_name]
collection = db['data_db']