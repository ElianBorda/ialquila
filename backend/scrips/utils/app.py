from pymongo import MongoClient
from pymongo import errors
import certifi

def getdatabase():
    connectionstring = "mongodb+srv://elian21:LlSM8VhaFcR4i9ZA@cluster0.oljii16.mongodb.net/?retryWrites=true&w=majority"
    client=MongoClient(connectionstring, tlsCAFile=certifi.where())
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
    
    
    try:
        collectionname.insert_one(item_1)
    except errors.PyMongoError as e:
        print(f"Error de MongoDB: {e}")

    

if __name__ == '__main__':
    
    main()
    
