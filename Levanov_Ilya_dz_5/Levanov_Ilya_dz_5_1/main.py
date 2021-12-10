def odd_nums():
    for i in range(1, 15 + 1, 2):
        yield i
a = odd_nums()
print(list(a), 'Используем yield')

a = [i for i in range(1, 15 + 1, 2)]
print(a, 'Не используем yield')