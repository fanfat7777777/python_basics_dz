def arg_dec(arg_decoratora):
    def my_decorator(function):
        def wrapper(arg):
            return function(arg) if arg_decoratora(arg) else f'Неверный аргумент: {arg}'
        return wrapper
    return my_decorator


@arg_dec(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


print(calc_cube(3))
