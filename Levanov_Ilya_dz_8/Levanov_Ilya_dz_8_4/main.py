def arg_dec(arg_decoratora):
    def my_decorator(function):
        def wrapper(arg):
            try:
                return function(arg) if arg_decoratora(arg) else f'Неверный аргумент: {arg}'
            except NameError as err:
                return err
            except TypeError as err:
                return err
            except:
                return 'Неизвестная ошибка'
        return wrapper
    return my_decorator


@arg_dec(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


print(calc_cube('1.2'))
