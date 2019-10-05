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
 step = 3
    answer_encoded = ""
    for l in plaintext:
        if 65 <= ord(l) <= 90:
            code_step = ord(l) + step
            if code_step > 90:
                code_step -= 26
            answer_encoded += chr(code_step)
        elif 97 <= ord(l) <= 122:
            code_step = ord(l) + step
            if code_step > 122:
                code_step -= 26
            answer_encoded += chr(code_step)
        else:
            answer_encoded += l
    return answer_encoded

def decrypt_caesar(ciphertext):
    answer_decoded = ""
    for l in ciphertext:
        if 65 <= ord(l) <= 90:
            code_step = ord(l) - step
            if code_step < 65:
                code_step += 26
            answer_decoded += chr(code_step)
        elif 97 <= ord(l) <= 122:
            code_step = ord(l) - step
            if code_step < 65:
                code_step += 26
            answer_decoded += chr(code_step)
        else:
            answer_decoded += l
    return answer_decoded
