from websitedata import *


class WebDataExtractor:
    
    def __init__(self):
        self._realestates = []
    
    async def addwebsite(self, realestatewebsite):
        self._realestates.append(realestatewebsite)
    
    async def addallwebsite(self, realestatewebsites):
        self._realestates.extend(realestatewebsites)
    
    async def transformtojson(realestatewebsites):
        websitedata = realestatewebsites.getwebsitedata()
        
        return websitedata.toJson()
    
    # Necesita corrutina
    async def getallwebsitedata(self):
        return list(map(self.transformtojson, self._realestates))
    
