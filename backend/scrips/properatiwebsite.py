from realestatewebsitestrategy import *
from websitedata import *

class ProperatiWebsite(RealEstateWebsiteStrategy):
    
    def __init__(self, urlwebsite):
        super().__init__(urlwebsite)
        
        # Necesita corrutina
    def getwebsitedata(self):
        soup = super.generatesoup()
        
        return WebsiteData("","",0,"","","","","","")