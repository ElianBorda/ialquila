from abc import ABC, abstractmethod
from bs4 import BeautifulSoup
import asyncio
import aiohttp
from clientsingleton import *

class RealEstateWebsiteStrategy(ABC): 
    def __init__(self, urlwebsite):
        self._urlwebsite = urlwebsite
        
    @abstractmethod    
    def getwebsitedata(self):
        pass
    
    async def generatesoup(self):
        session = ClientSingleton.getinstance()
        html    = ""
        async with session.get(self._urlwebsite) as res:
            html = await res.text()
        
        return BeautifulSoup(html,session)