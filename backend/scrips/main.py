from realestatewebsitestrategy import *
from properatiwebsite import *
from webdataextractor import *
import aiohttp
import asyncio

async def main():
        try: 
            properati = ProperatiWebsite("https://www.properati.com.ar/s/venta")
            await properati.getwebsitedata()
        finally:
            await ClientSingleton.closesession()


        # webdataextractor = WebDataExtractor()
        # webdataextractor.addwebsite(ProperatiWebsite("https://www.properati.com.ar/s/venta"))


        # result = webdataextractor.getallwebsitedata()

        # return result

if __name__ == "__main__":
    asyncio.run(main())