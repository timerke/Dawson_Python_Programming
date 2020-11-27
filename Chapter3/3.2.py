"""
Напишите программу, которая бы "подбрасывала" условную монету 100 раз
и сообщала, сколько раз выпал орел, а сколько - решка.
"""

import random

throw_number = 0
max_throw_number = 100
tail_number = 0
while throw_number < max_throw_number:
    coin = random.randint(0, 1)
    if coin == 0:
        tail_number += 1
    throw_number += 1
print(
    f"Из {max_throw_number} бросков монетки решка выпала {tail_number} раз ({tail_number/max_throw_number*100:.2f}%)."
)
