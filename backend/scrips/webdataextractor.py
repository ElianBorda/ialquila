from websitedata import *
import asyncio
import aiohttp
from clientsingleton import *
from barsingleton import *

class WebDataExtractor:
    
    def __init__(self):
        self._realestates = []
    
    def addwebsite(self, realestatewebsite):
        self._realestates.append(realestatewebsite)
    
    def addallwebsite(self, realestatewebsites):
        self._realestates.extend(realestatewebsites)
    
    # async def transformtojson(self):
    #     websitedata = await realestatewebsites.getwebsitedata()
        
    #     return websitedata.toJson()
    
    # Necesita corrutina
    def transformtojson(self, webssitesdata):
        jsons = []
        
        for web in webssitesdata:
            jsons.append(web.toJson())
            
        return jsons
        
    
    async def getallwebsitedata(self):
        websdata = []
        for realestate in self._realestates:
            websitedata = await realestate.getwebsitedata()
            websdata.extend(websitedata)
        
        return websdata
    
