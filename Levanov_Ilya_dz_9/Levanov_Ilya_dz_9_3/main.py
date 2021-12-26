class Worker:
    name = 'Вася'
    surname = 'Пупкин'
    position = 'Механик'
    def parametr(self, wage, bonus):
        self.wage = wage
        self.bonus = bonus
        self.__income__ = {
            'wage': self.wage,
            'bonus': self.bonus
        }


class Position(Worker):
    def get_full_name(self):
        names = f'{self.name} {self.surname}'
        return names

    def get_total_income(self, wage, bonus):
        if type(wage) and type(bonus) in (int, float):
            self.parametr(wage, bonus)
            total_income = self.__income__['wage'] + self.__income__['bonus']
            return total_income
        else:
            ValueError('Введены не числа')

p = Position()
print(p.get_full_name())
print(p.get_total_income(15000, 20000))
