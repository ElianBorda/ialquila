from scrapingdatabuilder import *
from pager import *


class ProperatiScrapingDataBuilder(ScrapingDataBuilder):
    
    def generatepaginate(self, soup):
        paginate = Pager(soup)
        paginate.ppp()
        
        # return 

    
    def nextpage(paginate):
        return super().nextpage()
    
    def getdatacards(html):
        return super().getdatacards()
    
    def getdatacard(html):
        return super().getdatacard()