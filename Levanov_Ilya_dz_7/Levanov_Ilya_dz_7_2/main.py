import os

# то что должно получиться
test = {
    'my_project': {
        'settings': [
            '__init__.py',
            'dev.py',
            'prod.py'],
        'mainapp': [
            '__init__.py',
            'models.py',
            'views.py', {
                'templates': {
                    'mainapp': [
                        'base.html',
                        'index.html'
                    ]
                }
            }
        ]
    }
}

dir_project = {}
my_project = os.getcwd()

with open('config.yaml', 'r') as conf:
    line = conf.readlines()
    for i in range(len(line)):          # Перебираем по строкам
        print(line[i])
        