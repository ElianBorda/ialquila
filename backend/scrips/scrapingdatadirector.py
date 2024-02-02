from scrapingdatabuilder import *

class ScrapingDataDirector:
    
    def getwebdata(self, builder, soup):
        
        cards = []
        
        paginate = builder.generatepaginate(soup)
        while (builder.nextpage(paginate) != None):
            cards.append(builder.getdatacards(paginate))
            
        return cards
