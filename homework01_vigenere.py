

input_text = input("Enter the text: ") # Тут мы просим пользователя ввести текст, который ему нужно закодировать/раскодировать. Записываем мы это в переменную input_text
def enter_key():
    global input_step
    input_step = input("Enter the key: ")
enter_key()

step = []

for i in input_step:
    if 65 <= ord(i) <= 90:
        step.append(ord(i) - 65)
    elif 97 <= ord(i) <= 122:
        step.append(ord(i) - 97)
    else:
        print("Please enter only letters")
        enter_key()

# Тут мы сдвигаем каждую букву на 3 вправо, т.е. шифруем
def encrypt_caesar(str):
    number = 0
    answer_encoded = ""
    for l in str:
        if 65 <= ord(l) <= 90:
            code_step = ord(l) + step[number]
            if code_step > 90:
                code_step -= 26
            answer_encoded += chr(code_step)
            number += 1
            if number == len(step):
                number = 0
        elif 97 <= ord(l) <= 122:
            code_step = ord(l) + step[number]
            if code_step > 122:
                code_step -= 26
            answer_encoded += chr(code_step)
            number += 1
            if number == len(step):
                number = 0
        else:
            answer_encoded += l
    print("")
    print(f"Encoded message: {answer_encoded}")
    return answer_encoded


# А тут мы сдвигаем каждую букву на 3 влево, т.е. расшифровываем
def decrypt_caesar(str):
    number = 0
    answer_decoded = ""
    for l in str:
        if 65 <= ord(l) <= 90:
            code_step = ord(l) - step[number]
            if code_step < 65:
                code_step += 26
            answer_decoded += chr(code_step)
            number += 1
            if number == len(step):
                number = 0
        elif 97 <= ord(l) <= 122:
            code_step = ord(l) - step[number]
            if code_step < 97:
                code_step += 26
            answer_decoded += chr(code_step)
            number += 1
            if number == len(step):
                number = 0
        else:
            answer_decoded += l
    print("")
    print(f"Decoded message: {answer_decoded}")
    return answer_decoded

encrypt_caesar(input_text)
decrypt_caesar(input_text)


input("")