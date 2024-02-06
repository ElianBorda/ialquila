import aiohttp


class ClientSingleton:
    """La clase ClientSingleton permite generar una sola sesion y cerrarla.
    
    Se recomienda que la sesion se cierre en el main
    
        async def main():
            #Logica inicial del programa
            
            ClientSingleton.closesession()
    """
    
    
    _clientinstance = None
        
    @classmethod    
    async def getinstance(cls):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        if cls._clientinstance is None:
            cls._clientinstance = aiohttp.ClientSession(headers=headers)
        
        return cls._clientinstance 
    
    @classmethod
    async def closesession(cls):
        if cls._clientinstance is not None:
            await cls._clientinstance.close()
            cls._clientinstance = None