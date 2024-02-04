from scrapingdatabuilder import *
from pager import *
from soupcreator import *
from websitedata import * 


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
    
    def getdatacards(self, soup):
        datacards = []
        for card in self._getcards(soup):
            datacards.append(self.getdatacard(card))
        return datacards
    
    def getdatacard(self, soup):
        return WebsiteData(
            self._getdatatitle(soup),
            self._getdatadesc(soup),
            
        )
    
    def _getcards(self, soup):
        return soup.find_all('div', class_='listing-card')
    
    def _getdatatitle(self, soup):
        return soup.find('div', class_='listing-card__title').text
    
    def _getdatadesc(self, soup):
        return ""

    def _getdatatitle(self, soup):
        return soup.find('div', class_='listing-card__title').text
    
    def _getdataprice(self, soup):
        info = (soup.find('div', class_='listing-card__information')).find('div', class_='listing-card__information-main')
    
        return (info.find('div', class_='listing-card__price-wrapper')).find('div', class_='price').text
    
        