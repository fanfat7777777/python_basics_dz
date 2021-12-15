d = {}
with open('nginx_logs.txt', 'r') as f:
    for line in f:
        k = line[:line.find('- ')]  # получаем ip
        d[k] = d[k] + 1 if k in d else d[k] = 1

spam = max(d, key=d.get)  # Находим ip спамера
print(f'ip спамера - {spam}: {d[spam]}')
