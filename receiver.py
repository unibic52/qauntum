import random
from quantum_key_generator import QuantumKeyGenerator


key = "10101011"

rec_public_key=[]
basis = ['rectilinear', 'diagonal']

binary = []

states = {
    'rectilinear': {'--': 0, '|': 1},
    'diagonal': {'-': 1, '+': 0}
}

def receiver1(pol):

  for x in range(0,len(key)):
    new1 = random.choice(basis)
    rec_public_key.append(new1)


  for x in range(0,len(key)):
    try: 
      binary.append(states[rec_public_key[x]][pol[x]])
    except KeyError:
      pass
  
  return(binary)



 
