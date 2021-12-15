import sys

with open('bakery.csv', 'a+', encoding='utf-8') as a:
    mods = input('Чтение/Запись?(w/r)')
    if mods == 'r':                     #Чтение
        a.seek(0)
        end = len(a.readlines())

        def bak_r(start = 1, end = end):
            if start > end:
                print(f'В файле {end} записи(ей)')
            a.seek(0)
            b = a.readlines()
            for i in range(start - 1, end):
                print(b[i].replace('\n', ''))

        if len(sys.argv) == 1:          #Условия вывода
            bak_r()
        elif len(sys.argv) == 2:
            bak_r(int(sys.argv[1]))
        elif len(sys.argv) == 3:
            bak_r(int(sys.argv[1]), end if int(sys.argv[2]) > end else int(sys.argv[2]))

    elif mods == 'w':                       #Запись
        print('Для выхода: exit')
        sys.argv.append('')
        while sys.argv[1] != 'exit':
            sys.argv[1] = input()
            a.write(f'{sys.argv[1]}\n') if sys.argv[1] != 'exit' else None
    else:
        print('Неверная команда')