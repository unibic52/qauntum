import random
from quantum_key_generator import QuantumKeyGenerator

public_key=[]

basis = ['rectilinear', 'diagonal']

binary = []

states = {
    'rectilinear': {'--': 0, '|': 1},
    'diagonal': {'-': 1, '+': 0}
}

key = "10101011"
qkg = QuantumKeyGenerator(key)
polar = qkg.run()


for x in range(0,len(key)):
  new1 = random.choice(basis)
  public_key.append(new1)

for x in range(0,len(key)):
  try: 
    binary.append(states[public_key[x]][polar[x]])
  except KeyError:
    pass
print(key)
for i in binary:
    print(i, end="")
  
