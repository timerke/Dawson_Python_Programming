"""
Создайте программу, имитирующу телевизор как объект. У пользователя
должна быть возможность вводить номер канала, а также увеличить и
уменьшить громкость. Программа должна следить за тем, чтобы номер
канала и уровень громкости оставались в допустимых пределах.
"""

# Класс для объектов, симулирующих телевизор
class TV(object):
    """Класс симулирует работу телевизора"""

    # Атрибуты класса - общие для всех телевизоров
    __min_channel = 1  # наименьший канал
    __max_channel = 100  # наибольший канал
    __min_volume = 0  # наименьший звук
    __max_volume = 50  # наибольший звук

    def __init__(self, channel=1, volume=0):
        """Конструктор"""
        if TV.__min_channel <= channel <= TV.__max_channel:
            # Если номер канала лежит в допустимом диапазоне
            self.__channel = channel
        else:
            self.__channel = TV.__min_channel
        if TV.__min_volume <= volume <= TV.__max_volume:
            # Если звук лежит в допустимом диапазоне
            self.__volume = volume
        else:
            self.__volume = TV.__min_volume

    def __str__(self):
        """Метод для вывода полной информации об объекте класса TV"""
        return f"Объект TV; канал - {self.channel}; звук - {self.volume}"

    @property
    def channel(self):
        """Свойство для канала"""
        return self.__channel

    @channel.setter
    def channel(self, user_channel):
        """Сеттер для канала"""
        if TV.__min_channel <= user_channel <= TV.__max_channel:
            # Если номер канала, на который нужно переключиться, лежит в допустимом диапазоне
            self.__channel = user_channel

    def down(self):
        """Метод понижает звук"""
        if TV.__min_volume <= self.__volume - 1:
            self.__volume -= 1

    def up(self):
        """Метод повышает звук"""
        if self.__volume + 1 <= TV.__max_volume:
            self.__volume += 1

    @property
    def volume(self):
        """Свойство для звука"""
        return self.__volume


# Создаем объект телевизор
tv = TV(465, 34)
print(tv)
# Меняем канал слишком сильно
tv.channel = 506
print(f"Канал = {tv.channel}")
# Меняем канал нормально
tv.channel = 56
print(f"Канал = {tv.channel}")
# Увеличиваем звук
for _ in range(23):
    tv.up()
print(f"Звук = {tv.volume}")
# Уменьшаем звук
for _ in range(13):
    tv.down()
print(f"Звук = {tv.volume}")
print(tv)
