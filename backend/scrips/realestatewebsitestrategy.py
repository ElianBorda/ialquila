from abc import ABC, abstractmethod
from bs4 import BeautifulSoup
import asyncio
import aiohttp
from clientsingleton import *

class RealEstateWebsiteStrategy(ABC): 
    """RealEstateWebsiteStrategy es una clase abstracta.
    
    Sus subclases poseen distintos algoritmos para extraer datos de distintas
    paginas webs. 
    
    metodo getwebsitedata: dependiendo de la subclase, extrae los datos de una pagina web particular.
    
    metodo generatesoup: genera una instancia de html para extraer datos.
    """
    
    def __init__(self, urlwebsite):
        self._urlwebsite = urlwebsite
        
    @abstractmethod    
    async def getwebsitedata(self):
        pass
    
    async def generatesoup(self):
        session = ClientSingleton.getinstance()
        html    = ""
        async with session.get(self._urlwebsite) as res:
            html = await res.text()
        
        return BeautifulSoup(html,session)