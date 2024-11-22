import random

class QuantumReceiver:
    def __init__(self):
        self.rec_public_key = []  
        self.rec_polars = []     
        self.binary = []         
        self.bk = []            
        self.states = {          
            'rectilinear': {'--': 0, '|': 1},
            'diagonal': {'-': 1, '+': 0}
        }
        self.basis = ['rectilinear', 'diagonal']  

    def receiver(self, pol):

        self.rec_public_key = [random.choice(self.basis) for _ in range(0,8)]

        for x in range(0,8):
            try:
                # Map the polar value and append to binary
                self.binary.append(self.states[self.rec_public_key[x]][pol[x]])
                self.rec_polars.append(pol[x])
            except KeyError:
                # Handle invalid polar keys
                random_polar = random.choice(list(self.states[self.rec_public_key[x]].keys()))
                self.rec_polars.append(random_polar)
                self.binary.append(self.states[self.rec_public_key[x]][random_polar])

        return self.binary

    def decode(self, sedpub):

        for x in range(len(sedpub)):
            try:
                self.bk.append(self.states[sedpub[x]][self.rec_polars[x]])
            except KeyError:
                pass

        return self.bk



