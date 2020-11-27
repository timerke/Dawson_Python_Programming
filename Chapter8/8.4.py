"""
Напишите программу "Зооферма", в которой будет создано несколько
объектов класса Critter, а манипулировать ими всеми можно будет с
помощью списка. Теперь пользователь должен заботиться не об одной
зверюшке, а обо всех обитателях зоофермы. Выбирая пункт в меню,
пользователь выбирает действие, которое хотел бы выполнить со всеми
зверюшками: покормить их, поиграть с ними или узнать об их самочувствии.
Чтобы программа была интереснее, при создании каждой зверюшки следует
назначать ей случайно выбранные уровни голода и уныния.
"""

import random

# Класс для объектов-питомцев
class Critter(object):
    """Виртуальный питомец"""

    def __init__(self, name, hunger=0, boredom=0):
        """Конструктор класса"""
        self.__name = name  # имя питомца
        self.__hunger = hunger  # уровень голода питомца
        self.__boredom = boredom  # насколько питомцу скучно

    def __str__(self):
        """Метод для вывода информации об объекте класса Critter"""
        return f"Питомца зовут {self.__name}; голод - {self.__hunger}; уныние - {self.__boredom}; настроение - {self.mood}"

    def __pass_time(self):
        """Метод определяет, что со временем голод и уныние питомца повышаются"""
        self.__hunger += 1
        self.__boredom += 1

    @property
    def mood(self):
        """Свойство определяет настроение питомца"""
        unhappiness = self.__hunger + self.__boredom
        if unhappiness < 5:
            m = "прекрасно"
        elif 5 <= unhappiness <= 10:
            m = "неплохо"
        elif 11 <= unhappiness <= 15:
            m = "не сказать чтобы хорошо"
        else:
            m = "ужасно"
        return m

    def talk(self):
        """Метод узнает настроение и имя питомца"""
        print(f"Меня зовут {self.__name}, и я чувствую себя {self.mood}.")
        self.__pass_time()

    def eat(self, food=4):
        """Метод уменьшает голод питомца"""
        print("Мррр... Спасибо!")
        self.__hunger -= food
        if self.__hunger < 0:
            self.__hunger = 0
        self.__pass_time()

    def play(self, fun_time=4):
        """Метод снижает уровень уныния"""
        print("Уиии!")
        self.__boredom -= fun_time
        if self.__boredom < 0:
            self.__boredom = 0
        self.__pass_time()


# Функция заправивает у пользователя числовые значения
def ask_number(question):
    """Функция запрашивает у пользователя числовое значение"""
    number = None
    while not number:
        try:
            number = int(input(question))
        except:
            # При ошибке ввода ничего не происходит, просто цикл повторяется
            number = None
    return number


# Функция создает ферму из питомцев
def create_pets():
    # Кортеж из имен, которые можно дать питомцам
    names = ["Машка", "Петька", "Рекс", "Белый клык", "Бобик", "Мурка", "Телка"]
    N = len(names)  # максимально возможное количество питомцев
    # Случайным образом определяем количество питомцев на ферме
    n = random.randint(1, N)
    # Случайным образом выбираем имена для питомцев, а также их голод и уныние
    pets = list(range(n))  # список для питомцев
    for i in range(n):
        # Выбираем имя из списка возможных имен
        name_i = random.randint(1, len(names)) - 1
        pet_name = names[name_i]
        names = (
            names[:name_i] + names[name_i + 1 :]
        )  # удаляем выбранное имя из списка возможных имен
        # Выбираем случайным образом голод и уныние питомца
        hunger = random.randint(0, 10)
        boredom = random.randint(0, 10)
        # Создаем питомца
        pets[i] = Critter(pet_name, hunger, boredom)
    print(f"У Вас на ферме {n} питомцев.")
    return pets


# Основная функция
def main():
    """Основная функция для выполнения программы"""
    # Создаем ферму из питомцев
    pets = create_pets()
    # Взаимодействие пользователя с питомцем
    choice = None
    while choice != "0":
        print(
            """
        Зверюшка:
        0 - Выйти
        1 - Узнать о самочувствии зверюшки
        2 - Покормить зверюшку
        3 - Поиграть со зверюшкой
        """
        )
        choice = input("Ваш выбор: ")
        if choice == "0":
            # Выход из программы
            print("До свидания.")
        elif choice == "1":
            # Узнаем о самочувствии каждого питомца
            for pet in pets:
                pet.talk()
        elif choice == "2":
            # Кормим всех питомцев
            food = ask_number("Сколько еды скормить зверюшке? ")
            for pet in pets:
                pet.eat(food)
        elif choice == "3":
            # Играем с каждой зверюшкой
            fun_time = ask_number("Сколько времени будете играть? ")
            for pet in pets:
                pet.play(fun_time)
        elif choice == "$":
            # Выбран секретный пункт меню, нужно показать полную информацию о питомце
            for pet in pets:
                print(pet)
        else:
            print("Я не понял, что Вы хотите выбрать.")


# Запускаем игру
main()
