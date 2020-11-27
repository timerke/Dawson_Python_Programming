"""
Игра крестики-нолики.
Напишите такую функцию computer_move(), которая сделала бы стратегию
компьютера безупречной. Проверьте, можно ли создать непобедимого противника.
"""

from random import choice

# Глобальные переменные
X = "X"  # ход крестиком
O = "O"  # ход ноликом
EMPTY = " "  # пустая клеточка
TIE = "Ничья"
SQUARES_NUMBER = 9  # количество клеточек

# Функция выводит условие игры
def display_instruction():
    """Функция выводит условие игры"""
    print(
        """
        Давай сыграем в крестики-нолики!
        Чтобы сделать свой ход, Вам нужно будет выбрать номер клетки на игровом поле:
         0 | 1 | 2
        -----------
         3 | 4 | 5
        -----------
         6 | 7 | 8
        """
    )


# Функция запрашивает у пользователя число
def ask_number(question, low, high):
    """Функция запрашивает у пользователя число в диапазоне от low до high
    и возвращает это число"""
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response


# Функция определяет, кто будет ходить первым
def who_is_first():
    """Функция случайным образом определяет, кто будет ходить первым.
    Функция возвращает значки (крестики и нолики), которыми будут
    ходить пользователь и компьютер"""
    # Случайным образом выбирается пользователь или компьютер
    first = choice(("computer", "user"))
    if first == "user":
        # Если первым будет ходить пользователь
        user = X  # кто ходит первым, рисует крестики
        computer = O  # кто ходит вторым, рисует нолики
        print("По результатам жеребьевки Вы ходите первым! (У Вас крестики Х)")
    else:
        user = O  # кто ходит вторым, рисует нолики
        computer = X  # кто ходит первым, рисует крестики
        print("По результатам жеребьевки Вы ходите вторым! (У Вас нолики О)")
    return user, computer


# Функция создает новое игровое поле
def new_board():
    """Функция создает новое пустое игровое поле и возвращает его"""
    board = [EMPTY for _ in range(SQUARES_NUMBER)]
    return board


# Функция выводит на экран игровое поле
def display_board(board):
    """Функция выводит на экран игровое поле"""
    print(f"\t {board[0]} | {board[1]} | {board[2]}")
    print("\t-----------")
    print(f"\t {board[3]} | {board[4]} | {board[5]}")
    print("\t-----------")
    print(f"\t {board[6]} | {board[7]} | {board[8]}")


# Функция определяет пустые клетки на игровом поле
def empty_cells(board):
    """Функция определяет пустые клетки на игровом поле и
    возвращает их"""
    cells = []  # список с пустыми клетками
    for i in range(SQUARES_NUMBER):
        if board[i] == EMPTY:
            cells.append(i)
    return cells


# Функция определяет победителя
def who_is_winner(board, user, computer):
    """Функция определяет победителя игры"""
    # Выигрышные позиции на игровом поле
    WAYS_TO_WIN = (
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6),
    )
    # Проверяем возможного победителя
    for way in WAYS_TO_WIN:
        line = tuple([board[i] for i in way])
        if line == (computer, computer, computer):
            # Если победил компьютер
            return computer
        elif line == (user, user, user):
            # Если победил пользователь
            return user
    # Если нет победителя, может, ничья?
    if EMPTY not in board:
        # На игровом поле нет пустых клеток, потому ничья
        return TIE
    # Игра не завершена
    return None


# Функция определяет ход пользователя
def user_move(board):
    """Функция определяет ход пользователя и возвращает его"""
    # Запрашиваем у пользователя его ход
    move = None
    while move not in empty_cells(board):
        move = ask_number("Введите номер клетки от 0 до 8: ", 0, SQUARES_NUMBER)
    return move


# Функция определяет ход компьютера
def computer_move(board, user, computer):
    """Функция определяет ход компьютера и возвращает его"""
    board = board[:]  # копируем игровое поле
    # Позиции от лучшего к худшему
    BEST_MOVES = (4, 0, 2, 6, 8, 1, 3, 5, 7)
    print("Я выберу клетку с номером ", end="")
    # Проверяем, есть ли выигрышный ход для компьютера
    for move in empty_cells(board):
        board[move] = computer
        if who_is_winner(board, user, computer) == computer:
            print(move)
            return move
        board[move] = EMPTY
    # Проверяем, есть ли проигрышный ход для компьютера
    for move in empty_cells(board):
        board[move] = user
        if who_is_winner(board, user, computer) == user:
            print(move)
            return move
        board[move] = EMPTY
    # Если нет ни выигрышного, ни проигрышного хода
    for move in BEST_MOVES:
        if move in empty_cells(board):
            print(move)
            return move


# Функция определяет, кто ходит следующим
def next_turn(turn):
    """Функция определяет, кто ходит следующим, и возвращает значок того,
    кто ходит следующим (крестик или нолик)"""
    turn = X if turn == O else O
    return turn


# Функция подволит итоги игры
def sum_up(winner, user, computer):
    """Функция подводит итоги игры"""
    if winner == computer:
        # Если победил компьютер
        print("Ура! Я победил!")
    elif winner == user:
        # Если победил пользователь
        print("Вы победили!")
    else:
        # Если ничья
        print("Ничья!")


# Основная функция игры крестики-нолики
def main():
    """Основная функция игры крестики-нолики"""
    # Выводим условие игры
    display_instruction()
    # Определяем, за кем первый ход в игре
    user, computer = who_is_first()
    # Первым ходит тот, у кого крестики
    turn = X
    # Создаем пустое игровое поле
    board = new_board()
    # Игра продолжается, пока не будет победителя или ничьей
    winner = None
    while not winner:
        print(winner)
        if user == turn:
            # Если ходит пользователь
            move = user_move(board)
        else:
            # Если ходит компьютер
            move = computer_move(board, user, computer)
        board[move] = turn
        display_board(board)  # выводим на экран новое поле
        winner = who_is_winner(board, user, computer)  # проверяем победителя
        turn = next_turn(turn)  # переход хода
    # Подводим итоги игры
    sum_up(winner, user, computer)


# Вызов основной функции игры крестики-нолики
main()
