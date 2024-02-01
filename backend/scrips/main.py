from realestatewebsitestrategy import *
from properatiwebsite import *
from webdataextractor import *
import aiohttp
import asyncio

webdataextractor = WebDataExtractor()
webdataextractor.addwebsite(ProperatiWebsite("https://www.properati.com.ar/s/venta"))

if __name__ == "__main__":
    asyncio.run(webdataextractor.getallwebsitedata)