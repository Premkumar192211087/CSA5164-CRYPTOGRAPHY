def caesar_cipher(text, shift, mode='encrypt'):
    result = ""

    for char in text:
        if char.isalpha():  # Check if character is an alphabet
            shift_base = ord('A') if char.isupper() else ord('a')
            if mode == 'encrypt':
                shifted = (ord(char) - shift_base + shift) % 26 + shift_base
            elif mode == 'decrypt':
                shifted = (ord(char) - shift_base - shift) % 26 + shift_base
            result += chr(shifted)
        else:
            result += char  # Non-alphabet characters are not changed

    return result

# User Input
mode = input("Enter mode (encrypt/decrypt): ").strip().lower()
text = input("Enter the text: ")
shift = int(input("Enter the shift value: "))

# Perform Caesar Cipher
if mode in ['encrypt', 'decrypt']:
    encrypted_text = caesar_cipher(text, shift, mode)
    print(f"Result: {encrypted_text}")
else:
    print("Invalid mode. Please enter 'encrypt' or 'decrypt'.")
