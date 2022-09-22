# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать
#  все конфеты у своего конкурента?

# i = 100
# while i > 0:
#     a = int(input('Игрок 1 введите количество конфет '))
#     if a > 28 or a < 0:
#         raise ValueError('Играй по правилам')
#     elif a < 29 and a > 0:
#         if i - a == 0:
#             print('Победил 1 игрок')
#             break
#         elif i - a <= 0:
#             raise ValueError('Неверный ход')
#         else:
#             i = i - a
#             print(f'Осталось {i} конфет')
#     b = int(input('Игрок 2 введите количество конфет '))
#     if b > 28 or b < 0:
#         raise ValueError('Играй по правилам')
#     elif a < 29 and a >= 0:
#         if i - b == 0:
#             print('Победил 2 игрок')
#             break
#         elif i - b <= 0:
#             raise ValueError('Неверный ход')
#         else:
#             i = i - b
#             print(f'Осталось {i} конфет')


# a) Добавьте игру против бота

from random import randint


# i = 100
# while i > 0:
#     a = int(input('Игрок 1 введите количество конфет '))
#     if a > 28 or a < 0:
#         raise ValueError('Играй по правилам')
#     elif a < 29 and a > 0:
#         if i - a == 0:
#             print('Победил 1 игрок')
#             break
#         elif i - a <= 0:
#             raise ValueError('Неверный ход')
#         else:
#             i = i - a
#             print(f'Осталось {i} конфет')
#     if i > 28:
#         b = randint(1,28)
#         i = i - b
#         print(f'Бот Арсений забрал {b} конфет')
#         print(f'Осталось {i} конфет')
#     elif i - b == 0:
#         print('Победил 2 игрок')
#         break
#     elif i < 28:
#         b = randint(1,i)
#         print(f'Бот Арсений забрал {b} конфет')
#         i = i - b
#         print(f'Осталось {i} конфет')
#     elif i - b <= 0:
#         raise ValueError('Неверный ход')
#     else:
#         i = i - b
#         print(f'Осталось {i} конфет')

# b) Подумайте как наделить бота ""интеллектом""

# from random import randint


# i = 100
# print(f'Всего {i} конфет')
# while i > 0:
#     a = int(input('Игрок 1 введите количество конфет '))
#     if a > 28 or a < 0:
#         raise ValueError('Играй по правилам')
#     elif a < 29 and a > 0:
#         if i - a == 0:
#             print('Победил 1 игрок')
#             break
#         elif i - a <= 0:
#             raise ValueError('Неверный ход')
#         else:
#             i = i - a
#             print(f'Осталось {i} конфет')
#     if i > 56:
#         b = randint(1,29)
#         i = i - b
#         print(f'Бот Арсений забрал {b} конфет')
#         print(f'Осталось {i} конфет')
#     elif i < 55:
#         b = i % 29
#         i = i - b
#         print(f'Бот Арсений забрал {b} конфет')
#         print(f'Осталось {i} конфет')
#     elif i < 28:
#         b = i
#         i = i - b
#         print(f'Бот Арсений забрал {b} конфет')
#         print(f'Осталось {i} конфет')
#         if i - b == 0:
#             print('Победил Бот Арсений')
#             break

# %28+1 == 0


candies = 150
print(f'{candies} всего конфет')
count = randint(1, 2)
while candies > 0:
    count += 1
    if count % 2 == 0:
        if count == 2:
            print('ходит бот')
            quantity = 20
            print(f'конфет изымаете бот {quantity}')
        else:
            print('ходит бот')
            quantity = 29 - quantity
            print(f'конфет изымаете бот {quantity}')
    else:
        print('ходит игрок')
        quantity = int(input('Введите число конфет которое изымаете - '))
    if 0 < quantity < 29:
        candies -= quantity
        print(f'конфет осталось - {candies}')
    else:
        print('Вы ввели некоректное кол-во конфет, введите число от 1 до 28')
        count -= 1

if count % 2 == 0:
    print('победил бот')
else:
    print('победил игрок')
