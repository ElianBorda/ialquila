from pymongo import MongoClient
from pymongo import errors
from colorama import Fore, Back, Style, init
import asyncio
import certifi



class MongoDataBase:
    
    async def getdatabase(self):
        connectionstring = "mongodb+srv://elian21:LlSM8VhaFcR4i9ZA@cluster0.oljii16.mongodb.net/?retryWrites=true&w=majority"
        client= MongoClient(connectionstring, tlsCAFile=certifi.where())
        return client["ialquila"]
    
    async def getcollection(self):
        dbname = await self.getdatabase()
        collectionname = dbname["producto"]
        return collectionname
    
    async def insertdata(self, listwebsitedata):
        collectionname = await self.getcollection()
        tasksinsert = []
        
        for data in listwebsitedata:
            filter = {
                'swid': data['swid']
                }
            updatedata = {'$set': data}
            loop = asyncio.get_event_loop()
            task = loop.run_in_executor(None, collectionname.update_one, filter, updatedata, True)
            tasksinsert.append(task)
            print(Fore.YELLOW + "======== DATO INSERTADO EN MONGO ========" + Style.RESET_ALL)
        
        await asyncio.gather(*tasksinsert)    
            
        