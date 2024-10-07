def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.

    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ''
    keyword *= len(plaintext) // len(keyword) + 1
    for i in range(len(plaintext)):
        if ord(keyword[i]) >= ord('a') and ord(keyword[i]) <= ord('z'):
            if ord(plaintext[i]) >= ord('a') and ord(plaintext[i]) <= ord('z'):
                ciphertext += str(chr((ord(plaintext[i]) - ord('a') + ord(keyword[i]) - ord('a')) % 26 + ord('a')))
            elif ord(plaintext[i]) >= ord('A') and ord(plaintext[i]) <= ord('Z'):
                ciphertext += str(chr((ord(plaintext[i]) - ord('A') + ord(keyword[i]) - ord('a')) % 26 + ord('A')))
            else:
                ciphertext += plaintext[i]
        else:
            if ord(plaintext[i]) >= ord('a') and ord(plaintext[i]) <= ord('z'):
                ciphertext += str(chr((ord(plaintext[i]) - ord('a') + ord(keyword[i]) - ord('A')) % 26 + ord('a')))
            elif ord(plaintext[i]) >= ord('A') and ord(plaintext[i]) <= ord('Z'):
                ciphertext += str(chr((ord(plaintext[i]) - ord('A') + ord(keyword[i]) - ord('A')) % 26 + ord('A')))
            else:
                ciphertext += plaintext[i]
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.

    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ''
    keyword *= len(ciphertext) // len(keyword) + 1
    for i in range(len(plaintext)):
        if ord(keyword[i]) >= ord('a') and ord(keyword[i]) <= ord('z'):
            if ord(ciphertext[i]) >= ord('a') and ord(ciphertext[i]) <= ord('z'):
                plaintext += str(chr((ord(ciphertext[i]) - ord('a') + ord(keyword[i]) - ord('a')) % 26 + ord('a')))
            elif ord(ciphertext[i]) >= ord('A') and ord(ciphertext[i]) <= ord('Z'):
                plaintext += str(chr((ord(ciphertext[i]) - ord('A') + ord(keyword[i]) - ord('a')) % 26 + ord('A')))
            else:
                plaintext += ciphertext[i]
        else:
            if ord(ciphertext[i]) >= ord('a') and ord(ciphertext[i]) <= ord('z'):
                plaintext += str(chr((ord(ciphertext[i]) - ord('a') + ord(keyword[i]) - ord('A')) % 26 + ord('a')))
            elif ord(ciphertext[i]) >= ord('A') and ord(ciphertext[i]) <= ord('Z'):
                plaintext += str(chr((ord(ciphertext[i]) - ord('A') + ord(keyword[i]) - ord('A')) % 26 + ord('A')))
            else:
                plaintext += ciphertext[i]
    return plaintext
