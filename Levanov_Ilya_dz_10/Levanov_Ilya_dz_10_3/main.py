class Cell:

    def __init__(self, cells):
        self.__cells = cells

    def __add__(self, other):
        self.__cells += other
        return self.__cells

    def __sub__(self, other):
        if self.__cells - other > 0:
            self.__cells -= other
            return self.__cells
        else:
            return 'Нельзя получить значение меньше 0'

    def __mul__(self, other):
        self.__cells *= other
        return self.__cells

    def __floordiv__(self, other):
        self.__cells //= other
        return self.__cells

    def __truediv__(self, other):
        self.__cells /= other
        return self.__cells

    def make_order(self, quantity):
        self.__quantity = quantity
        s = ''
        for i in range(1, self.__cells + 1):
            if i % self.__quantity == 0:
                s += '$\n'
            else:
                s += '$'
        print(s)


c = Cell(12)
# print(c + 10)

c.make_order(5)
