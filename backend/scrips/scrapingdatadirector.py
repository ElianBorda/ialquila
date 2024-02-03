from scrapingdatabuilder import *

class ScrapingDataDirector:
    
    def getwebdata(self, builder, soup):
        
        # cards = []
        
        print('llega a la parte de getwebdata en ScrapingDataDirector')
        
        paginate = builder.generatepaginate(soup)
        print(paginate is None)
        
        # while (builder.nextpage(paginate) != None):
        #     cards.append(builder.getdatacards(paginate))
            
        # return cards
