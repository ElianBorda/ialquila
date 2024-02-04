from abc import ABC, abstractmethod

class ScrapingDataBuilder(ABC):
    
    @abstractmethod
    async def nextpage(self, soup):
        pass
    
    @abstractmethod
    def getdatacards(self, html):
        pass
    
    @abstractmethod
    def getdatacard(self, html):
        pass
    
