class Car:
    speed = 0
    color = 'white'
    name = 'Nissan'
    is_police = False

    def go(self):
        return f'Машина {self.__class__.__name__} поехала'

    def stop(self):
        return f'Машина {self.__class__.__name__} остановилась'

    def turn(self, direction):
        self.direction = direction
        return f'Машина {self.__class__.__name__} повернула на {self.direction}'

    def show_speed(self, speed):
        self.speed = speed
        return f'Скорость машины {self.__class__.__name__} = {self.speed}'

    # def check_speed(self, speed):                 # вариант проверки
    #     self.speed = speed
    #     if self.__class__.__name__ == 'TownCar' and self.speed > 60:
    #         return f'{self.__class__.__name__} Вы превысили скорость'
    #     elif self.__class__.__name__ == 'WorkCar' and self.speed > 40:
    #         return f'Машина {self.__class__.__name__} превысила скорость'
    #     else:
    #         return f'Скорость машины {self.__class__.__name__} = {self.speed}'


class TownCar(Car):
    def show_speed(self, speed):
        self.speed = speed
        # return self.check_speed(self.speed)       # вариант проверки
        if self.speed > 60:
            return f'{self.__class__.__name__} Вы превысили скорость'
        else:
            return f'Скорость машины {self.__class__.__name__} = {self.speed}'


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self, speed):
        self.speed = speed
        # return self.check_speed(self.speed)       # вариант проверки
        if self.speed > 40:
            return f'Машина {self.__class__.__name__} превысила скорость'
        else:
            return f'Скорость машины {self.__class__.__name__} = {self.speed}'


class PoliceCar(Car):
    pass

b = TownCar()
print(b.go())
print(b.show_speed(50))
print(b.turn('лево'))
print(b.show_speed(70))
print(b.stop())
print('#'*50)

w = WorkCar()
print(w.go())
print(w.show_speed(20))
print(w.turn('право'))
print(w.show_speed(45))
print(w.stop())
print('#'*50)

p = PoliceCar()
print(p.go())
print(p.show_speed(60))
print(p.turn('лево'))
print(p.show_speed(80))
print(p.stop())
print('#'*50)
