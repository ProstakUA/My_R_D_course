# Базові типи даних та операції. Part 2

users_text = input("Please, enter your text: ")
if users_text.isdigit():
    if int(users_text) % 2 == 0:
        print("The entered text is an even number")
    else:
        print("The entered text is an odd number")
else:
    print("The entered text is a word and has a length of " + str(len(users_text)) + " character(s).")
