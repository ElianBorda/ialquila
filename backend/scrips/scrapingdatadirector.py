from scrapingdatabuilder import *

class ScrapingDataDirector:
    
    async def getwebdata(self, builder, soup):
        
        cards = []
        currentsoup = soup
        print('llega a la parte de getwebdata en ScrapingDataDirector')

        while (await builder.nextpage(currentsoup) != None):
            cards.append(builder.getdatacards(currentsoup))
            currentsoup = await builder.nextpage(currentsoup)
        
        print(cards)
        
        # return cards
