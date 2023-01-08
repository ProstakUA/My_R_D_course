# Колекції та структури даних. Part 1

# Створити телефонну книгу, яка матиме наступні команди:
# stats: кількість записів
# add: додати запис
# delete <name>: видалити запис за іменем (ключем)
# list: список всіх імен в книзі
# show <name>: детальна інформація по імені
# Записи не мають повторюватися, заборонено перезаписувати записи, тільки видаляти і додавати заново.

print("My_phone_book©")
print("At your My_phone_book© application present some commands: stats, add <name> <phone>, delete <name>, list, show <name>, exit, notice")
noticement = """
------------------------------------------------------------------------------------------------------------
My_phone_book©
Useful commands for this My_phone_book© application:
stats              - shows numbers of My_phone_book© entries
add <name> <phone> - adds <name> and <phone> number to My_phone_book©, if <name> has not been added earlier
show <name>        - prints name and phone number for entry <name>
delete <name>      - delete phone number from My_phone_book© by <name>
list               - shows all numbers what have entered to My_phone_book©
exit               - finishes work with program
notice             - shows a list of supported commands again
------------------------------------------------------------------------------------------------------------
"""

phone_book = {}
while True:
    users_input = input("Enter your new number: ")
    if len(users_input) < 1:
        print("Please, enter correct data")
        continue
    users_splitted_data = users_input.split()
    match users_splitted_data[0]:
        case 'stats':
            print(f"In your phone book present {len(phone_book)} entry(ies) number(s)")
        case 'add':
            if len(users_splitted_data) == 3:
                if users_splitted_data[1] not in phone_book:
                    phone_book[users_splitted_data[1]] = users_splitted_data[2]
                    print("Your new phone number has been added")
                else:
                    print(f"{users_splitted_data[1]} has been added earlier")
            else:
                print("You have a mistake, please, use a correct format: add <name> <phone>")
        case 'delete':
            if len(users_splitted_data) == 2:
                if users_splitted_data[1] in phone_book:
                    del phone_book[users_splitted_data[1]]
                    print(f"{users_splitted_data[1]} has been deleted")
                else:
                    print(f"{users_splitted_data[1]} is not present at list")
            else:
                print("Oops. We have a mistake, please, use a correct format: delete <name>")
        case 'list':
            if len(phone_book) > 0:
                for key, value in phone_book.items():
                    print(f"{key} {value}")
            else:
                print("Your phone book list is empty")
        case 'show':
            if phone_book.get(users_splitted_data[1]) is not None:
                print(f"{users_splitted_data[1]} {phone_book[users_splitted_data[1]]}")
            else:
                print(f"{users_splitted_data[1]} not present at your list")
        case 'exit':
            break
        case 'notice':
            print(noticement)
        case _:
            print("Unsupported command")