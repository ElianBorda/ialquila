import aiohttp


class ClientSingleton:
    def __init__(self):
        self._clientinstance = None
        
    @staticmethod    
    def getinstance(self):
        if self._clientinstance == None:
            self._clientinstance = aiohttp.ClientSession() 
        
        return self._clientinstance 