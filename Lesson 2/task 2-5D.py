prices = [453.4, 74, 478.0, 33.8, 911.2, 015.27, 167.05, 28.2, 932.1, 032.5]
sorted_prices = max(prices)

for price in sorted_prices:
    rub, kop = str(f'{price:.2f}').split('.')
    print(f'{rub} руб. {int(kop):02d} коп.,', end=' ')