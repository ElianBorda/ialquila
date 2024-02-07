from clientsingleton import *
import aiohttp
import asyncio
from bs4 import *

class SoupCreator:
    
    @classmethod
    async def generatesoup(cls, url):
        session = await ClientSingleton.getinstance() 
        try:
            async with session.get(url) as res:
                text = await res.text()
                return BeautifulSoup(text,'html.parser')
        except aiohttp.ClientError as e:
            print(f"Hay problemas con la creacion del soup para el Url {url}: {e}")
            return None
            