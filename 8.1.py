"""
Доработайте программу "Моя зверюшка" так, чтобы пользователь мог сам
решать, сколько еды скормить зверюшке и сколько времени потратить на
игру с ней ( в зависимости от передаваемых величин зверюшка должна
неодинаково быстро насыщаться и веселеть).
"""

# Класс для объектов-питомцев
class Critter(object):
    """Виртуальный питомец"""

    def __init__(self, name, hunger=0, boredom=0):
        """Конструктор класса"""
        self.__name = name  # имя питомца
        self.__hunger = hunger  # уровень голода питомца
        self.__boredom = boredom  # насколько питомцу скучно

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


# Основная функция
def main():
    """Основная функция для выполнения программы"""
    critter_name = input("Как Вы назовете свою зверюшку? ")
    critter = Critter(critter_name)
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
            # Узнаем о самочувствии
            critter.talk()
        elif choice == "2":
            # Кормим зверюшку
            food = ask_number("Сколько еды скормить зверюшке? ")
            critter.eat(food)
        elif choice == "3":
            # Играем со зверюшкой
            fun_time = ask_number("Сколько времени будете играть? ")
            critter.play(fun_time)
        else:
            print("Я не понял, что Вы хотите выбрать.")


# Запускаем игру
main()
