"""
Доработайте игру "Отгадай число" из главы 3 так, чтобы в ней нашла
применение функция ask_number().
"""

import random

# Функция выведет на экран условие игры
def output_condition(max_attempts_number):
    """Функция выводит на экран условие игры"""
    print('Добро пожаловать в игру "Отгадай число"!')
    print(
        f"Я загадал число от 1 до 100. Угадай мое число за {max_attempts_number} попытки."
    )


# Функция просит пользователя ввести число
def ask_number(question, low, high, multiplicity=1):
    """Функция просит ввести число из диапазона"""
    response = None
    while response not in range(low, high, multiplicity):
        response = int(input(question))
    return response


# Функция с игрой
def game(max_attempts_number):
    """Функция с игрой"""
    my_number = random.randint(1, 100)  # загаданное число
    user_number = -1  # параметр для попытки пользователя
    attempt_number = 0  # номер попытки
    while user_number != my_number and attempt_number < max_attempts_number:
        attempt_number += 1
        question = f"Попытка {attempt_number}. Ваше число: "
        user_number = ask_number(question, 1, 100)
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
