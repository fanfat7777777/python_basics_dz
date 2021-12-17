import os

dir_project = {}


with open('config.yaml', 'r') as conf:
    line = conf.readlines()

    for i in range(1, len(line)):                                       # Перебираем по строкам
        l_new = line[i].strip().replace('|--', '').replace('|', '')     # Наша текущая строка
        l_old = line[i-1].strip().replace('|--', '').replace('|', '')   # Предыдущая строка

        # Если файла нет, то
        if not os.path.exists(l_new):
            # Создаём каталог
            if not l_new.count(' '):
                print()
                my_project = os.getcwd() + rf'\{l_new}'
                print(my_project)
            else:
                # Если пробелы есть
                # Проверяем является ли это именем файла
                if l_new.count('.'):
                    print(my_project + '\\' + l_new.strip())
                else:
                    # Если не файл, то это директория
                    if l_new.count(' ') > l_old.count(' '):     # Новый подкаталог
                        my_project += '\\' + l_new.strip()
                        print(my_project)
                    elif l_new.count(' ') == l_old.count(' '):  # Папка в каталоге
                        print(my_project + '\\' + l_new.strip())
