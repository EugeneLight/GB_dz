from functools import wraps


def val_checker(sub):
    def sub_val_checker(func):
        @wraps(func)
        def wrapper(arg):
            if sub(arg):
                print(func(arg))
            else:
                raise ValueError(f'wrong val: {arg}')

        return wrapper

    return sub_val_checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return int(x) ** 3


try:
    a = calc_cube(-4)
except ValueError as e:
    print(e)
