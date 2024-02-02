from realestatewebsitestrategy import *
from websitedata import *
from propratiscrapingdatabuilder import *
from scrapingdatadirector import * 

class ProperatiWebsite(RealEstateWebsiteStrategy):
    
    def __init__(self, urlwebsite): 
        super().__init__(urlwebsite)
        
        # Necesita corrutina
    async def getwebsitedata(self):
        
        """getwebsitedata: Lista de websites
        soup = pagina web con tarjetas y paginado. 
        debemos extraer los datos, y pasar a la siguiente pagina
        Con otro obj podriamos extraer los datos. Director getdataproperati(soup)
        
        """
        
        soup = super.generatesoup()
        builder = ProperatiScrapingDataBuilder()
        director = ScrapingDataDirector()
        

        
        return director.getwebdata(builder, soup)