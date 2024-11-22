import random
from quantum_key_generator import QuantumKeyGenerator
import receiver


sender_public_key = []
reciver_public_key = []
new_key = []
key = "10101001"

qkg = QuantumKeyGenerator(key)
polar1 = qkg.run()
new_key = receiver.receiver1(polar1)

sender_public_key = qkg.public_key
reciver_public_key = receiver.rec_public_key

print(new_key)

sender_key = 


