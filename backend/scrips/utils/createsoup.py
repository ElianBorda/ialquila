import asyncio
import aiohttp
from bs4 import BeautifulSoup

async def create_soup(session, url):
    return BeautifulSoup(await fetch_page(session, url), 'html.parser')

async def fetch_page(session, url):
    async with session.get(url) as res:
        return await res.text()