def hex2int(hex_char):
    hex_char = hex_char.upper()  # Приводим символ к верхнему регистру
    valid_hex_chars = "0123456789ABCDEF"

    if hex_char not in valid_hex_chars:
        return "Ошибка: некорректный шестнадцатеричный символ"

    return int(hex_char, 16)


def int2hex(decimal_num):
    if not (0 <= decimal_num <= 15):
        return "Ошибка: число вне диапазона 0-15"

    return hex(decimal_num)[2:].upper()  # Получаем шестнадцатеричное представление и обрезаем '0x'


add_16chr_first = input("Ваш 16-ричный символ: ")
# add_2chr_first = int(input("Ваш 2-х-ричный символ: "))
add_2chr_first = input("Ваш 2-х-ричный символ: ")
add_2chr_first = int(add_2chr_first)


# Примеры использования:
print(hex2int(add_16chr_first))  # Ожидаемый результат: 10
print(hex2int('f'))  # Ожидаемый результат: 15
print(hex2int('G'))  # Ожидаемый результат: Ошибка
# print(int2hex(int(add_2chr_first)))  # Ожидаемый результат: A
print(int2hex(add_2chr_first))  # Ожидаемый результат: A
print(int2hex(15))  # Ожидаемый результат: F
print(int2hex(16))  # Ожидаемый результат: Ошибка
