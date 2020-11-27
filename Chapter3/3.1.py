"""
Напишите программу - симулятор пирожка с "сюрпризом" - которая бы
при запуске отображала один из пяти различных "сюрпризов", выбранный случайным
образом.
"""

import random

surprise = random.randint(1, 5)
if surprise == 1:
    print("Сюрприз 1")
elif surprise == 2:
    print("Сюрприз 2")
elif surprise == 3:
    print("Сюрприз 3")
elif surprise == 4:
    print("Сюрприз 4")
elif surprise == 5:
    print("Сюрприз 5")
