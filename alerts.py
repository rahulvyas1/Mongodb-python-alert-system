import pymongo

# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
client = MongoClient("mongodb+srv://kay:7^303corA7Md@cluster0.mongodb.net/test")
db=client.test
# Issue the serverStatus command and print the results
print(db)