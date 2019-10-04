def encrypt_caesar(plaintext):
 step = 3
 input_text = input("Enter the text: ")
 def encrypt_caesar(str):
    answer_encoded = ""
    for l in str:
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
    print("")
    print(f"Encoded message: {answer_encoded}")
    return answer_encoded

def decrypt_caesar(ciphertext):
def decrypt_caesar(str):
    answer_decoded = ""
    for l in str:
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
    print("")
    print(f"Decoded message: {answer_decoded}")
    return answer_decoded

encrypt_caesar(input_text)
decrypt_caesar(input_text)

input("")
