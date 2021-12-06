#Упрощённый вариант ДЗ
prices = [57.8, 46.51, 97, 7, 3, 6, 12.05, 184.1, 5.2, .8]
print(prices)

print('\n', 'A)')
for i in prices:
    print(f'{int(i)} руб {int(i * 100 % 100):02d} коп', end=' ')
print(id(prices))

print('\n', 'B)')
prices.sort()
print(prices, id(prices))

print('\n', 'C)')
new_price = sorted(prices, reverse=True)
print(new_price, id(new_price))

print('\n', 'C)')
print(new_price[:5])