# ElGamal
# ElGamal Encryption Program

This is a Python implementation of the ElGamal encryption scheme. ElGamal is a public-key cryptosystem that uses asymmetric key encryption for secure communication.

## Assignment Details

This implementation of the ElGamal encryption scheme is developed as part of Assignment 03 for the course "Practical Aspects of Modern Cryptography" (CIS5371/CIS 4634) by Mehrdad Nojoumian.

### Assignment Instructions
For this assignment, the task was to implement the ElGamal Public-Key Encryption scheme using any programming language of choice. The recommendation was to use C/C++ or Java, but this implementation is done in Python. The implementation was carried out individually, but students had the option to work in pairs or with team members from previous assignments.

#### Assignment Requirements:
- The program should prompt the user to enter the desired key size in terms of the number of bits.
- Based on the specified key size, the program should use the Fermat or Miller-Rabin primality test algorithm to generate a large prime number.
- The program should utilize existing programming packages to find a generator of the finite field.
- It should initialize a pair of keys, i.e., private and public keys.
- For computations, the Square-and-Multiply algorithm should be used.
- The program should allow the user to input plaintext for encryption and perform encryption (generating the ciphertext from the plaintext) and decryption (generating the original plaintext from the ciphertext).

## Requirements

- Python 3.x
- pycryptodome library (for generating large primes)

You can install pycryptodome via pip:


## Usage

1. Clone this repository or download the Python script (main.py) to your local machine.

2. Run the Python script using the following command:


3. Follow the instructions provided by the program:
   - Enter the desired key size in bits.
   - Enter the plaintext message (`M`) that you want to encrypt. The message can be any string.
   - The program will then generate the public and private keys (`p`, `g`, `y`, `x`).
   - After encryption, the ciphertext `(a, b)` will be displayed.
   - The program will decrypt the ciphertext and display the decrypted plaintext message.

## Notes

- The key size used in this implementation can go up to 2056 bits
- The program uses the Miller-Rabin primality test to generate large prime numbers for the encryption scheme.
- Make sure to keep your private key (`x`) secure and do not share it with anyone.
  

