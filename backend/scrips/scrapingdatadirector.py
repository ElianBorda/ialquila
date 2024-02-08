from scrapingdatabuilder import *
import asyncio
from colorama import Fore, Back, Style, init


class ScrapingDataDirector:
    
    async def getwebdata(self, builder, soup):
        
        cardstasks = []
        souplistpages = await builder.generatepagelist(soup)
        for souppage in souplistpages:
            datacardstask = asyncio.create_task(builder.getdatacards(souppage))
            # print(Fore.LIGHTMAGENTA_EX + "Se crea una tarea para la obtencion de las tarjetas" + Style.RESET_ALL)
            cardstasks.append(datacardstask)
            
        return datacardstask
        
        
    # async def _generatelistpag(self, initialsoup, builder):
    #     listpages = [initialsoup]
    #     nextpage  = await builder.nextpage(initialsoup) 
        
    #     while (nextpage != None):
    #         listpages.append(nextpage)
    #         nextpage = await builder.nextpage(nextpage)
            
    #     return listpages
        
