prices = [57.8, 46.51, 97, 7, 3]
print(prices)
print()

print('A)')
for i in range(0, len(prices)):
    prices[i] = '%.2f' % prices[i]              #делаем 2 знака после запятой
    k = prices[i].split('.')
    if len(k[0]) == 1:
        k[0] = k[0].replace(k[0], f'0{k[0]}')   #делаем 2 знака перед запятой
    print(f"{k[0]} руб {k[1]} коп")
    k = f"{k[0]}.{k[1]}"
    prices[i] = k

print()
print('B) Цены по возрастанию')
prices.sort()
for i in range(0, len(prices)):
    k = prices[i].split('.')
    print(f"{k[0]} руб {k[1]} коп")

print()
print('C) Сортировка по убыванию')
new_prices = prices
new_prices.sort(reverse=True)
print(new_prices)

print()     #Подзадача D
max_prices = prices                 #Получаем список
max_prices.sort(reverse=True)       #Сортируем

if len(max_prices) >= 5:            #Если цен в списке 5 и более, то выведем 5 максимальных цен
    len_prices = 5
else:                               #Если меньше 5, то выведем сколько есть
    len_prices = len(max_prices)
print(f'D) {len_prices} макс цен')

for i in range(0, len_prices):
            k = prices[i].split('.')
            print(f"{k[0]} руб {k[1]} коп")