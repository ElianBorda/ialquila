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
        if cls._clientinstance is None:
            cls._clientinstance = aiohttp.ClientSession()
        
        return cls._clientinstance 
    
    @classmethod
    async def closesession(cls):
        if cls._clientinstance is not None:
            await cls._clientinstance.close()
            cls._clientinstance = None