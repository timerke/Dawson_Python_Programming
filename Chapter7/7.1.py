"""
Доработайте игру "Викторина" таким образом, чтобы у каждого вопроса
появился "номинал" - уникальное количество очков. В конце игры сумма
очков пользователя должна стать равной сумме номиналов вопросов,
на которые он ответил верно.
"""

from sys import exit

# Функция открывает файл
def open_file(file_name, mode):
    """Функция открывает файл и возвращает файловый объект"""
    try:
        file = open(file_name, mode, encoding="utf-8")
    except IOError as e:
        # Если при открытии файла возникло исключение
        print(f"Файл {file_name} не удалось открыть!\n{e}")
        exit()
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
    """Функция приветствует игрока"""
    print("\t\tДобро пожаловать в игру Викторина!")


# Функция реализовывает игру
def game():
    """Функция реализует игру"""
    file = open_file("7.questions.txt", "r")
    welcome()  # выводим приветствие для игрока
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
    print(f"Ваш счет: {score}.")


# Запускаем игру
game()
