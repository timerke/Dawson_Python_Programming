"""
Реализуйте ту же самую функциональность, что и в предыдущей задаче,
иным способом: на этот раз сохраните список рекордов в обычном
текстовом файле.
"""

import pickle
import sys

# Функция открывает файл
def open_file(file_name, mode):
    """Функция открывает файл и возвращает файловый объект"""
    try:
        file = open(file_name, mode, encoding="utf-8")
    except IOError as e:
        # Если при открытии файла возникло исключение
        print(f"Файл {file_name} не удалось открыть!\n{e}")
        sys.exit()
    else:
        return file


# Функция читает вопрос из файла
def read_question(file):
    """Функция читает вопрос из файла"""
    category = file.readline()  # категория вопроса
    question = file.readline()  # вопрос
    answers = [file.readline() for i in range(4)]  # варианты ответов
    right_answer = file.readline()  # номер правильного ответа
    if right_answer:
        right_answer = right_answer[0]
    try:
        nominal = int(file.readline())  # номинал вопроса
    except:
        nominal = 0
    explanation = file.readline()  # объяснение правильного ответа на вопрос
    return category, question, answers, right_answer, nominal, explanation


# Функция приветствует игрока
def welcome():
    """Функция приветствует игрока и возвращает его имя"""
    print("\t\tДобро пожаловать в игру Викторина!")
    gamer = input("Как Вас зовут? ")
    print()
    return gamer


# Функция читает файл с рекордами
def read_achievements(file_name):
    """Функция читает файл с рекордами и возвращает список рекордов"""
    try:
        file = open(file_name, "r", encoding="utf-8")
    except IOError:
        return None
    else:
        # Читаем из файла, пока в файле есть объекты для считывания
        achievements = []
        gamer = file.readline()[:-1]
        score = int(file.readline()[:-1])
        while gamer:
            achievements.append({"gamer": gamer, "score": score})
            gamer = file.readline()[:-1]
            score = file.readline()
            if score:
                score = int(score[:-1])
        file.close()
        return achievements


# Функция записывает рекорды в файл
def write_achievements(file_name, achievements):
    """Функция записывает рекорды в файл"""
    file = open(file_name, "w", encoding="utf-8")
    for achievement in achievements:
        gamer = achievement["gamer"] + "\n"
        score = str(achievement["score"]) + "\n"
        file.writelines((gamer, score))
    file.close()


# Функция выводит на экран список рекордов викторины
def display_achievements(achievements):
    """Функция выводит на экран список рекордов викторины"""
    print("\t\tРекорды")
    i = 1
    for achievement in achievements:
        score = achievement["score"]
        gamer = achievement["gamer"]
        print(f"{i}. {gamer} - {score}")
        i += 1


# Функция работает с рекордами викторины в конце игры
def work_achievements(gamer, score):
    """Функция работает с рекордами викторины в конце игры"""
    # Сначала считываются все сохраненные рекорды
    achievements = read_achievements("7.achievements.txt")
    if not achievements:
        achievements = []
    # Добавляем в список рекордов новую запись и сортируем по убыванию очков
    achievements.append({"gamer": gamer, "score": score})
    achievements.sort(key=lambda a: a["score"], reverse=True)
    # Выводим на экран список рекордов
    display_achievements(achievements)
    # Сохраняем 3 лучших рекордов
    if 3 < len(achievements):
        achievements = achievements[:3]
    write_achievements("7.achievements.txt", achievements)


# Функция реализовывает игру
def game():
    """Функция реализует игру"""
    file = open_file("7.questions.txt", "r")
    gamer = welcome()  # выводим приветствие для игрока
    score = 0  # количество очков игрока
    # Извлекаем вопросы и получаем ответы
    category, question, answers, right_answer, nominal, explanation = read_question(
        file
    )
    while category:
        # Выводим вопрос
        print(category.upper(), end="")
        print(question, end="")
        for i in range(4):
            print(f"\t{i+1}. {answers[i]}", end="")
        # Получаем ответ
        answer = input("Ваш ответ: ")
        if answer == right_answer:
            print("Да!", end=" ")
            score += nominal
        else:
            print("Нет!", end=" ")
        print(f"{explanation}Счет: {score}.\n")
        # Читаем следующий вопрос
        category, question, answers, right_answer, nominal, explanation = read_question(
            file
        )
    # Завершение игры
    file.close()
    print("Это был последний вопрос!")
    print(f"Ваш счет: {score}.\n")
    # Работа с рекордами игры
    work_achievements(gamer, score)


# Запускаем игру
game()
