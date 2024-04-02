import random
from Crypto.Util import number

def is_prime(n, k=100):
    """Miller-Rabin primality test."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    # Find r and s such that n - 1 = 2^r * s
    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2

    # Perform Miller-Rabin test k times
    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def generate_large_prime(key_size):
    """Generate a large prime using the Miller-Rabin test."""
    while True:
        prime = number.getPrime(key_size)
        if is_prime(prime):
            return prime

def find_generator(p):
    while True:
        g = random.randint(2, p - 1)
        if pow(g, (p - 1) // 2, p) != 1 and pow(g, p - 1, p) == 1:
            return g

def generate_random_number(max_val):
    while True:
        result = random.randint(2, max_val - 1)
        if result < max_val:
            return result

def main():
    # Get the key size from the user
    key_size = 256  # in bits

    # Generate a large prime number p using the Miller-Rabin primality test
    p = generate_large_prime(key_size)

    # Find a generator g of the finite field GF(p)
    g = find_generator(p)

    # Generate a random number x such that 1 < x < p-1
    x = generate_random_number(p)

    # Compute y = g^x mod p
    y = pow(g, x, p)

    # Private key is x and the public key is (p, g, y)
    print("Private key x =", x)
    print("Public key (p, g, y) =", p, ",", g, ",", y)

    # Get plaintext message M from user
    M_str = input("Enter plaintext message M: ")
    M = int.from_bytes(M_str.encode(), byteorder='big')

    # Encrypt the plaintext message M
    k = generate_random_number(p)
    a = pow(g, k, p)
    b = pow(y, k, p) * M % p
    print("Ciphertext (a, b) =", a, ",", b)

    # Decrypt the ciphertext (a, b)
    decrypted_M = (b * pow(a, -x, p)) % p
    print("Decrypted plaintext M (integer) =", decrypted_M)
    print("Decrypted plaintext M (string) =", decrypted_M.to_bytes((decrypted_M.bit_length() + 7) // 8, byteorder='big').decode())

if __name__ == "__main__":
    main()
