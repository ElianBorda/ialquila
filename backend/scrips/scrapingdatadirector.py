from scrapingdatabuilder import *
import asyncio

class ScrapingDataDirector:
    
    async def getwebdata(self, builder, soup):
        
        cardstasks = []
        listpages = await self._generatelistpag(soup, builder)
        
        for page in listpages:
            datacardstask = asyncio.create_task(builder.getdatacards(page))
            cardstasks.append(datacardstask)
        
        datacards = await asyncio.gather(*cardstasks)
        return datacards
        
    async def _generatelistpag(self, initialsoup, builder):
        listpages = [initialsoup]
        nextpage  = await builder.nextpage(initialsoup) 
        
        while (nextpage != None):
            listpages.append(nextpage)
            nextpage = await builder.nextpage(nextpage)
            
        return listpages
        
