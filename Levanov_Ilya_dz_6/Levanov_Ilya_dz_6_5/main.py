import os.path
import sys

my_dict = {}


def check_f(text):
    print(text)
    f_name = input()
    while not os.path.exists(f_name):  # проверяем наличие файлов
        print('Такого файла нет')
        f_name = input()
    sys.argv.append(f_name)


check_f('Введите файл с пользователями')
check_f('Введите файл с хобби: ')

with open(sys.argv[1], 'r', encoding='utf-8') as a, open(sys.argv[2], 'r', encoding='utf-8') as b:
    def f_cl(line, key):
        line = line.replace(',', ' ') if key == 'k' else line
        line = line.replace('\n', '') if key == 'k' or key == 'v' else line
        return line


    k = [f_cl(line, 'k') for line in a]  # Список ключей
    v = [f_cl(line, 'v') for line in b]  # Список значений

    if len(v) > len(k):
        print('1')
    else:
        for i in range(len(k)):
            my_dict[k[i]] = None if i >= len(v) else v[i]  # Создаём словарь

        id_files = 'w' if os.path.exists('parameters.csv') else 'x'  # Проверяем наличие файла
        with open('parameters.csv', id_files, encoding='utf-8') as p:
            for k, v in my_dict.items():
                p.write(f'{k}: {v}\n')
print(my_dict)
