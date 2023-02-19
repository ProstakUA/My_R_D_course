#Регулярні вирази (RegEx) в Python
#
# 1. До завдання, в якому ви реалізовували телефонну книгу, додати валідацію номера телефону за допомогою
# RegEx. Врахувати можливість декількох форматів: +380XXXXXXXXX, 380XXXXXXXXX, 0XXXXXXXXX


import json
import re

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

PHONE_BOOK_DATA_FILE = 'phonebook.json'

try:
    with open(PHONE_BOOK_DATA_FILE, 'r') as buff:
        phone_book = json.load(buff)
except FileNotFoundError:
    phone_book = {}


def stats_info():
    print(f"In your phone book present {len(phone_book)} entry(ies) number(s)")


def add_info_to_phone_book(name, phone):
    if name in phone_book:
        print(f"{name} has been added earlier")
    else:
        if check_in_phone(phone):
            phone_book[name] = phone
            with open(PHONE_BOOK_DATA_FILE, 'w') as buff:
                json.dump(phone_book, buff)
            print("Your new phone number has been added")
        else:
            print("You have a mistake, please, use a correct format: add <name> <phone>")



def delete_info_from_phone_book(name):
    if name not in phone_book:
        return False
    else:
        del phone_book[name]
        with open(PHONE_BOOK_DATA_FILE, 'w') as buff:
            json.dump(phone_book, buff)
        return True


def list_info_from_phone_book():
    if len(phone_book) > 0:
        for key, value in phone_book.items():
            print(f"{key} {value}")
    else:
        print("Your phone book list is empty")


def show_name_info_from_phone_book(name):
    print(f"{name} {phone_book[name] if name in phone_book else 'not present at your list'}")


def check_in_phone(phone):
    regex = "(\+?38)?0\d{9}$"
    return re.fullmatch(regex, phone)


while True:
    users_input = input("Enter your new number: ")

    if len(users_input) < 1:
        print("Please, enter correct data")
        continue

    users_splitted_data = users_input.split()

    match users_splitted_data[0]:
        case 'stats':
            stats_info()
        case 'add':
            if len(users_splitted_data) == 3:
                add_info_to_phone_book(users_splitted_data[1], users_splitted_data[2])
            else:
                print("You have a mistake, please, use a correct format: add <name> <phone>")
        case 'delete':
            if len(users_splitted_data) == 2:
                if delete_info_from_phone_book(users_splitted_data[1]):
                    print(f"{users_splitted_data[1]} has been deleted")
                else:
                    print(f"{users_splitted_data[1]} is not present at list")
            else:
                print("Oops. We have a mistake, please, use a correct format: delete <name>")
        case'list':
            list_info_from_phone_book()
        case 'show':
            show_name_info_from_phone_book(users_splitted_data[1])
        case 'exit':
            break
        case 'notice':
            print(noticement)
        case _:
            print("Unsupported command")