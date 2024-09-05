from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
import binascii

def des_decrypt(ciphertext_hex, key_hex):
    key = binascii.unhexlify(key_hex)
    ciphertext = binascii.unhexlify(ciphertext_hex)
    
    des = DES.new(key, DES.MODE_ECB)
    decrypted = des.decrypt(ciphertext)
    return unpad(decrypted, DES.block_size).decode('utf-8')

# User input
ciphertext_hex = input("Enter ciphertext (hex): ")
key_hex = input("Enter key (hex, 8 bytes): ")
plaintext = des_decrypt(ciphertext_hex, key_hex)
print(f"Decrypted Text: {plaintext}")
