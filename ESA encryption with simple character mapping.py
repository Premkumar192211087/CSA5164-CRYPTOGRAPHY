from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii

def rsa_encrypt_characters(plaintext, public_key):
    cipher = PKCS1_OAEP.new(public_key)
    encrypted_blocks = [cipher.encrypt(bytes([ord(c)])) for c in plaintext]
    return [binascii.hexlify(block).decode('utf-8') for block in encrypted_blocks]

# User input
public_key = RSA.import_key(input("Enter public key (PEM format): "))
plaintext = input("Enter plaintext: ")
encrypted_blocks = rsa_encrypt_characters(plaintext, public_key)
print(f"Encrypted Blocks: {encrypted_blocks}")
