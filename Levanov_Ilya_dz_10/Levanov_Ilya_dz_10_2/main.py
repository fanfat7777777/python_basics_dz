class Person:

    def __init__(self, name, meaning):
        self.__name = name.lower()
        self.__meaning = meaning
        self.__len_cloth = 0

    @property
    def cloth(self):

        return f'{self.__name}: {self.__len_cloth}' if self.__len_cloth != 0 \
            else 'Введены не верные значения'

    @cloth.setter
    def cloth(self, meaning):
        self.__meaning = meaning
        if self.__name == 'пальто':
            if self.__meaning < 75:
                self.__len_cloth = round(self.__meaning / 6.5 + 0.5, 2)
        elif self.__name == 'костюм':
            if self.__meaning < 200:
                self.__len_cloth = round(self.__meaning * 2 + 0.3, 2)


p = Person('Пальто', 20)
p.cloth = 55
print(p.cloth)


