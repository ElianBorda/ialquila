from abc import ABC, abstractmethod

class ScrapingDataBuilder(ABC):
    
    @abstractmethod
    def generatepaginate(html):
        pass
    
    @abstractmethod
    def nextpage(paginate):
        pass
    
    @abstractmethod
    def getdatacards(html):
        pass
    
    @abstractmethod
    def getdatacard(html):
        pass
    
