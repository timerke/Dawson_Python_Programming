"""
А вот задача посложнее. Напишите игру, в которой случайное число
от 1 до 100 загадывает человек, а отгадывает компьютер.
"""

import random

# Функция выведет на экран условие игры
def output_condition(max_attempts_number):
    print('Добро пожаловать в игру "Отгадай число наоборот"!')
    print(
        f"Загадай число от 1 до 100. Я угадаю твое число за {max_attempts_number} попытки."
    )


# Функция с игрой
def game(max_attempts_number):
    user_answer = ""  # параметр для ответа пользователя
    attempt_number = 0  # номер попытки
    min_number = 1
    max_number = 100
    while (
        user_answer != "="
        and attempt_number < max_attempts_number
        and min_number <= max_number
    ):
        attempt_number += 1
        my_number = random.randint(min_number, max_number)
        print(f"Попытка {attempt_number}. Я думаю, что ты загадал число {my_number}.")
        user_answer = input("Твое число больше (>), меньше(<) или я угадал (=): ")
        if user_answer == "<":
            max_number = my_number - 1
        elif user_answer == ">":
            min_number = my_number + 1
    if user_answer != "=" and min_number <= max_number:
        print("Я проиграл!")
    elif user_answer == "=":
        print(f"Я отгадал число за {attempt_number} попыток.")
    else:
        print("Ты жульничаешь!")


# Количество попыток для отгадывания числа определяется случайным образом
max_attempts_number = random.randint(1, 100)
output_condition(max_attempts_number)
#
game(max_attempts_number)
