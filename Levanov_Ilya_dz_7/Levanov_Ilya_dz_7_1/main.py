import os

my_project = os.getcwd()
starter = {
    my_project: ['settings', 'mainapp', 'adminapp', 'authapp']
}

for create_dir in starter.values():
    for i in create_dir:
        if not os.path.exists(i):
            os.mkdir(i)
