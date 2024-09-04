import numpy as np

def mod_inverse(matrix, modulus):
    # Find the determinant
    det = int(np.round(np.linalg.det(matrix))) % modulus
    # Find the modular inverse of the determinant
    det_inv = pow(det, -1, modulus)
    
    # Find the matrix of cofactors
    cofactors = np.linalg.inv(matrix).T * np.linalg.det(matrix)
    cofactors = np.round(cofactors).astype(int) % modulus
    
    # Compute the inverse matrix
    inverse_matrix = (det_inv * cofactors) % modulus
    return inverse_matrix

def hill_cipher_encrypt(plaintext, key_matrix):
    modulus = 26  # For the alphabet
    plaintext = plaintext.upper().replace(" ", "")
    n = key_matrix.shape[0]

    # Pad the plaintext to ensure it's divisible by the size of the key matrix
    while len(plaintext) % n != 0:
        plaintext += 'X'

    # Convert plaintext to numerical form
    plaintext_vector = [ord(char) - ord('A') for char in plaintext]

    # Encrypt the plaintext
    encrypted_vector = []
    for i in range(0, len(plaintext_vector), n):
        block = np.array(plaintext_vector[i:i + n])
        encrypted_block = np.dot(key_matrix, block) % modulus
        encrypted_vector.extend(encrypted_block)

    # Convert back to text
    encrypted_text = ''.join(chr(num + ord('A')) for num in encrypted_vector)
    return encrypted_text

def hill_cipher_decrypt(ciphertext, key_matrix):
    modulus = 26  # For the alphabet
    n = key_matrix.shape[0]
    
    # Get the inverse of the key matrix
    inverse_key_matrix = mod_inverse(key_matrix, modulus)

    # Convert ciphertext to numerical form
    ciphertext_vector = [ord(char) - ord('A') for char in ciphertext]

    # Decrypt the ciphertext
    decrypted_vector = []
    for i in range(0, len(ciphertext_vector), n):
        block = np.array(ciphertext_vector[i:i + n])
        decrypted_block = np.dot(inverse_key_matrix, block) % modulus
        decrypted_vector.extend(decrypted_block)

    # Convert back to text
    decrypted_text = ''.join(chr(num + ord('A')) for num in decrypted_vector)
    return decrypted_text

def main():
    # Get the key matrix size (2x2 or 3x3)
    n = int(input("Enter the size of the key matrix (2 or 3): "))

    # Get the key matrix from user input
    key_matrix = []
    print(f"Enter the {n}x{n} key matrix (row-wise):")
    for i in range(n):
        row = list(map(int, input().split()))
        key_matrix.append(row)

    key_matrix = np.array(key_matrix)
    
    # Get the plaintext message
    plaintext = input("Enter the plaintext message: ")

    # Encrypt the plaintext
    encrypted_message = hill_cipher_encrypt(plaintext, key_matrix)
    print("Encrypted Message:", encrypted_message)

    # Decrypt the ciphertext
    decrypted_message = hill_cipher_decrypt(encrypted_message, key_matrix)
    print("Decrypted Message:", decrypted_message)

if __name__ == "__main__":
    main()
