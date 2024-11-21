import random

public_key=[]
key = 10101011

basis = ['rectilinear', 'diagonal']

states = {
    'rectilinear': {'hor': 0, 'ver': 1},
    'diagonal': {'neg': 1, 'pos': 0}
}

generate = ['hor', 'ver', 'neg', 'pos']

print(random.choice(generate))

for x in range(1,9):
  new1 = random.choice(basis)
  public_key.append(new1)
  
print(public_key)

generated = []

new = ""
for x in range(1,9):
    new = random.choice(generate)
    generated.append(new)

print(generated)

binary = []



for x in generated:
    if (x == 'hor'):
     binary.append(states['rectilinear']['hor'])
    if (x == 'ver'):
     binary.append(states['rectilinear']['ver'])
    if (x == 'neg'):
     binary.append(states['diagonal']['neg'])
    if (x == 'pos'):
     binary.append(states['diagonal']['pos'])

print(binary)
