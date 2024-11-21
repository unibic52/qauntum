import random

class QuantumKeyGenerator:
    def __init__(self, key):
        self.key = key  # The binary key to encode
        self.public_key = []  # Stores the randomly chosen basis for each bit
        self.polar = []  # Stores the polarization states
        self.basis = ['rectilinear', 'diagonal']  # Available bases
        self.states = {
            'rectilinear': {'--': 0, '|': 1},
            'diagonal': {'-': 1, '+': 0}
        }

    
    def generate_public_key(self):
        """Randomly selects a basis for each bit in the key."""
        self.public_key = [random.choice(self.basis) for _ in range(len(self.key))]
    
    def find_key(self, category, value):
        """Finds the polarization state key for a given category and value."""
        return next((key for key, val in self.states.get(category, {}).items() if val == value), None)
    
    def encode_key(self):
        """Encodes the binary key into polarization states using the public key."""
        self.polar = [
            self.find_key(self.public_key[i], int(self.key[i]))
            for i in range(len(self.key))
        ]
    
    def run(self):
        """Main method to generate public key and encode the key."""
        self.generate_public_key()
        self.encode_key()
        return self.polar


key = "10101011"
qkg = QuantumKeyGenerator(key)
polar = qkg.run()

print("Polarization States:", polar)
