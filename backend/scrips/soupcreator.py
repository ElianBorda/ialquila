from clientsingleton import *
import aiohttp
import asyncio
from bs4 import *
from colorama import Fore, Back, Style, init


class SoupCreator:
    
    @classmethod
    async def generatesoup(cls, url):
        retry = 5
        retrydelay = 1
        session = await ClientSingleton.getinstance()
        
        for attempt in range(1, retry+1):
            try:
                async with session.get(url, timeout=5000) as res:
                    text = await res.text()
                    return BeautifulSoup(text,'html.parser')
            except aiohttp.ClientError as e:
                print(f"Hay problemas con la creacion del soup para el Url {url}: {e}")
            except ConnectionResetError as e:
                pass    
                
            await asyncio.sleep(retrydelay)
            