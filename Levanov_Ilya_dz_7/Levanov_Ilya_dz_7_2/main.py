import os

dir_project = {}
my_way = os.getcwd()


def secyr(way, key_way, name):
    # Если файла нет, то создаём его
    if not os.path.exists(name):
        os.mkdir(name)
    # Если это ключевая директория, то переходим в неё
    os.chdir(way + rf'\{name}') if key_way else None


with open('config.yaml', 'r') as conf:
    line = conf.readlines()
    # Перебираем по строкам
    for i in range(1, len(line)):
        l_new = line[i].strip().replace('|--', '').replace('|', '')         # Наша текущая строка
        l_old = line[i - 1].strip().replace('|--', '').replace('|', '')     # Предыдущая строка

        if not l_new.count(' '):        # Если каталог находится в корне проекта
            os.chdir(my_way)            # Возвращаемся в корень
            secyr(my_way, 1, l_new.strip())
        else:
            # Если пробелы есть
            # Проверяем является ли это именем файла
            if l_new.count('.'):
                with open(f'{l_new.strip()}', 'w'):
                    pass
            else:
                # Если это директория
                if l_new.count(' ') > l_old.count(' '):  # Новый подкаталог (Ключевой путь)
                    secyr(os.getcwd(), 1, l_new.strip())
                elif l_new.count(' ') == l_old.count(' '):  # Папка в каталоге
                    secyr(os.getcwd(), 0, l_new.strip())
