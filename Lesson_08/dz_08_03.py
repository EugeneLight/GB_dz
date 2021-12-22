from functools import wraps


def type_logger(func):
    @wraps(func)
    def wrapper(*args):
        nums = [f'{num}: {type(num)}' for num in args]
        print(*nums, sep='\n')

    return wrapper


@type_logger
def calc_cube(*nums):
    val_nums = [x for x in nums if isinstance(x, int) | isinstance(x, float)]
    return [x ** 3 for x in val_nums]


a = calc_cube([11, 12], 5, 12, 'num', 8, 3.2)
