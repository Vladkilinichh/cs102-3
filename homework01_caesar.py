ddef encrypt_caesar(plaintext):
    """
    Encrypts plaintext using a Vigenere cipher.
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    step = 3
    for l in plaintext:
        if 65 <= ord(l) <= 90:
            code_step = ord(l) + step
            if code_step > 90:
                code_step -= 26
            ciphertext += chr(code_step)
        elif 97 <= ord(l) <= 122:
            code_step = ord(l) + step
            if code_step > 122:
                code_step -= 26
            ciphertext += chr(code_step)
        else:
            ciphertext += l
    print("")
    print(f"Encoded message: {ciphertext}")
    return ciphertext


def decrypt_caesar(ciphertext):
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
    step = 3
    plaintext = ""
    for l in ciphertext:
        if 65 <= ord(l) <= 90:
            code_step = ord(l) - step
            if code_step < 65:
                code_step += 26
            plaintext += chr(code_step)
        elif 97 <= ord(l) <= 122:
            code_step = ord(l) - step
            if code_step < 65:
                code_step += 26
            plaintext += chr(code_step)
        else:
            plaintext += l
    print("")
    print(f"Decoded message: {plaintext}")
    return plaintext

# ---- ДЛЯ ТЕСТИРОВАНИЯ ----
input_text = input('Enter the text: ')

input("")
