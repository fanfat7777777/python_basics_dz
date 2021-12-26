class Stationery:
    title = ''

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print('Уникальное сообщение Pen')


class Pencil(Stationery):
    def draw(self):
        print('Уникальное сообщение Pencil')


class Handle(Stationery):
    def draw(self):
        print('Уникальное сообщение Handle')


s = Stationery()
s.draw()

p = Pen()
p.draw()

pc = Pencil()
pc.draw()

h = Handle()
h.draw()
