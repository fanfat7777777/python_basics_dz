class Data:
    def __init__(self, k_date):
        self.k_date = k_date        # Получаем строку с датой дд-мм-гггг

    @staticmethod
    def validate(numbers):               # Проверяем на число
        if 0 < numbers[0] > 31:
            numbers[0] = 'Неверное указано число'
        if 0 < numbers[1] > 12:
            numbers[1] = 'Неверно указан месяц'
        for i in numbers:
            print(i, end=' ')

    @classmethod
    def mutable_date(cls, k_date):                # Разбиваем строку и переводим в числа
        numbers = k_date.split('-')
        for i in range(len(numbers)):
            numbers[i] = int(numbers[i])
        cls.validate(numbers)

    def import_date(self):
        self.mutable_date(self.k_date)


v = Data('11-12-1998')
v.import_date()
