import pymongo

if __name__ == "__main__":
    client = pymongo.MongoClient("mongodb://localhost:27017")
    print(client)
    db = client['harry']
    collection = db["mySampleCollectionForHarry"]
    collection.insert_one({"hello": "world"})

