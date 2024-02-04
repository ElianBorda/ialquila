from scrapingdatabuilder import *

class ScrapingDataDirector:
    
    async def getwebdata(self, builder, soup):
        
        cards = []
        currentsoup = soup
        print('llega a la parte de getwebdata en ScrapingDataDirector')

        while (builder.nextpage(currentsoup) != None):
            cards.append(builder.getdatacards(currentsoup))
            currentsoup = builder.nextpage(currentsoup)
        
        return cards
