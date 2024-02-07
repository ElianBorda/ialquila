from scrapingdatabuilder import *
import asyncio

class ScrapingDataDirector:
    
    async def getwebdata(self, builder, soup):
        
        cardstasks = []
        souplistpages = await builder.generatepagelist(soup)
        
        for souppage in souplistpages:
            datacardstask = asyncio.create_task(builder.getdatacards(souppage))
            cardstasks.append(datacardstask)
        
        datacards = await asyncio.gather(*cardstasks)
        print(datacards)
        # return datacards
        
        
    # async def _generatelistpag(self, initialsoup, builder):
    #     listpages = [initialsoup]
    #     nextpage  = await builder.nextpage(initialsoup) 
        
    #     while (nextpage != None):
    #         listpages.append(nextpage)
    #         nextpage = await builder.nextpage(nextpage)
            
    #     return listpages
        
