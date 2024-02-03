class Persona:
    _instanciadepersona = None
        
    @staticmethod    
    def getinstance():
        if Persona._instanciadepersona == None:
            print("Instancia de persona no existe, lo vamos a crear")
            Persona._instanciadepersona = "Hola, soy una persona"
        
        return Persona._instanciadepersona 
    

def main ():
    
    ins1 = Persona.getinstance()
    ins2 = Persona.getinstance()
    ins3 = Persona.getinstance()
    
    print(ins1)
    print(ins2)
    print(ins3)
    

if __name__ == "__main__":
    main()