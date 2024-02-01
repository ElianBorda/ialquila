#For Tests
import time
from colorama import Fore, Back, Style, init



import re
import json
import asyncio
import aiohttp
from utils import createsoup
from bs4 import BeautifulSoup

async def main():
    tasks = []
    async with aiohttp.ClientSession() as session: 
        page = 40
        for i in range(1, page+1):
            soup = await createsoup.create_soup(session, f'https://www.properati.com.ar/s/departamento/venta/{i}')
            tasks.append(asyncio.create_task(page_data(soup, session)))
            
        data_tasks = await asyncio.gather(*tasks)
        flattened_data = [item for sublist in data_tasks for item in sublist]
            
        data_json = await asyncio.gather(*flattened_data)
        
        print(data_json)

    
async def page_data(soup, session): 
    tasks    = []
    optionsfilters = soup.find_all('li', class_='breadcrumb-item')
    cards = soup.find_all('div', class_='listing-card')
    for card in cards:
        tasks.append(get_data(session, card, optionsfilters))    
        
    return tasks 


async def get_data(session, card, optionsfilters):
        
        price_clear   = 0
        exchange_rate = 'Consultar'
        img       = card.find('img', class_='swiper-no-swiping')['src']
        
        info          = (card.find('div', class_='listing-card__information')).find('div', class_='listing-card__information-main')
        title         = card.find('div', class_='listing-card__title').text
        price         = (info.find('div', class_='listing-card__price-wrapper')).find('div', class_='price').text
        location      = card.find('div', class_='listing-card__location').text
        
        if price != 'Consultar':
            price_clear   = float(price.replace('$ ', '').replace('USD ', '').replace('.', ''))
            exchange_rate = re.sub(r'[\d,]+', '', price).replace('.', ''). replace(' ','')
            
        # link_button   = card.get("data-href")
        # desc   = (await createsoup.create_soup(session, f"https://www.properati.com.ar/{card.get('data-href')}")).find('div', class_='description').text

        return {
                "titulo"     : title, 
                "precio"     : price_clear,
                "cambio"     : exchange_rate,
                "img"        : img,
                "ubicacion"  : location,
                "categoria"  : optionsfilters[0].text,
                "residencia" : optionsfilters[1].text
            }
        
if __name__ == '__main__':
    init = time.time()
    asyncio.run(main())
    finish = time.time()
    total = finish - init 
    print(Fore.GREEN + "Test terminado: el tiempo total es de " + str(total) + Style.RESET_ALL)