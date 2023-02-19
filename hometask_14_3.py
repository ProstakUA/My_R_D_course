#Регулярні вирази (RegEx) в Python
#
# 3. (необов'язкове виконання) Написати програму, яка буде:
#
# зчитувати текст із файлу, назва якого вводиться користувачем (program argument або input)
# знаходити всі email в тексті і змінювати їх на X***@****X, де замість Х мають бути перша і остання літери
# справжньої адреси, а весь інший текст має бути замінений на *. Кількість * необовʼязково
# має відповідати кількості замінених символів

from os import path
import sys
import re


if len(sys.argv) < 2:
    file_txt = input("What's your file name: ")
else:
    file_txt = sys.argv[1]


if not path.exists(file_txt):
    print(f"File with your inputted name - '{file_txt}' not found")
    exit()

with open(file_txt, 'r') as buff:
    text = buff.read()


if not path.exists(file_txt):
    print(f"File with your inputted name - '{file_txt}' not found")
    exit()


with open(file_txt, 'r') as buff:
    text = buff.read()

email_regex = r'(?!\b)[a-zA-Z\d_.-]{0,63}[a-zA-Z\d]@([a-zA-Z\d-]{0,63}[a-zA-Z\d](\.[a-zA-Z]{1,14}){1,2})(?<!\b)'
x = re.sub(email_regex, '***@****', text)
print(x)