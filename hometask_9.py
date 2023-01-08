# Рекурсія
# Створити програму, яка буде приймати число і друкувати відповідне число в послідовності Фібоначчі, використовуючи генератори.

def fib_gen(n):
    fib_prev = 0
    fib_aft = 1
    for i in range(n):
        yield fib_prev
        fib_prev, fib_aft = fib_aft, fib_prev + fib_aft


def fib_num_by_index(i):
    i += 1
    result = None
    for item in fib_gen(i):
        result = item
    return result

while True:
    users_input = input("Please, input the sequence number from the Fibonacci sequence that interests you: ")
    try:
        num_in_a_fib_row = int(users_input)
    except ValueError:
        print("Mistake! Please input an integer number!")
        continue
    if num_in_a_fib_row < 0:
        print("Mistake! Please input a positive integer number!")
        continue
    break

number = fib_num_by_index(num_in_a_fib_row)
print(f"Fibonacci number with inputted the sequence number from the sequence row {num_in_a_fib_row} is {number}")