import random
from quantum_key_generator import QuantumKeyGenerator  

public_key=[]
key = "10101011"
polar=[]

basis = ['rectilinear', 'diagonal']

states = {
    'rectilinear': {'--': 0, '|': 1},
    'diagonal': {'-': 1, '+': 0}
}

for x in range(1,9):
  new1 = random.choice(basis)
  public_key.append(new1)

def find_key(category, value):
    return next((key for key, val in states.get(category, {}).items() if val == value), None)

for x in range(0, 8):
    polar.append(find_key(public_key[x], int(key[x])))


key = "10101011"
qkg = QuantumKeyGenerator(key)
