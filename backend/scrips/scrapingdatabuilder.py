from abc import ABC, abstractmethod

class ScrapingDataBuilder(ABC):
    
    def __init__(self, urlwebsite):
        self._urlwebsite = urlwebsite
    
    # @abstractmethod
    # async def nextpage(self, soup):
    #     pass
    
    @abstractmethod
    async def generatepagelist(self, soup):
        pass
    
    @abstractmethod
    async def getdatacards(self, html):
        pass
    
    @abstractmethod
    async def getdatacard(self, html):
        pass
    
