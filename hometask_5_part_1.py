# Цикли (частина 1)

# Створити програму, яка буде очікувати від користувача введення тексту
# і виведе інформацію по кожному надрукованому символу:
# це “число” + яке воно (парне, непарне),
# це “буква” + яка вона (велика чи маленька),
# це “символ”

users_text = input("Please, enter your text: ")

for value in users_text:
    if value.isdigit():
        if int(value) % 2 == 0:
            print(f"The entered {value} is an even number")
        else:
            print(f"The entered {value} is an odd number")
    elif value.isalpha():
        if value.isupper():
            print(f"The entered {value} is a letter in upper case")
        else:
            print(f"The entered {value} is a letter in lower case")
    else:
        print(f"The entered {value} is a symbol")