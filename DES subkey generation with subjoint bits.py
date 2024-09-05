def generate_subkeys(key_hex):
    key = binascii.unhexlify(key_hex)
    left = key[:28]
    right = key[28:56]

    subkeys = []
    for i in range(16):
        left_shifted = left[i % 28:] + left[:i % 28]
        right_shifted = right[i % 28:] + right[:i % 28]
        subkey = left_shifted + right_shifted
        subkeys.append(binascii.hexlify(subkey).decode('utf-8'))
    
    return subkeys

# User input
key_hex = input("Enter key (hex, 56 bits, 14 hex chars): ")
subkeys = generate_subkeys(key_hex)
print(f"Generated Subkeys: {subkeys}")
