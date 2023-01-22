# Помилки та винятки
# part 1
# Написати власний декоратор, задачею якого має бути друк назви функції і часу, коли вона була викликана.
# Декоратор має працювати для різних функцій однаково.


from datetime import datetime

def own_dec(func):
    def time_func(*args, **kwargs):
        print(f"'{func.__name__}' find that now is {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        func(*args, **kwargs)
    return time_func

@own_dec
def func_1(a, b):
    print(f"func_1 find sum of a and b = {a + b}")

@own_dec
def func_2(c, d):
    print(f"func_2 find multiplication of c * d = {c * d}")

func_1(2, 2)
func_2(2, 4)


# Помилки та винятки
# Part 2
# Написати кастомний Exception клас, MyCustomException, який має повідомляти "Custom exception is occured".

class MyCustomException(Exception):
    pass

raise MyCustomException('Custom exception is occurred')

# Помилки та винятки
# part 3
# Написати власний менеджер контексту, задачею якого буде друкувати "==========" – 10 знаків дорівнює
# перед виконанням коду та після виконання коду, таким чином виділяючи блок коду символами дорівнює.
# У випадку виникнення будь-якої помилки вона має бути надрукована текстом, проте програма не має завершити своєї роботи.

class own_context_manager():
    def __enter__(self):
        print('=' * 10)
        return self

    def __exit__(self, val_1, val_2, exc_traceback):
        if val_1 is not None:
            print(val_2)
        print('=' * 10)
        return True

with own_context_manager():
    print('Program is running')

with own_context_manager():
    print(1 / 0)

print("Program is closed")


# Помилки та винятки
# part 4
# Написати конструкцію try ... except ... else ... finally, яка буде робити точно те ж,
# що і менеджер контексту із попереднього завдання.



def try_except_else_finally_context_manager(func):
    try:
        print("=" * 10)
        func()
    except Exception as res:
        print(res)
    finally:
        print("=" * 10)


try_except_else_finally_context_manager(lambda: print("My function"))
mtry_except_else_finally_context_manager(lambda: print(1 / 0))

print("Program is closed")