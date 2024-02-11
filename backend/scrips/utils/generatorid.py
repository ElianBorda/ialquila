import random
import string

class GeneratorId:
    
    @classmethod
    def generateidstring():
        len = 50
        character = string.ascii_letters + string.digits
        id = ''.join(random.choice(character) for _ in range(len))
        return id