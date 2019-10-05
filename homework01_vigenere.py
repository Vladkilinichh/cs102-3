def encrypt_vigenere(plaintext, keyword):
    """
    Encrypts plaintext using a Vigenere cipher.
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    input_text = input("Enter the text: ")
    global input_step
    input_step = input("Enter the key: ")

step = []

for i in input_step:
    if 65 <= ord(i) <= 90:
        step.append(ord(i) - 65)
    elif 97 <= ord(i) <= 122:
        step.append(ord(i) - 97)
    else:
        print("Please enter only letters")
        enter_key()


def encrypt_vigenere(plaintext, keyword):
    number = 0
    ciphertext = ""
    for l in str:
        if 65 <= ord(l) <= 90:
            code_step = ord(l) + step[number]
            if code_step > 90:
                code_step -= 26
            ciphertext += chr(code_step)
            number += 1
            if number == len(step):
                number = 0
        elif 97 <= ord(l) <= 122:
            code_step = ord(l) + step[number]
            if code_step > 122:
                code_step -= 26
            ciphertext += chr(code_step)
            number += 1
            if number == len(step):
                number = 0
        else:
            ciphertext += l
    print("")
    print(f"Encoded message: {answer_encoded}")
    return ciphertext


def encrypt_vigenere(plaintext, keyword):
    """
    Decrypts a ciphertext using a Vigenere cipher.
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    number = 0
    plaintext = ""
    for l in str:
        if 65 <= ord(l) <= 90:
            code_step = ord(l) - step[number]
            if code_step < 65:
                code_step += 26
            plaintext += chr(code_step)
            number += 1
            if number == len(step):
                number = 0
        elif 97 <= ord(l) <= 122:
            code_step = ord(l) - step[number]
            if code_step < 97:
                code_step += 26
            plaintext += chr(code_step)
            number += 1
            if number == len(step):
                number = 0
        else:
            plaintext += l
    print("")
    print(f"Decoded message: {answer_decoded}")
    return answer_decoded
