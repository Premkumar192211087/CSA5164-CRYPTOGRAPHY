from sympy import mod_inverse

def find_rsa_private_key(e, n):
    p = q = None
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            p = i
            q = n // i
            break
    
    phi_n = (p - 1) * (q - 1)
    d = mod_inverse(e, phi_n)
    
    return d

# User input
e = int(input("Enter public exponent (e): "))
n = int(input("Enter modulus (n): "))
private_key = find_rsa_private_key(e, n)
print(f"Private Key (d): {private_key}")
