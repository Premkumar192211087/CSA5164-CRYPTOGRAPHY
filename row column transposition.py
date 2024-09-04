def encrypt_message(plaintext, key):
    key = [int(k) for k in key]
    num_columns = len(key)
    num_rows = -(-len(plaintext) // num_columns)  # Ceiling division
    padded_plaintext = plaintext.ljust(num_columns * num_rows, 'X')  # Padding

    grid = [padded_plaintext[i:i + num_columns] for i in range(0, len(padded_plaintext), num_columns)]
    encrypted_text = ''.join([''.join(row[col-1] for row in grid) for col in key])

    return encrypted_text

def decrypt_message(ciphertext, key):
    key = [int(k) for k in key]
    num_columns = len(key)
    num_rows = len(ciphertext) // num_columns

    grid = [''] * num_columns
    k = 0
    for col in key:
        grid[col-1] = ciphertext[k:k + num_rows]
        k += num_rows

    decrypted_text = ''.join([''.join(row) for row in zip(*grid)]).rstrip('X')

    return decrypted_text

def main():
    plaintext = input("Enter the plaintext message: ").replace(" ", "").upper()
    key = input("Enter the numeric key (e.g., 3142): ")

    encrypted_message = encrypt_message(plaintext, key)
    print("Encrypted Message:", encrypted_message)

    decrypted_message = decrypt_message(encrypted_message, key)
    print("Decrypted Message:", decrypted_message)

if __name__ == "__main__":
    main()
