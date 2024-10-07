import typing as tp


def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.

    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ''
    for i in range(len(plaintext)):
        if ord(plaintext[i]) >= ord('a') and ord(plaintext[i]) <= ord('z'):
            ciphertext += str(chr((ord(plaintext[i]) - ord('a') + shift) % 26 + ord('a')))
        elif ord(plaintext[i]) >= ord('A') and ord(plaintext[i]) <= ord('Z'):
            ciphertext += str(chr((ord(plaintext[i]) - ord('A') + shift) % 26 + ord('A')))
        else:
            ciphertext += plaintext[i]
    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.

    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    # PUT YOUR CODE HERE
    plaintext = ''
    for i in range(len(ciphertext)):
        if ord(ciphertext[i]) >= ord('a') and ord(ciphertext[i]) <= ord('z'):
            plaintext += str(chr((ord(ciphertext[i]) - ord('a') - shift) % 26 + ord('a')))
        elif ord(ciphertext[i]) >= ord('A') and ord(ciphertext[i]) <= ord('Z'):
            plaintext += str(chr((ord(ciphertext[i]) - ord('A') - shift) % 26 + ord('A')))
        else:
            plaintext += plaintext[i]
    return plaintext


def caesar_breaker_brute_force(ciphertext: str, dictionary: tp.Set[str]) -> int:
    """
    Brute force breaking a Caesar cipher.
    """
    best_shift = 0
    # PUT YOUR CODE HERE

    return best_shift
