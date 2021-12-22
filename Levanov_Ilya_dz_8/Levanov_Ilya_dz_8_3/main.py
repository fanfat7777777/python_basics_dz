from functools import wraps


def type_logger(func):
    @wraps(func)  # Сохранит имя функции calc_cube, и не перезапишет его как wrapper
    def wrapper(*args, **kwargs):
        numbers = list(args) + list(kwargs.values())
        my_list = []
        for i in numbers:
            my_list.append(f'{i}({func(i)}): {type(func(i))}')
        return my_list
    return wrapper


@type_logger
def calc_cube(x):
    return x ** 3


print(calc_cube.__name__, calc_cube(3, 4, number=2))
