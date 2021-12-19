import os
import create_file
print('''Создать файлы - y
Пропустить - n''')

create_file.create() if input() == 'y' else None


for root, dirs, files in os.walk(os.getcwd()):
    pass
    # print(root, dirs, files)
    # if root.count('templates'):
    #     print(root, dirs, files)

