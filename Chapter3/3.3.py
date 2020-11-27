"""
Измените программу "Отгадай число" таким образом, чтобы у игрока
было ограниченное количество попыток. Если игрок не укладывается в заданное
число (и проигрывает), то программа должна выводить сколь возможно
суровый текст.
"""

import random

# Функция выведет на экран условие игры
def output_condition(max_attempts_number):
    print('Добро пожаловать в игру "Отгадай число"!')
    print(
        f"Я загадал число от 1 до 100. Угадай мое число за {max_attempts_number} попытки."
    )


# Функция с игрой
def game(max_attempts_number):
    my_number = random.randint(1, 100)  # загаданное число
    user_number = -1  # параметр для попытки пользователя
    attempt_number = 0  # номер попытки
    while user_number != my_number and attempt_number < max_attempts_number:
        attempt_number += 1
        print(f"Попытка {attempt_number}. ", end="")
        user_number = int(input("Ваше число: "))
        if user_number < my_number:
            print("Загаданное число больше.")
        elif my_number < user_number:
            print("Загаданное число меньше.")
    if user_number != my_number:
        print("Вы проиграли!")
    else:
        print(f"Вы отгадали число за {attempt_number} попыток.")


# Количество попыток для отгадывания числа определяется случайным образом
max_attempts_number = random.randint(1, 100)
output_condition(max_attempts_number)
#
game(max_attempts_number)
