from websitedata import *
import asyncio
import aiohttp
from clientsingleton import *


class WebDataExtractor:
    
    def __init__(self):
        self._realestates = []
    
    def addwebsite(self, realestatewebsite):
        self._realestates.append(realestatewebsite)
    
    def addallwebsite(self, realestatewebsites):
        self._realestates.extend(realestatewebsites)
    
    def transformtojson(self, realestatewebsites):
        websitedata = realestatewebsites.getwebsitedata()
        
        return websitedata.toJson()
    
    # Necesita corrutina
    def getallwebsitedata(self):
        tasks = list(map(self.transformtojson, self._realestates))
        
        session = ClientSingleton.getinstance()
        session.close()
        
        return tasks
    
