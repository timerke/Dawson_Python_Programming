"""
Доработайте функцию ask_number() так, чтобы ее можно было вызывать
еще с одним параметром - кратностью (величиной шага). Сделайте шаг
по умолчанию равным 1.
"""


def ask_number(question, low, high, multiplicity=1):
    """Функция просит ввести число из диапазона"""
    response = None
    while response not in range(low, high, multiplicity):
        response = int(input(question))
    return response


low = 1
high = 20
multiplicity = 3
question = f"Введите число от {low} до {high} с шагом {multiplicity}: "
ask_number(question, low, high, multiplicity)
