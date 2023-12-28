# -----------------------------------------------------------------------
# FA 23 CMPSC 360 Extra Credit Assignment
# RSA Implementation
# 
# Name: Siddharth Shah
# ID: 916270083
# 
# 
# You cannot use any external/built-in libraries to help compute gcd
# or modular inverse. You cannot use RSA, cryptography, or similar libs
# for this assignment.
# 
# -----------------------------------------------------------------------

from typing import Tuple


def is_prime(n: int) -> bool:
    """
    Checks if the input is a valid prime number.

    Args:
        n (int): The input number.

    Returns:
        bool: True if the input is prime, False otherwise.
    """
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def generate_key_pair(p: int, q: int) -> Tuple[Tuple[int, int], Tuple[int, int]]:
    """
    Generates the public and private key pair if p and q are distinct primes.
    Otherwise, raises a ValueError.

    Args:
        p (int): The first prime number.
        q (int): The second prime number.

    Returns:
        Tuple[Tuple[int, int], Tuple[int, int]]: The public and private key pair.
    """
    if not (is_prime(p) and is_prime(q)):
        raise ValueError("Both numbers must be prime.")

    n = p * q
    phi = (p - 1) * (q - 1)
    e = generate_public_exponent(phi)
    d = modular_inverse(e, phi)

    public_key = (n, e)
    private_key = (n, d)

    return public_key, private_key


def generate_public_exponent(phi: int) -> int:
    """
    Generates the smallest public exponent for a given phi value.

    Args:
        phi (int): The Euler's totient function.

    Returns:
        int: The public exponent.
    """
    for e in range(2, phi):
        if gcd(e, phi) == 1:
            return e
    return None


def gcd(x: int, y: int) -> int:
    """
    Calculates the greatest common divisor of two integers.

    Args:
        x (int): The first integer.
        y (int): The second integer.

    Returns:
        int: The greatest common divisor.
    """
    while y != 0:
        x, y = y, x % y
    return x


def modular_inverse(a: int, n: int) -> int:
    """
    Calculates the modular inverse of a with respect to n.

    Args:
        a (int): The integer.
        n (int): The modulus.

    Returns:
        int: The modular inverse.
    """
    t, new_t = 0, 1
    r, new_r = n, a

    while new_r != 0:
        quotient = r // new_r
        t, new_t = new_t, t - quotient * new_t
        r, new_r = new_r, r - quotient * new_r

    if r > 1:
        raise ValueError("a is not invertible")
    if t < 0:
        t += n

    return t


def mod_exp(base: int, exp: int, mod: int) -> int:
    """
    Calculates the modular exponentiation of base^exp mod mod.

    Args:
        base (int): The base.
        exp (int): The exponent.
        mod (int): The modulus.

    Returns:
        int: The result of modular exponentiation.
    """
    result = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        exp = exp // 2
        base = (base * base) % mod
    return result


def rsa_encrypt(message: int, public_key: Tuple[int, int]) -> int:
    """
    Encrypts the message with the given public key using the RSA algorithm.

    Args:
        message (int): The message to encrypt.
        public_key (Tuple[int, int]): The public key.

    Returns:
        int: The encrypted ciphertext.
    """
    n, e = public_key
    return mod_exp(message, e, n)

def rsa_decrypt(ciphertext: int, private_key: Tuple[int, int]) -> int:
    """
    Decrypts the ciphertext using the private key according to the RSA algorithm.

    Args:
        ciphertext (int): The encrypted ciphertext.
        private_key (Tuple[int, int]): The private key.

    Returns:
        int: The decrypted message, an integer.
    """
    n, d = private_key
    return mod_exp(ciphertext, d, n)


if __name__ == "__main__":
    # Example usage:
    p = 61
    q = 53
    public_key, private_key = generate_key_pair(p, q)
    message = 42
    ciphertext = rsa_encrypt(message, public_key)
    decrypted_message = rsa_decrypt(ciphertext, private_key)

    print(f"Original Message: {message}")
    print(f"Ciphertext: {ciphertext}")
    print(f"Decrypted Message: {decrypted_message}")
