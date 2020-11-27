"""
Напишите однокарточную версию игры "Война", структура раунда в которой такова:
все игроки тянут по одной карте, а выигрывает тот, у кого номинал карты
оказывается наибольшим.
"""

from essentials import *


class Player:
    """Класс отвечает за игрока."""

    def __init__(self):
        """Конструктор класса."""

        self.card = None  # карт игрока

    def __str__(self):
        """Метод возвращает строку-представление объекта класса Player."""

        string = f'Игрок {self._name}, карта: {self.card.__str__()}'
        return string

    def determine_name(self, number):
        """Метод определяет имя и игрока.
        :param number: номер игрока."""

        while True:
            name = input(f'Имя игрока под номером {number}: ')
            if name:
                self._name = name
                return

    def get_value(self):
        """Метод возвращает количество очков игрока.
        :return: количество очков у игрока."""

        return self.card.get_value()


class War:
    """Класс отвечает за логику игры "Война"."""

    def __init__(self):
        """Конструктор класса."""

        self._players = []  # список игроков
        # Определяем игроков
        self._define_players()
        self.deck = Deck()  # берем колоду и перетасовываем ее

    def _define_players(self):
        """Метод определяет параметры игроков."""

        # Сколько игроков
        while True:
            print('Сколько игроков?')
            response = input('Ваш ответ: ')
            try:
                players_number = int(response)
            except Exception:
                pass
            else:
                if 0 < players_number <= 52:
                    self.players_number = players_number
                    break
        # Имена всех игроков
        for i in range(1, self.players_number + 1):
            player = Player()
            player.determine_name(i)
            self._players.append(player)

    def play(self):
        """Метод определяет логику игры."""

        # Раздаем по карте каждому игроку
        for player in self._players:
            player.card = self.deck.hand_out(True)
            print(player)
        # Сортируем список игроков по количеству очков
        self._players = sorted(self._players,
                               key=lambda player: player.get_value(),
                               reverse=True)
        # Определяем победителей
        print('Победители:')
        for player in self._players:
            if player.get_value() == self._players[0].get_value():
                print(player)


if __name__ == '__main__':
    game = War()
    game.play()
