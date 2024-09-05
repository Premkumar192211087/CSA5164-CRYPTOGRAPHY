def common_factor_attack(n, known_plaintext):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            p = i
            q = n // i
            return p, q
    return None

# User input
n = int(input("Enter modulus (n): "))
known_plaintext = int(input("Enter known plaintext block: "))
factors = common_factor_attack(n, known_plaintext)
if factors:
    print(f"Factors of n: {factors}")
else:
    print("No factors found.")
