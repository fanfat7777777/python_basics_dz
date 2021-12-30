class Person:

    def __init__(self, name, meaning):
        self.__name = name.lower()
        self.__meaning = meaning
        self.__len_cloth = 0

    def get_cloth(self):
        return f'{self.__name}: {self.__len_cloth}'

    def set_cloth(self, meaning):
        self.__meaning = meaning
        if self.__name == 'пальто':
            if self.__meaning < 75:
                self.__len_cloth = self.__meaning / 6.5 + 0.5
        elif self.__name == 'костюм':
            if self.__meaning < 200:
                self.__len_cloth = self.__meaning * 2 + 0.3
        else:
            raise AttributeError('Введены не верные значения')

    inf = property(get_cloth, set_cloth)


p = Person('Пальто', 20)
p.inf = 65
print(p.inf)
