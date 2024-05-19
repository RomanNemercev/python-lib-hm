import random

# SHORTEST = 7
# LONGEST = 10
# MIN_ASCII = 33
# MAX_ASCII = 126
#
# def randomPassword():
#     randomLength = randint(SHORTEST, LONGEST)
#     result = ""
#     for i in range(randomLength):
#         result += chr(randint(MIN_ASCII, MAX_ASCII))
#     return result
#
# def main():
#     print("Ваш случайный пароль:", randomPassword())
#
# if __name__ == "__main__":
#     main()

MAX_NUM_NEW = 4
MAX_WORD_NEW = 3
MAX_NUM_OLD = 3
MAX_WORD_OLD = 3
NUM_ASCII = range(48, 58)
WORD_ASCII = range(97, 123)


def randomPlate():
    result = ""
    if random.choice([True, False]):  # 50% вероятность
        # новый формат: 4 цифры и 3 буквы
        for i in range(MAX_NUM_NEW):
            result += chr(random.randint(NUM_ASCII[0], NUM_ASCII[-1]))
        for i in range(MAX_WORD_NEW):
            result += chr(random.randint(WORD_ASCII[0], WORD_ASCII[-1]))
    else:
        # старый формат: 3 цифры и 3 буквы
        for i in range(MAX_NUM_OLD):
            result += chr(random.randint(NUM_ASCII[0], NUM_ASCII[-1]))
        for i in range(MAX_WORD_OLD):
            result += chr(random.randint(WORD_ASCII[0], WORD_ASCII[-1]))

    return result

def main():
    print("Ваш случайный номер:", randomPlate())


if __name__ == "__main__":
    main()
