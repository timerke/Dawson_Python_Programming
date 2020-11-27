"""
Добавьте в игру "Блек-джек" проверку на ошибки. Перед началом очередного раунда
надо проверять, достаточно ли карт в колоде. Если нет, колоду следует вновь
наполнить и перемешать. Найдите в программе и другие уязвимые места, которым
не помешает проверка на ошибки или перехват исключений.

Доработайте проект "Блек-джек" так, чтобы игроки могли делать ставки. Программа
должна следить за капиталом каждого игрока и выводить из-за стола тех, у кого
закончатся деньги.
"""

from essentials import *


class BlackJack:
    """Класс отвечает за логику игры Блек-джек."""

    def __init__(self):
        """Конструктор класса."""

        self._players = []  # список игроков
        self._dealer = Dealer()  # дилер
        # Определяем игроков
        self._define_players()
        self.lap = 1  # раунд игры
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
                if players_number > 0:
                    self.players_number = players_number
                    break
        # Имена и капитал всех игроков
        for i in range(1, self.players_number + 1):
            player = Player()
            player.determine_name_and_capital(i)
            self._players.append(player)

    def _play_in_lap(self):
        """Метод определяет логику игры в раунде.
        :return: True, если в следующем раунде игры могут сыграть игроки,
        иначе False."""

        print(f'Раунд {self.lap}!')
        # Определяем ставки игроков на раунд
        self.bets = []  # список ставок игроков
        players_in_lap = []  # список игроков в раунде
        for player in self._players:
            bet = player.determine_bet()
            if bet:
                self.bets.append(bet)
                players_in_lap.append(player)
        if len(players_in_lap) == 0:
            return False
        # Раздаем по две карты всем игрокам и дилеру
        for player in players_in_lap:
            # Две карты из колоды
            player.cards = [self.deck.hand_out(True), self.deck.hand_out(True)]
            print(player)
        self._dealer.cards = [self.deck.hand_out(True), self.deck.hand_out()]
        print(self._dealer)
        # Опрашиваем игроков, будут ли они брать допкарты
        for player in players_in_lap:
            while player.calculate_sum() < 21 and\
                    player.determine_move() == 'y':
                player.cards.append(self.deck.hand_out(True))
                print(player)
        # Дилер переворачивает все карты и добирает карты
        self._dealer.cards[-1].turn_over()
        print(self._dealer)
        while self._dealer.calculate_sum() < 17:
            self._dealer.cards.append(self.deck.hand_out(True))
            print(self._dealer)
        # Проверяем, кто из игроков проиграл, кто выиграл
        dealer_sum = self._dealer.calculate_sum()
        for i, player in enumerate(players_in_lap):
            player_sum = player.calculate_sum()
            if player_sum > 21 or player_sum < dealer_sum <= 21:
                # Игрок проиграл
                player.change_capital(-self.bets[i])
            elif player_sum == dealer_sum:
                # Никто не выиграл
                player.change_capital(0)
            else:
                # Игрок выиграл
                player.change_capital(self.bets[i])
        print(f'Раунд {self.lap} закончился.')
        # Проверяем количество игроков, которые могут играть
        for player in self._players:
            if player.capital > 0:
                return True
        return False

    def play(self):
        """Метод определяет логику игры."""

        while True:
            if not self._play_in_lap():
                # Игра завершена
                break
            self.lap += 1


class Hand:
    """Класс отвечает за игрока."""

    def __init__(self):
        """Конструктор класса."""

        self.cards = []  # список из карт игрока

    def calculate_sum(self):
        """Метод вычисляет количество очков.
        :return: количество очков у игрока."""

        sum = 0
        is_ace = False  # есть ли среди карт игрока туз
        for card in self.cards:
            if card.get_value() == 1:
                is_ace = True
            sum += card.get_value()
        # Туз приносит 11 очков, если сумма очков не больше 21
        if is_ace and sum + 10 <= 21:
            sum += 10
        return sum


class Dealer(Hand):
    """Класс отвечает за дилера."""

    def __init__(self):
        """Конструктор класса."""

        super().__init__()

    def __str__(self):
        """Метод возвращает строку-представление объекта класса Dealer."""

        string = f'Дилер, карты: '
        for card in self.cards:
            string += card.__str__() + ' '
        string += f'Количество очков: {self.calculate_sum()}'
        return string


class Player(Hand):
    """Класс отвечает за игрока."""

    def __init__(self):
        """Конструктор класса."""

        super().__init__()
        self._name = ''  # имя игрока
        self._capital = 0  # капитал игрока

    def __str__(self):
        """Метод возвращает строку-представление объекта класса Player."""

        string = f'Игрок {self._name}, карты: '
        for card in self.cards:
            string += card.__str__() + ' '
        string += f'Количество очков: {self.calculate_sum()}'
        return string

    @property
    def capital(self):
        """Метод возвращает значение капитала игрока."""

        return self._capital

    @capital.setter
    def capital(self, capital):
        """Метод задает значение капитала игрока.
        :param capital: значение капитала."""

        if capital > 0:
            self._capital = capital
        else:
            self._capital = 0

    def change_capital(self, bet):
        """Метод изменяет капитал игрока."""

        self._capital += bet
        if bet > 0:
            print(f'Игрок {self._name} выиграл, его капитал {self._capital}.')
        elif bet < 0:
            print(f'Игрок {self._name} проиграл, его капитал {self._capital}.')
        else:
            print(f'Игрок {self._name} вернул свою ставку.')

    def determine_bet(self):
        """Метод определяет, какую ставку сделает игрок.
        :return: ставка игрока."""

        if self._capital <= 0:
            return 0
        while True:
            print(f'{self._name}, какую сделаете ставку? ')
            response = input('Ваш ответ: ')
            try:
                bet = int(response)
                if 0 <= bet <= self._capital:
                    return bet
            except Exception:
                pass

    def determine_move(self):
        """Метод определяет, будет ли игрок брать карту.
        :return: 'y', если игрок берет допкарту, иначе 'n'."""

        while True:
            print(f'{self._name}, сдать еще карту?')
            response = input('Ваш ответ (yes/no): ')
            if response.lower() in ('y', 'ye', 'yes', 'no', 'n'):
                if response.lower() in ('y', 'ye', 'yes'):
                    return 'y'
                return 'n'

    def determine_name_and_capital(self, number):
        """Метод определяет имя и капитал игрока.
        :param number: номер игрока."""

        while True:
            name = input(f'Имя игрока под номером {number}: ')
            if name:
                self._name = name
                break
        while True:
            response = input(f'Капитал игрока под номером {number}: ')
            try:
                capital = int(response)
            except Exception:
                pass
            else:
                if capital > 0:
                    self._capital = capital
                    break


if __name__ == '__main__':
    game = BlackJack()
    game.play()
