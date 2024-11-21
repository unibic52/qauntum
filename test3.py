states = {
    'rectilinear': {'--': 0, '|': 1},
    'diagonal': {'-': 1, '+': 0}
}

try:
    print(states['rectilinear']['-'])

except KeyError:
    print(states['diagonal']['-'])
