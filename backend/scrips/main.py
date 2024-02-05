from realestatewebsitestrategy import *
from properatiwebsite import *
from webdataextractor import *
import aiohttp
import asyncio
import time
from colorama import Fore, Back, Style, init
from barsingleton import *

async def main():
        
        
        try: 
            webdataextractor = WebDataExtractor()
            webdataextractor.addwebsite(ProperatiWebsite("https://www.properati.com.ar/s/departamento/venta"))
            webdataextractor.addwebsite(ProperatiWebsite("https://www.properati.com.ar/s/departamento/alquiler"))
            webdataextractor.addwebsite(ProperatiWebsite("https://www.properati.com.ar/s/casa/alquiler"))
            webdataextractor.addwebsite(ProperatiWebsite("https://www.properati.com.ar/s/casa/venta"))
            websites = await webdataextractor.getallwebsitedata()
        finally:
            await ClientSingleton.closesession()


        # webdataextractor = WebDataExtractor()
        # webdataextractor.addwebsite(ProperatiWebsite("https://www.properati.com.ar/s/venta")


        # result = webdataextractor.getallwebsitedata()

        # return result

if __name__ == "__main__":
    init = time.time()
    asyncio.run(main())
    finish = time.time()
    total = finish - init 
    print(Fore.GREEN + "Test terminado: el tiempo total es de " + str(total) + Style.RESET_ALL)