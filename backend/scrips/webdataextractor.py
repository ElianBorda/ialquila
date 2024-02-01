from websitedata import *

class WebDataExtractor:
    
    def __init__(self):
        self._realestates = []
    
    def addwebsite(self, realestatewebsite):
        self._realestates.append(realestatewebsite)
    
    def addallwebsite(self, realestatewebsites):
        self._realestates.extend(realestatewebsites)
    
    async def transformToJson(websitedata):
        return websitedata.toJson()
    
    # Necesita corrutina
    async def getallwebsitedata(self):
        return list(map(self.transformToJson, self._realestates))
    
