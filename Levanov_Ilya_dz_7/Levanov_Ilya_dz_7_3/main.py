import os
import shutil
import create_file

if not os.path.isdir('templates'):
    os.mkdir('templates')

print('''Создать файлы - y
Пропустить - n''')

create_file.create() if input() == 'y' else None

# Файлы копируются со второго запуска, я пока не понял в чём причина


for root, dirs, files in os.walk(os.getcwd()):
    if root.count('templates') and not root.count('templates\\'):
        for g in os.listdir(root):
            shutil.copytree(rf'{root}', 'templates\\' + g) \
                if not os.path.exists('templates\\' + g) else None

print('Запусти второй раз, чтобы скопировать файлы')
