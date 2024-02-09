from pymongo import MongoClient
from pymongo import errors

def getdatabase():
    connectionstring = "mongodb://localhost:27017/"
    client=MongoClient(connectionstring)
    return client["ialquila"]

def main():
    dbname = getdatabase()
    collectionname = dbname["producto"]
    item_1 = {
        "_id" : "U1IT0000990",
        "item_name" : "Blender",
        "max_discount" : "10%",
        "batch_number" : "RR450020FRG",
        "price" : 340,
        "category" : "kitchen appliance"
    }

    # item_2 = {
    # "_id" : "U1IT00002",
    # "item_name" : "Egg",
    # "category" : "food",
    # "quantity" : 12,
    # "price" : 36,
    # "item_description" : "brown country eggs"
    # }
    # collectionname.insert_one(item_1)
    
    
    collectionname.insert_one(item_1)
    

if __name__ == '__main__':
    
    main()
    
