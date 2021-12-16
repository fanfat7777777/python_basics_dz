import os.path
my_dict = {}

with open('users.csv', 'r', encoding='utf-8') as a, open('hobby.csv', 'r', encoding='utf-8') as b:
    def f_cl(line, key):
        line = line.replace(',', ' ') if key == 'k' else line
        line = line.replace('\n', '') if key == 'k' or key == 'v' else line
        return line

    k = [f_cl(l, 'k') for l in a]               #Список ключей
    v = [f_cl(l, 'v') for l in b]               #Список значений

    if len(v) > len(k):
        print('1')
    else:
        for i in range(len(k)):
            my_dict[k[i]] = None if i >= len(v) else v[i]               #Создаём словарь

        id_files = 'w' if os.path.exists('parameters.csv') else 'x'     #Проверяем наличие файла
        with open('parameters.csv', id_files, encoding='utf-8') as p:
            for k, v in my_dict.items():
                p.write(f'{k}: {v}\n')
print(my_dict)