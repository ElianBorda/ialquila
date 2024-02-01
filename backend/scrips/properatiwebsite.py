from realestatewebsitestrategy import *
from websitedata import *

class ProperatiWebsite(RealEstateWebsiteStrategy):
    
    def __init__(self, urlwebsite):
        super().__init__(urlwebsite)
        
        # Necesita corrutina
    async def getwebsitedata(self):
        soup = super.generatesoup()
        
        ##¿Builder?
        
        return WebsiteData("","",0,"","","","","","")