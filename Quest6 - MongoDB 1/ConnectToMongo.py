import pymongo
import json
import pprint
from pymongo import MongoClient

# Connect to MongoDB Client
client = MongoClient('mongodb://dgogri:jc35uDs5@smgo7db01.smu.edu:27017/dgogridb')
# Choose the database to use as 'db'
db = client.dgogridb

# Get collections from dgogridb database and print them
collections = db.collection_names(include_system_collections=False)
print("Printing Collections Below")
for col in collections:
    print(col)


# Get data from quest6 collection and print them
print("\nPrinting Database Data Below")
for dataInDB in db.quest6.find({}, {"_id": 0} ):
    print(dataInDB)

