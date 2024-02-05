import asyncio

class Persona:
    _instanciadepersona = None
        
    @staticmethod    
    def getinstance():
        if Persona._instanciadepersona == None:
            print("Instancia de persona no existe, lo vamos a crear")
            Persona._instanciadepersona = "Hola, soy una persona"
        
        return Persona._instanciadepersona 
    
    
class PersonaAsyn:
    
    async def imprimir1(self):
        await asyncio.sleep(3)
        print('impresion de prueba 1')
    
    async def imprimir2(self):
        await asyncio.sleep(3)
        print('impresion de prueba 2')    
        
    

async def main ():
    
    # ins1 = Persona.getinstance()
    # ins2 = Persona.getinstance()
    # ins3 = Persona.getinstance()
    
    # print(ins1)
    # print(ins2)
    # print(ins3)
    
    personaasyn = PersonaAsyn()
     
    listtask = []
    listtask.append(asyncio.create_task(personaasyn.imprimir1()))
    listtask.append(asyncio.create_task(personaasyn.imprimir2()))
    
    await asyncio.gather(*listtask)
    

if __name__ == "__main__":
    asyncio.run(main())