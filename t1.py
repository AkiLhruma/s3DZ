# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

# Пример:

# - 6 -> да
# - 7 -> да
# - 1 -> нет

d = int(input('Input day number: '))
if 5 < d < 8:
    print('yes')
elif 0 < d < 6:
    print('no')
elif d <= 0 or d > 7:
    print('incorrect input.')