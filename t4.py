# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10
digit = []
value = 4
while value >= 2:
    digit.append(value % 2)
    value //= 2
digit.append(value)
digit.reverse()
print(*digit) 