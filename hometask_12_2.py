#Файли
#
# 2. Написати декоратор, який буде записувати в файл назву функції, яку він декорує, і писати час її виклику.

from datetime import datetime

LOG_FILE_NAME_TIME = 'log.log'

def log_own_dec(func):
    def time_func(*args, **kwargs):
        with open(LOG_FILE_NAME, 'a') as buff:
            print(f"'{func.__name__}' find that now is {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", file=buff)
        result = func(*args, **kwargs)
        return result
    return time_func


@log_own_dec
def func_1(a, b):
    print(f"func_1 find sum of a and b = {a + b}")


@log_own_dec
def func_2(c, d):
    print(f"func_2 find multiplication of c * d = {c * d}")


@log_own_dec
def general_func_return():
    return 'return func in string form'


func_1(2, 2)
func_2(2, 4)
print(general_func_return())