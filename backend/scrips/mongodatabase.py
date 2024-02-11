from pymongo import MongoClient
from pymongo import errors
from colorama import Fore, Back, Style, init
import asyncio



class MongoDataBase:
    
    async def getdatabase(self):
        connectionstring = "mongodb://localhost:27017/"
        client= MongoClient(connectionstring)
        return client["ialquila"]
    
    async def insertdata(self, listwebsitedata):
        dbname = await self.getdatabase()
        collectionname = dbname["producto"]
        tasksinsert = []
        
        for data in listwebsitedata:
            print(Fore.YELLOW + "======== DATO INSERTADO EN MONGO ========" + Style.RESET_ALL)
            filter = {
                'titulo'   : data['titulo'],
                'img'      : data['img'],
                'ubicacion': data['ubicacion']
                }
            updatedata = {'$set': data}
            task = asyncio.create_task(collectionname.update_one(filter, updatedata, upsert=True))
            tasksinsert.append(task)
        
        await asyncio.gather(*tasksinsert)    
            
        