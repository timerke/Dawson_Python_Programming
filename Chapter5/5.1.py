"""
Создайте программу, которая будет выводить список слов в случайном порядке.
На экране должны печататься без повторений все слова из представленного
списка.
"""

import random

# Функция создает список из уникальных слов
def create_unique_words(words):
    unique_words = []  # список с уникальными словами из words
    for word in words:
        if word not in unique_words:
            unique_words.append(word)
    return unique_words


# Список слов, которые будут выведены на экран
WORDS = ('кот', 'собака', 'мир', 'кот', 'дерево', 'мир')
unique_words = create_unique_words(WORDS)  # список с уникальными словами
# Выводим на экран слова из списка уникальных слов, пока в списке есть слова
while len(unique_words) != 0:
    # Определяем позицию случайного слова, которое будет выведено на экран
    word_position = random.randrange(len(unique_words))
    print(unique_words[word_position])
    # Удаляем выведенное на экран слово из списка уникальных слов
    del unique_words[word_position]
