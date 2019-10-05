def encrypt_caesar(plaintext):
    step = 3
    ciphertext = ""
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
encrypt_caesar(input_text)
decrypt_caesar(input_text)
input("")
#---------------------------
