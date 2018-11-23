from tkinter import *


def input_values(a, b, c, k):
    try:
        counter = ((a ** 2 / b ** 2 + c ** 2 * a ** 2) / (a + b + c * (k - a / b ** 3)) + c + (k / b - k / a) * c)
        print(abs(counter))
    except ZeroDivisionError:
        print("Division by zero!")


print('Введите значения')
input_values(int(input()), int(input()), int(input()), int(input()))

num_list = [12, 3, 10, 14.2, 2.1, -10]


def summarize():
    print(sum(i for i in num_list if i > 10))


def maximum():
    print(max(num_list))


list_misc = [1, 2, 4, 2.2, 6, 'text', 4.1, -2]


def give_even():
    for i in list_misc:
        try:
            if i % 2 == 0:
                print(i)
        except TypeError:
            continue


my_number = 4


def cycle():
    while True:
        print('Enter user number')
        user_number = float(input())
        if user_number >= my_number:
            print('Try again')
        else:
            print('Great!')
        break


list_given = ['repeat', 'retest', 'hello', '', '1234567890']


def strings():
    print('\n'.join([elem for elem in list_given if 5 < len(elem) < 10]))


from random import randint


def chars():
    for _ in range(5):
        print(chr(randint(1040, 1071)), end='')


sentence_misc = 'repeat retest 6.2 hello 5 1234567890 0.1 -4'


def digit():
    print(', '.join(x for x in sentence_misc if x.isdigit()))


import string

sentence = 'Пусть дана строка, состоящая из слов, пробелов и знаков препинания.'
exclude = set(string.punctuation)
sentence_first = ''.join(char for char in sentence if char not in exclude)

sentence_list = sentence_first.split()


def words():
    word = ([elem for elem in sentence_list if len(elem) > 5])
    print(', '.join(word))


first_string = 'Ф;И;О;Возраст;Категория;Иванов;Иван;Иванович;23 года;Студент 3 курса;Петров;Семен;Игоревич;22 года;Студент 2 курса'

M = first_string.split(';')


def table():
    print(''.join(M[0:3]), '\t', '\t'.join(M[3:5]))
    print(' '.join(M[5:8]), '\t', '\t'.join(M[8:10]))
    print(' '.join(M[-5:-2]), '\t', '\t'.join(M[-2:]))


second_string = 'ФИО;Возраст;Категория;Иванов Иван Иванович;23 года;Студент 3 курса;Петров Семен Игоревич;22 года;Студент 2 курса;Иванов Семен Игоревич;22 года;Студент 2 курса;Акибов Ярослав Наумович;23 года;Студент 3 курса;Борков Станислав Максимович;21 год;Студент 1 курса;Петров Семен Семенович;21 год;Студент 1 курса;Романов Станислав Андреевич;23 года;Студент 3 курса;Петров Всеволод Борисович;21 год;Студент 2 курса'

item = second_string.split(';')

n = 3
new_list = [item[i:i+n] for i in range(0, len(item), n)]


def surname():
    for x in new_list:
        for y in x:
            if y.startswith('Петров'):
                print(' '.join(x))


rand_string = 'Пусть дана строка произвольной длины. Выведите информацию о том, сколько в ней символов и сколько слов.'


def length():
    print(len(rand_string))
    print(len(rand_string) - rand_string.count(' '))
    print(len(rand_string.split(' ')))


while True:
    user_input = input('Вы хотите продолжить?')
    if user_input == 'yes':
        root = Tk()
        mainmenu = Menu(root)
        root.config(menu=mainmenu)

        usermenu1 = Menu(mainmenu)
        usermenu1.add_command(label='Пример', command=lambda: input_values(int(input()), int(input()), int(input()), int(input())))
        usermenu1.add_command(label='Сумма', command=lambda: summarize())
        usermenu1.add_command(label='Максимум', command=lambda: maximum())
        usermenu1.add_command(label='Четные', command=lambda: give_even())

        usermenu2 = Menu(mainmenu)
        usermenu2.add_command(label='Число', command=lambda: cycle())
        usermenu2.add_command(label='Строки', command=lambda: strings())
        usermenu2.add_command(label='Буквы', command=lambda: chars())
        usermenu2.add_command(label='Цифры', command=lambda: digit())

        usermenu3 = Menu(mainmenu)
        usermenu3.add_command(label='Слова', command=lambda: words())
        usermenu3.add_command(label='Таблица', command=lambda: table())
        usermenu3.add_command(label='Фамилия', command=lambda: surname())
        usermenu3.add_command(label='Длина', command=lambda: length())

        mainmenu.add_cascade(label='Меню 1', menu=usermenu1)
        mainmenu.add_cascade(label='Меню 2', menu=usermenu2)
        mainmenu.add_cascade(label='Меню 3', menu=usermenu3)

        root.mainloop()
        continue
    elif user_input == 'no':
        break
    else:
        continue
