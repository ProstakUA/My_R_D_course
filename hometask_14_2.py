#Регулярні вирази (RegEx) в Python

# 2. (необов'язкове виконання) Написати програму, яка буде:
# зчитувати текст із файлу, назва якого вводиться користувачем (program argument або input)
# знаходити всі email в тексті і змінювати їх на *@*.

from os import path
import re
import sys

if len(sys.argv) < 2:
    file_txt = input("What's your file name: ")
else:
    file_txt = sys.argv[1]

if not path.exists(file_txt):
    print(f"File with your inputted name - '{file_txt}' not found")
    exit()

with open(file_txt, 'r') as buff:
    text = buff.read()

email_regex = r'(?![_.-])((?![_.-][_.-])[a-zA-Z\d_.-]){0,63}[a-zA-Z\d]@((?!-)((?!--)[a-zA-Z\d-]){0,63}[a-zA-Z\d]\.){1,2}([a-zA-Z]{2,14}\.)?[a-zA-Z]{2,14}'
x = re.sub(email_regex, '*@*', text)
print(x)