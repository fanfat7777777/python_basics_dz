import os


def create():
    with open('config.yaml', 'r') as conf:
        line = conf.readlines()
        # Перебираем по строкам
        for i in range(1, len(line) - 1):

            l_old = line[i].replace('|--', '').replace('|', ' ').replace('\n', '')
            l_new = line[i + 1].replace('|--', '').replace('|', ' ').replace('\n', '') \
                if i < len(line) else None

            id_old = l_old.count(' ') // 3
            id_new = l_new.count(' ') // 3

            if id_old > id_new:
                # Цикл возврата к нужной папке
                for way_ret in range(id_old - id_new):
                    os.chdir('..')

            if id_old < id_new:
                # Сначала заходим в директорию
                if not os.path.isdir(l_old.strip()):
                    os.mkdir(l_old.strip())
                    os.chdir(os.getcwd() + rf'\{l_old.strip()}')
                else:
                    os.chdir(os.getcwd() + rf'\{l_old.strip()}')
                # Создаём папку или пропускаем
                if not l_new.count('.'):
                    if not os.path.isdir(l_new.strip()):
                        os.mkdir(l_new.strip())
                # Создаём или перезаписываем файл
                else:
                    with open(l_new.strip(), 'w'):
                        pass

            elif id_old == id_new:
                # Папка
                if not os.path.isdir(l_new.strip()) and not l_new.count('.'):
                    os.mkdir(l_new.strip())
                # Файл
                else:
                    if not os.path.exists(l_new.strip()):
                        with open(l_new.strip(), 'w'):
                            pass


create()
