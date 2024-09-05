from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
import binascii

def encrypt_ecb(plaintext_hex, key_hex):
    key = binascii.unhexlify(key_hex)
    plaintext = binascii.unhexlify(plaintext_hex)
    cipher = DES.new(key, DES.MODE_ECB)
    ciphertext = cipher.encrypt(pad(plaintext, DES.block_size))
    return binascii.hexlify(ciphertext).decode('utf-8')

def encrypt_cbc(plaintext_hex, key_hex, iv_hex):
    key = binascii.unhexlify(key_hex)
    iv = binascii.unhexlify(iv_hex)
    plaintext = binascii.unhexlify(plaintext_hex)
    cipher = DES.new(key, DES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pad(plaintext, DES.block_size))
    return binascii.hexlify(ciphertext).decode('utf-8')

def encrypt_cfb(plaintext_hex, key_hex, iv_hex):
    key = binascii.unhexlify(key_hex)
    iv = binascii.unhexlify(iv_hex)
    plaintext = binascii.unhexlify(plaintext_hex)
    cipher = DES.new(key, DES.MODE_CFB, iv)
    ciphertext = cipher.encrypt(plaintext)
    return binascii.hexlify(ciphertext).decode('utf-8')

# User input
plaintext_hex = input("Enter plaintext (hex): ")
key_hex = input("Enter key (hex, 8 bytes): ")
iv_hex = input("Enter IV (hex, 8 bytes): ")

print("ECB Mode:", encrypt_ecb(plaintext_hex, key_hex))
print("CBC Mode:", encrypt_cbc(plaintext_hex, key_hex, iv_hex))
print("CFB Mode:", encrypt_cfb(plaintext_hex, key_hex, iv_hex))
