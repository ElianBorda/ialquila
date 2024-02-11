from scrapingdatabuilder import *
import asyncio
from colorama import Fore, Back, Style, init


class ScrapingDataDirector:
    
    async def getwebdata(self, builder, soup):
        
        cardstasks = []
        souplistpages = await builder.generatepagelist(soup)
        for souppage in souplistpages:
            datacardstask = asyncio.create_task(builder.getdatacards(souppage))
            print(Fore.LIGHTMAGENTA_EX + "Tarea para la extraccion de las tarjetas CREADA" + Style.RESET_ALL)
            cardstasks.append(datacardstask)
            
        return cardstasks
        
