"""
Доработайте игру "Анаграммы" так, чтобы к каждому слову полагалась
подсказка. Игрок должен получать право на подсказку в том случае, если
у него нет никаких предположений. Разработайте систему начисления
очков, по которой бы игроки, отгадавшие слово без подсказки, получали
больше тех, кто запросил подсказку.
"""

import random

# Функция создает анаграмму
def jumble(word):
    jumble_word = ""
    while word:
        # Положение символа, который добавится в анаграмму
        pos = random.randrange(len(word))
        # К анаграмме добавляем букву из загаданного слова
        jumble_word += word[pos]
        # Из загаданного слова удаляем букву
        word = word[:pos] + word[pos + 1:]
    return jumble_word


# Функция выводит подсказку
def help(word, help_number):
    if help_number + 1 <= len(word):
        help_number += 1
        print(f"Слово начинается так: {word[:help_number]}")
    else:
        print("У вас больше нет подсказок!")
    return help_number


# Кортеж из слов, которые могут быть использованы в игре
WORDS = ("математика", "анаграмма", "гиппопотам", "рождение")
# Выбираем случайным образом слово, которое будет в игре
correct_word = random.choice(WORDS)
# Создаем анаграмму загаданного слова
jumble_word = jumble(correct_word)
print(f"Отгадайте слово из его анаграммы: {jumble_word}")

user_guess = ""  # попытки пользователя отгадать слово
help_number = 0  # количество подсказок, которыми воспользовался пользователь
while user_guess != correct_word:  # игра продолжается, пока слово не угадано
    user_guess = input("Ваш вариант (ENTER - закончить, ? - подсказка): ")
    if user_guess == "" or help_number == len(correct_word):
        # Если пользователь ввел ENTER или с помощью подсказок выведено все слово,
        # игра прекращается
        break
    elif user_guess == "?":
        # Если пользователь просит подсказку
        help_number = help(correct_word, help_number)
else:
    # Если пользователь отгадал слово
    print(
        f"Вы угадали слово и заработали {len(correct_word)-help_number} баллов")
