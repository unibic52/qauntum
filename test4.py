import random
from quantum_key_generator import QuantumKeyGenerator

key = "10101011"  # Example binary key

rec_public_key = []  # To store the receiver's basis
basis = ['rectilinear', 'diagonal']  # Possible bases
binary = []  # To store the decoded binary key

states = {
    'rectilinear': {'--': 0, '|': 1},  # Rectilinear states
    'diagonal': {'-': 1, '+': 0}      # Diagonal states
}

def receiver1(pol):
    """
    Decodes a given polarization key (pol) based on the receiver's randomly chosen basis.
    
    Args:
        pol (list): The polarization states as a list of strings.

    Returns:
        list: The decoded binary key based on the receiver's basis and polarization.
    """
    print("Type of pol:", type(pol))  # Debugging type
    print("Value of pol:", pol)       # Debugging value
    
    # Generate a random basis for the receiver
    for _ in range(len(key)):
        rec_public_key.append(random.choice(basis))
    
    # Decode the polarization key into binary
    for x in range(len(key)):
        try:
            binary.append(states[rec_public_key[x]][pol[x]])  # Lookup based on basis and pol
        except KeyError as e:
            print(f"KeyError at index {x}: {e}")  # Optional debug message for missing key
            binary.append(None)  # Graceful handling (e.g., append None if an error occurs)
    
    return binary

qkg = QuantumKeyGenerator(key)
pol = qkg.run()
print(receiver1(pol))