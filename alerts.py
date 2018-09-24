import pymongo

from pymongo import MongoClient
# pprint library is used to make the output look more pretty
# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
client = MongoClient("mongodb+srv://kay:7^303corA7Md@cluster0.mongodb.net/test")
db=client.test
# Issue the serverStatus command and print the results
console.log(db)