import time


class TrafficLight:
    __color__ = {7: 'красный', 2: 'жёлтый', 3: 'зелёный'}

    @classmethod
    def color_change(cls):
        for k, v in cls.__color__.items():
            print(v), time.sleep(k)


print('TrafficLight:\n', TrafficLight())
TrafficLight().color_change()

test = TrafficLight()
print('test:\n', test)
test.color_change()
