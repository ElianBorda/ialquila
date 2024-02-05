from tqdm import tqdm

class BarSingleton:
    
    _barinstance = None
    
    @classmethod    
    def getinstance(cls):
        if cls._barinstance is None:
            cls._barinstance = tqdm(total=100, desc="Procesando", unit="elemento")
        
        return cls._barinstance 
    
    @classmethod    
    def updatebar(cls, numupdate):
        if cls._barinstance is not None:
            cls._barinstance.update(numupdate)
            
    @classmethod    
    def closebar(cls):
        if cls._barinstance is not None:
            cls._barinstance.close()

