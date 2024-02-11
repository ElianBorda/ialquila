from realestatewebsitestrategy import *
from properatiwebsite import *
from webdataextractor import *
import asyncio
import time
from colorama import Fore, Back, Style, init
from barsingleton import *
from mongodatabase import MongoDataBase

async def main():
        # https://www.properati.com.ar/s/departamento/venta?minPrice=1000000000
        try: 
            mongodb          = MongoDataBase()
            webdataextractor = WebDataExtractor()
            # webdataextractor.addwebsite(ProperatiWebsite("https://www.properati.com.ar/s/departamento/venta?minPrice=1000000000"))
            webdataextractor.addwebsite(ProperatiWebsite("https://www.properati.com.ar/s/departamento/venta"))
            webdataextractor.addwebsite(ProperatiWebsite("https://www.properati.com.ar/s/departamento/alquiler"))
            webdataextractor.addwebsite(ProperatiWebsite("https://www.properati.com.ar/s/casa/alquiler"))
            webdataextractor.addwebsite(ProperatiWebsite("https://www.properati.com.ar/s/casa/venta"))
            data = await webdataextractor.getalljsondata()
            await mongodb.insertdata(data)
        finally:
            await ClientSingleton.closesession()

if __name__ == "__main__":
    init = time.time()
    asyncio.run(main())
    finish = time.time()
    total = finish - init 
    print(Fore.GREEN + "Test terminado: el tiempo total es de " + str(total) + Style.RESET_ALL)