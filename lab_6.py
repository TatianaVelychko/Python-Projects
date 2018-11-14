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


L = [1, 2, 4, 2.2, 6, 'text', 4.1, -2]


def give_even():
    for i in L:
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


M = ['repeat', 'retest', 'hello', '', '1234567890']


def strings():
    print('\n'.join([elem for elem in M if 5 < len(elem) < 10]))


from random import randint


def chars():
    for _ in range(5):
        print(chr(randint(1040, 1071)), end='')


S = 'repeat retest 6.2 hello 5 1234567890 0.1 -4'


def digit():
    print(', '.join(x for x in S if x.isdigit()))


while True:
    user_input = input('Вы хотите продолжить?')
    if user_input == 'yes':
        root = Tk()
        mainmenu = Menu(root)
        root.config(menu=mainmenu)

        usermenu1 = Menu(mainmenu)
        usermenu1.add_command(label='Сумма', command=lambda: summarize())
        usermenu1.add_command(label='Максимум', command=lambda: maximum())
        usermenu1.add_command(label='Четные', command=lambda: give_even())

        usermenu2 = Menu(mainmenu)
        usermenu2.add_command(label='Число', command=lambda: cycle())
        usermenu2.add_command(label='Строки', command=lambda: strings())
        usermenu2.add_command(label='Буквы', command=lambda: chars())
        usermenu2.add_command(label='Цифры', command=lambda: digit())

        mainmenu.add_cascade(label='Меню 1', menu=usermenu1)
        mainmenu.add_cascade(label='Меню 2', menu=usermenu2)

        root.mainloop()
        continue
    elif user_input == 'no':
        break
    else:
        continue
