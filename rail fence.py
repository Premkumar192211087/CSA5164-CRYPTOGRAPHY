def encrypt_rail_fence(plaintext, num_rails):
    rails = [''] * num_rails
    direction = 1  # 1 for moving down, -1 for moving up
    row = 0

    for char in plaintext:
        rails[row] += char
        if row == 0:
            direction = 1
        elif row == num_rails - 1:
            direction = -1
        row += direction

    encrypted_text = ''.join(rails)
    return encrypted_text

def decrypt_rail_fence(ciphertext, num_rails):
    rail_lengths = [0] * num_rails
    direction = 1
    row = 0

    # Determine the length of each rail
    for char in ciphertext:
        rail_lengths[row] += 1
        if row == 0:
            direction = 1
        elif row == num_rails - 1:
            direction = -1
        row += direction

    # Rebuild the rails with the correct characters
    rails = [''] * num_rails
    index = 0
    for i in range(num_rails):
        rails[i] = ciphertext[index:index + rail_lengths[i]]
        index += rail_lengths[i]

    # Read the rails to reconstruct the original message
    decrypted_text = ''
    direction = 1
    row = 0
    rail_positions = [0] * num_rails

    for i in range(len(ciphertext)):
        decrypted_text += rails[row][rail_positions[row]]
        rail_positions[row] += 1
        if row == 0:
            direction = 1
        elif row == num_rails - 1:
            direction = -1
        row += direction

    return decrypted_text

def main():
    plaintext = input("Enter the plaintext message: ").replace(" ", "").upper()
    num_rails = int(input("Enter the number of rails: "))

    encrypted_message = encrypt_rail_fence(plaintext, num_rails)
    print("Encrypted Message:", encrypted_message)

    decrypted_message = decrypt_rail_fence(encrypted_message, num_rails)
    print("Decrypted Message:", decrypted_message)

if __name__ == "__main__":
    main()
