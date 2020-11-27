"""Модуль содержит определения классов Card и Deck, которые отвечают за
объекты-карты и колоды."""

import random

# Кортеж из четырех мастей
SUITS = ('Clubs', 'Diamonds', 'Hearts', 'Spades')
# Словарь из достоинств карт
VALUES = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
          '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 1}


class Card:
    """Класс отвечает за объекты-карты."""

    def __init__(self, suit, value, is_open=False):
        """Конструктор класса.
        :param suit, value: масть и достоинство карты;
        :param is_open: True, если карта рубашкой вниз, иначе False."""

        self._suit = suit  # масть карты
        self._value = value  # достоинство карты
        self._is_open = is_open

    def __str__(self):
        """Метод возвращает строку-представление объекта класса Card."""

        if self._is_open:
            return f'Карта: {self._suit}, {self._value};'
        else:
            return f'Карта;'

    def get_value(self):
        """Метод возвращает количество очков карты.
        :return: количество очков."""

        if self._is_open:
            return VALUES[self._value]
        return 0

    def turn_over(self):
        """Метод переворачивает карту."""

        self._is_open = not self._is_open


class Deck:
    """Класс отвечает за карточную колоду."""

    def __init__(self):
        """Конструктор класса."""

        # Создаем список из всех карт
        self._cards = []  # список из всех карт
        self.add_new_deck()

    def __str__(self):
        """Метод возвращает строку-представление объекта класса Deck."""

        deck_string = 'Колода:'
        for i, card in enumerate(self._cards, 1):
            card.turn_over()
            deck_string += f'\n{i}. {card.__str__()}'
        return deck_string

    def add_new_deck(self):
        """Метод добавляет новую перетасованную колоду карт."""

        cards = []  # список карт в новой колоде карт
        for value in VALUES.keys():
            for suit in SUITS:
                cards.append(Card(suit, value))
        # Перемешиваем колоду
        random.shuffle(cards)
        # Добавляем колоду
        self._cards = [*cards, *self._cards]

    def hand_out(self, is_open=False):
        """Метод сдает карту.
        :param is_open: если True, то карта сдается рубашкой вниз.
        :return: объект-карта, лежащая сверху в колоде."""

        card = self._cards.pop()
        if is_open:
            card.turn_over()
        # Если колода становится пустой, добаляем новую
        if len(self._cards) == 0:
            self.add_new_deck()
        return card
