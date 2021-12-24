class Road:
    def __init__(self, __length__ = 0, __width__ = 0):
        self.__length__ = __length__
        self.__width__ = __width__

    @classmethod
    def __calculate__(cls, x):
        return type(x) in (int, float)

    def self__values(self, __length__, __width__):
        if self.__calculate__(__length__) and self.__calculate__(__width__):
            self.__length__ = __length__
            self.__width__ = __width__
            print(self.__length__ * self.__width__ * 25 * 5)

calc = Road()
calc.self__values(5000, 20)
