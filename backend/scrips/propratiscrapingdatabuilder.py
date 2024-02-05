from scrapingdatabuilder import *
from pager import *
from soupcreator import *
from websitedata import *
import asyncio 
import re

class ProperatiScrapingDataBuilder(ScrapingDataBuilder):

    
    async def nextpage(self, soup):
        try:
            listelempagination = soup.find_all('a', class_='pagination__link')
            elempagination     = listelempagination[-1]
            urlnextpage        = elempagination["href"]
            return await SoupCreator.generatesoup(urlnextpage)
        except Exception as e:
            return None 
    
    async def getdatacards(self, soup):
        datacardstasks = []
        for card in self._getcards(soup):
            datacardtask = asyncio.create_task(self.getdatacard(card, soup))
            datacardstasks.append(datacardtask)
            
        datacards = await asyncio.gather(*datacardstasks)    
            
        return datacards
    
    async def getdatacard(self, soup, soupcards):
        
        return WebsiteData(
            self._getdatatitle(soup),
            self._getdatadesc(soup),
            self._getdataprice(self._getprice(soup)),
            self._getdataexchange(self._getprice(soup)),
            self._getdataimg(soup),
            self._getdatalocation(soup),
            self._getdatalink(soup),
            self._getdatacategory(soupcards),
            self._getdataresidence(soupcards)
        )
    
    def _getcards(self, soup):
        return soup.find_all('div', class_='listing-card')
    
    def _getdatatitle(self, soup):
        return soup.find('div', class_='listing-card__title').text
    
    def _getdatadesc(self, soup):
        return ""

    def _getprice(self, soup):
        info = (soup.find('div', class_='listing-card__information')).find('div', class_='listing-card__information-main')
    
        return (info.find('div', class_='listing-card__price-wrapper')).find('div', class_='price').text
    
    def _getdataprice(self, price):
        priceclear   = 0
        if price != 'Consultar':
             priceclear   = float(price.replace('$ ', '').replace('USD ', '').replace('.', ''))
        return priceclear
    
    def _getdataexchange(self, price):
        exchange = 'Consultar'
        if price != 'Consultar':
             exchange =  re.sub(r'[\d,]+', '', price).replace('.', ''). replace(' ','')
        return exchange
    
    def _getdataimg(self, soup):
        return soup.find('img', class_='swiper-no-swiping')['src']
    
    def _getdatalocation(self, soup):
        return soup.find('div', class_='listing-card__location').text

    def _getdatalink(self, soup):
        
        return ""

    def _getdatacategory(self, soup):
        optionsfilters = soup.find_all('li', class_='breadcrumb-item')
        return optionsfilters[0].text
    
    def _getdataresidence(self, soup):
        optionsfilters = soup.find_all('li', class_='breadcrumb-item')        
        return optionsfilters[1].text
        
        