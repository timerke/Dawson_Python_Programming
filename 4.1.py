"""
Напишите программу, которая бы считала по просьбе пользователя.
Надо позволить пользователю ввести начало и конец счета, а также
интервал между называемыми целыми числами.
"""

first_number = int(input("Введите начало счета: "))
second_number = int(input("Введите конец счета: "))
interval = int(input("Введите интервал счета: "))
for i in range(first_number, second_number + 1, interval):
    print(i)
