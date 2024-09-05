import binascii
from Crypto.Cipher import DES3
from Crypto.Util.Padding import pad, unpad
import binascii

def triple_des_encrypt(plaintext_hex, key_hex, iv_hex):
    key = binascii.unhexlify(key_hex)
    iv = binascii.unhexlify(iv_hex)
    plaintext = binascii.unhexlify(plaintext_hex)

    cipher = DES3.new(key, DES3.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pad(plaintext, DES3.block_size))
    return binascii.hexlify(ciphertext).decode('utf-8')

# User input
plaintext_hex = input("Enter plaintext (hex): ")
key_hex = input("Enter key (hex, 24 bytes): ")
iv_hex = input("Enter IV (hex, 8 bytes): ")
ciphertext = triple_des_encrypt(plaintext_hex, key_hex, iv_hex)
print(f"Ciphertext: {ciphertext}")
