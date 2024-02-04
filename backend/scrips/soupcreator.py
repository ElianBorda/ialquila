from clientsingleton import *
from bs4 import *

class SoupCreator:
    
    @classmethod
    async def generatesoup(cls, url):
        session = await ClientSingleton.getinstance()
        async with session.get(url) as res:
            text = await res.text()
            return BeautifulSoup(text,'html.parser')