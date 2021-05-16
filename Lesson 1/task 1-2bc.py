"""Создать список, состоящий из кубов нечётных чисел от 1 до 1000:
a. Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
Например, число «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 +5+9=28–
делится нацело на 7. Внимание: использовать только арифметические операции!
b. К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого
списка, сумма цифр которых делится нацело на 7.
c. * Решить задачу под пунктом b, не создавая новый список."""
# Получилось решить задача b и b* сразу не создавая нового списка, просто изменив код в п. 14

cubed_list = []
all_sum = 0

for number in range(1, 1001, 2):
    cubed_list.append((number ** 3) + 17)  # Просто добавляю + 17 к каждому элементу списка.

for ind, val in enumerate(cubed_list):
    sum_digits = 0
    while val > 0:
        sum_digits += val % 10
        val //= 10
    if sum_digits % 7 == 0:
        all_sum += cubed_list[ind]

print(all_sum)