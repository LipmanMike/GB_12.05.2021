"""Выяснить тип результата выражений:
15 * 3
15 / 3
15 // 2
15 ** 2
"""

expressions = (15 * 3, 15 / 3, 15 // 2, 15 ** 2)

for ind, expression in enumerate(expressions, 1):
    print(ind, type(expression))

# a = 15 * 3
# b = 15 / 3
# c = 15 // 2
# d = 15 ** 2
# user_list = [a, b, c, d]
#
# for ind, number in enumerate(user_list, 1):
#     print(ind, type(number)) # Не могу понять как вставить placeholder в f строку


