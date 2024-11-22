import receiver
from sender import QuantumKeyGenerator
binary = []
key = "10101011"
qkg = QuantumKeyGenerator(key)
pol = qkg.run()
public = qkg.public_key
pol = qkg.polar
binary = receiver.receiver1(pol)
pols = receiver.rec_pol
rec_pub = receiver.rec_public_key

for x in range(0, 8):
    if (public[x] == rec_pub[x]):
        pass
    else:
        print(key[x], public[x], pol[x], rec_pub[x], pols[x], binary[x])
