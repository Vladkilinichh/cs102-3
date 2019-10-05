def encrypt_caesar(plaintext):
"""
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
    plaintext = ''
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
    return plaintext
