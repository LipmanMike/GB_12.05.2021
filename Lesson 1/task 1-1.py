"""Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах:
a. до минуты: <s> сек;
b. до часа: <m> мин <s> сек;
c. до суток: <h> час <m> мин <s> сек;
d. * в остальных случаях: <d> дн <h> час <m> мин <s> сек.
"""

duration = input('Введите время в секундах: ')
duration = int(duration)

time_hour = (duration // 3600) % 24
time_min = (duration // 60) % 60
time_sec = duration % 60
time_days = duration // (3600 * 24)


print(f'{time_days} дней {time_hour} час {time_min} минут {time_sec} секунд')