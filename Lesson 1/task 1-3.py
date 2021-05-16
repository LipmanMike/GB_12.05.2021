"""Реализовать склонение слова «процент» для чисел до 20. Например, задаем число 5
— получаем «5 процентов», задаем число 2 — получаем «2 процента». Вывести все склонения для проверки.
"""
num_list = []
for number in range(1, 21):
    num_list.append(number)

first_list = num_list[0]
second_list = num_list[1:4]
third_list = num_list[4:20]

print(f'{first_list} процент')

for number in second_list:
    print(f'{number} процента')

for number in third_list:
    print(f'{number} процентов')