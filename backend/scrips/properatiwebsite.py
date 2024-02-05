from realestatewebsitestrategy import *
from websitedata import *
from propratiscrapingdatabuilder import *
from scrapingdatadirector import * 

class ProperatiWebsite(RealEstateWebsiteStrategy):
    
    def __init__(self, urlwebsite): 
        super().__init__(urlwebsite)
        
        # Necesita corrutina
        
    async def getwebsitedata(self):
        
        soup = await super().generatesoup()
        builder = ProperatiScrapingDataBuilder()
        director = ScrapingDataDirector()
        
        return await director.getwebdata(builder, soup) 
    
    """ Si en un futuro queremos hacer web scraping con selenium, no nesesariamente 
    vamos a  beautifulsoup utilizar es decir, vamos a hacerlo mas escalable a futuro
    """
    