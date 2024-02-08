from websitedata import *
import asyncio
import aiohttp
from clientsingleton import *
from barsingleton import *
from colorama import Fore, Back, Style, init


class WebDataExtractor:
    
    def __init__(self):
        self._realestates = []
    
    def addwebsite(self, realestatewebsite):
        self._realestates.append(realestatewebsite)
    
    def addallwebsite(self, realestatewebsites):
        self._realestates.extend(realestatewebsites)
    
    # async def transformtojson(self):
    #     websitedata = await realestatewebsites.getwebsitedata()
        
    #     return websitedata.toJson()
    
    # Necesita corrutina
    def transformtojson(self, webssitesdata):
        jsons = []
        
        for web in webssitesdata:
            jsons.append(web.toJson())
            
        return jsons
        
    
    async def getallwebsitedata(self):
        websdatatask = []
        timeout=50000
        
        for realestate in self._realestates:
            webtask = asyncio.create_task(realestate.getwebsitedata())
            websdatatask.append(webtask)
            # print(Fore.YELLOW + "Se crea una tarea para una pagina web" + Style.RESET_ALL)
            
        try: 
            websdata = await asyncio.wait_for(asyncio.gather(*websdatatask), timeout)
            return websdata
        except asyncio.exceptions.TimeoutError:
            print(f"La operacion ha superado el tiempo de espera: {timeout}")
            return []
        
        
    
