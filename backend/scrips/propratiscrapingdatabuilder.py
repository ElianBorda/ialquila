from scrapingdatabuilder import *
from pager import *
from soupcreator import *


class ProperatiScrapingDataBuilder(ScrapingDataBuilder):

    
    async def nextpage(self, soup):
        try:
            listelempagination = soup.find_all('a', class_='pagination__link')
            elempagination     = listelempagination[-1]
            urlnextpage        = elempagination["href"]
            return await SoupCreator.generatesoup(urlnextpage)
        except Exception as e:
            print("No hay una siguiente pagina")
            return None 
        
        
    
    def getdatacards(html):
        return super().getdatacards()
    
    def getdatacard(html):
        return super().getdatacard()