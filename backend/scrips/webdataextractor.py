from websitedata import *

class WebDataExtractor:
    
    def __init__(self):
        self._realestates = []
    
    def addwebsite(self, realestatewebsite):
        self._realestates.append(realestatewebsite)
    
    def addallwebsite(self, realestatewebsites):
        self._realestates.extend(realestatewebsites)
    
    def transformToJson(websitedata):
        return websitedata.toJson()
    
    def getallwebsitedata(self):
        return list(map(self.transformToJson, self._realestates))
    
