from pymongo import MongoClient

Client= MongoClient('mongodb://localhost:27017')
db=Client['test_db']
collection=db['user']

