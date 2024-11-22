import random

class QuantumKeyGenerator:
    def __init__(self, key):
        self.key = key 
        self.public_key = []  
        self.polar = []  
        self.binary = []
        self.basis = ['rectilinear', 'diagonal']  
        self.states = {
            'rectilinear': {'--': 0, '|': 1},
            'diagonal': {'-': 1, '+': 0}
        }

    
    def generate_public_key(self):
        self.public_key = [random.choice(self.basis) for _ in range(0, 8)]
        return(self.public_key)

    
    def find_key(self, category, value):
        return next((key for key, val in self.states.get(category, {}).items() if val == value), None)
    
    def encode_key(self):
        self.polar = [
            self.find_key(self.public_key[i], int(self.key[i]))
            for i in range(len(self.key))
        ]
    
    def run(self):

        self.generate_public_key()
        self.encode_key()
        return self.polar
    
    def new_key(self, recpub):

          
        for x in range(0,8):
            try: 
                self.binary.append(self.states[recpub[x]][self.polar[x]])
            except KeyError:
                pass
        return self.binary







