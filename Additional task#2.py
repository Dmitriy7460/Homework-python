# Задача2 Де моргана необязательная
# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# в цикле 100 раз прогоняем
# каждый раз генерируем случайное количество предикат от 3 до 15
# и конечно со случайным булевым значением
# и засекаем общее время выполнения программы
# юзаем библиотеки random и time
# предикаты НЕ ЗАДАЕМ как целое число!

# import time

# seconds = time.time()
# print("Секунды с начала эпохи =", seconds)

import time
seconds1 = time.time()

import random
n= random.randint(3,15)

for i in range(100):
    for i in range (random.randint(4,16)):
        r= random.choice([True, False])
        x = r or r 
        y =  not r and not r

    print (not(x), "=", (y),(i))

seconds2 = time.time()
print("Общее время выполнения программы:", (seconds2 - seconds1))