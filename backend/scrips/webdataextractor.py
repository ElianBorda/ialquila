from websitedata import *
import asyncio
import aiohttp
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm
from clientsingleton import *
from barsingleton import *
from colorama import Fore, Back, Style, init


class WebDataExtractor:
    
    def __init__(self):
        self._realestates = []
        self._currentdata = []
    
    def addwebsite(self, realestatewebsite):
        self._realestates.append(realestatewebsite)
    
    def addallwebsite(self, realestatewebsites):
        self._realestates.extend(realestatewebsites)
    
    async def getalljsondata(self):
        await self.getallwebsitedata()
        
        return list(map(lambda objwebsitedata: objwebsitedata.toJson(), self._currentdata))
        
    
    async def getallwebsitedata(self):
        websdatatask = []
        timeout=50000
        loop = asyncio.get_event_loop()
        
        for realestate in self._realestates:
            webtask = loop.run_in_executor(None, realestate.getwebsitedata)
            # webtask = asyncio.create_task(realestate.getwebsitedata())
            websdatatask.append(webtask)
            # print(Fore.YELLOW + f"Tarea para la pagina web CREADA" + Style.RESET_ALL)
            
        try: 
            webdatalist = await self._tasksToObjectWebData(websdatatask)
            self._currentdata = webdatalist
            return webdatalist
        except asyncio.exceptions.TimeoutError:
            print(f"La operacion ha superado el tiempo de espera: {timeout}")
            return []
        
    
    async def _tasksToObjectWebData(self, tsksss):
        
        tsk   = []
        tsks  = []
        tskss = []
        
        inst3 = await asyncio.gather(*tsksss)
        for datalist in inst3:
            tskss.extend(await datalist)
            
        
        for datalist in tskss:
            tsks.extend(datalist)
        
        for datalist in tsks:
            tsk.extend(datalist)
                
        return tsk
    
