import json
from pymongo import MongoClient 

myclient = MongoClient("mongodb+srv://dota2sideprojectcluster.nxzxp.mongodb.net/dota2_database", username="pogilmogil", password="mEThrXGbuFTFowoz") 


db = myclient["dota2_database"]

Collection = db["dota2_collection"]

Collection.delete_many({})

with open('heroes.json') as file:
    file_data = json.load(file)

Collection.insert_many(file_data)

#if isinstance(file_data, list):
    #Collection.insert_many(file_data)
#else:
    #Collection.insert_one(file_data)
