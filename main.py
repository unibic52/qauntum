from sender import QuantumKeyGenerator
from receiver import QuantumReceiver


sender_public_key = []
reciver_public_key = []

key = "10101001"

qkg = QuantumKeyGenerator(key)
rkg = QuantumReceiver()
rkg.receiver(qkg.run())

sender_key = qkg.new_key(rkg.rec_public_key)
receiver_key = rkg.decode(qkg.public_key)


print(sender_key)
print(receiver_key)

