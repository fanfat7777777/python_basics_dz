import os

my_dict = {}


def calc(count):
    if my_dict.get(count) is None:
        my_dict[count] = 1
    else:
        v = my_dict[count] + 1
        my_dict[count] = v


for root, dirs, files in os.walk(rf'{os.getcwd()}\some_data'):
    for fil in os.listdir(root):
        if fil.count('.'):
            n = 100000
            while n >= 100:
                if n == 100:
                    calc(n) if os.path.getsize(rf'{root}\{fil}') < n else None
                elif n // 10 < os.path.getsize(rf'{root}\{fil}') < n:
                    calc(n)
                n //= 10

# Архив с файлами видимо обновили, т.к.
# в методичке, не верные данные по количеству файлов определённого размера
print(my_dict)
