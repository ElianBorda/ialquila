import re
import json
import asyncio
import aiohttp
from bs4 import BeautifulSoup

async def main():
    tasks = []
    file_route = "./datasw.json"
    async with aiohttp.ClientSession() as session: 
        soup = await create_soup(session, 'https://www.properati.com.ar/s/bernal/departamento/alquiler')
        cards = soup.find_all('div', class_='listing')
        for card in cards:
            tasks.append(asyncio.create_task(get_data(session, card)))    
        
        data = await asyncio.gather(*tasks)        
        with open(file_route, 'w') as file:
            json.dump(data, file, indent=2)

async def create_soup(session, url):
    return BeautifulSoup(await fetch_page(session, url), 'html.parser')


async def fetch_page(session, url):
    async with session.get(url) as res:
        return await res.text()
    
async def get_data(session, card):
        img           = card.find('div', class_='listing-card__image').find('div', class_='gallery-swiper-container').find('div', class_='swiper-wrapper').find('div', class_='swiper-slide').find('img', class_='swiper-no-swiping')['src']
        info          = (card.find('div', class_='listing-card__information')).find('div', class_='listing-card__information-main')
        title         = card.find('div', class_='listing-card__title').text
        price         = (info.find('div', class_='listing-card__price-wrapper')).find('div', class_='price').text
        location      = card.find('div', class_='listing-card__location').text
        price_clear   = float(price.replace('$ ', '').replace('USD ', '').replace('.', ''))
        exchange_rate = re.sub(r'[\d,]+', '', price).replace('.', ''). replace(' ','')
        link_button   = card.get("data-href")
        desc   = (await create_soup(session, f"https://www.properati.com.ar/{card.get('data-href')}")).find('div', class_='description').text

        return {
                "titulo"     : title, 
                "descripcion": desc,
                "precio"     : price_clear,
                "cambio"     : exchange_rate,
                "img"        : img,
                "ubicacion"  : location,
            }
        
if __name__ == '__main__':
    asyncio.run(main())