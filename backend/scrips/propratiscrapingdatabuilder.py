from scrapingdatabuilder import *
from pager import *
from soupcreator import *
from websitedata import *
import asyncio 
import re
import math
from colorama import Fore, Back, Style, init


class ProperatiScrapingDataBuilder(ScrapingDataBuilder):

    def __init__(self, urlwebsite): 
        super().__init__(urlwebsite)
     
    
    async def generatepagelist(self, soup):
        timeout = 50000
        soupamountcards   = soup.find('div', class_='pagination__summary').text
        amountcards       = re.search(r'de (\d+)', soupamountcards)
        numpags           = math.ceil(int(amountcards.group(1)) / 30)
        numpagsclear      = numpags if numpags <= 167 else 167
        souplistpagestask = []
        
        for numpag in range(2, numpagsclear+1):
            urlnextpage = self._urlwebsite + "/" + str(numpag)
            maybesoup   = asyncio.create_task(SoupCreator.generatesoup(urlnextpage))
            souplistpagestask.append(maybesoup)
            print(Fore.LIGHTBLUE_EX + "Tarea para la generacion de soup CREADA" + Style.RESET_ALL)
        
        souplistpages = await asyncio.wait_for(asyncio.gather(*souplistpagestask), timeout=timeout)
        souplistpages.append(soup)
        
        return souplistpages
        
    
    async def getdatacards(self, soup):
        
        datacardstasks = []
        if soup != None :
            for card in self._getcards(soup):
                datacardtask = asyncio.create_task(self.getdatacard(card, soup))
                datacardstasks.append(datacardtask)
                print(Fore.LIGHTGREEN_EX + "Tarea para la extraccion de datos CREADA" + Style.RESET_ALL)    
        else: 
            print(Fore.RED + "======== DATO PERDIDO ========" + Style.RESET_ALL)  
                    
        return datacardstasks
    
    async def getdatacard(self, soup, soupcards):

        print(Fore.LIGHTCYAN_EX + "Extrayendo datos de la card" + Style.RESET_ALL)
        return WebsiteData(
            self._getswid(soup),
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
    
    def _getswid(self, soup):
        pattern = re.compile(r'/detalle/([^"]+)')
        data = soup.get('data-href')
        code = pattern.search(data)
        codeextracted = code.group(1)
        return codeextracted
    
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
        
        