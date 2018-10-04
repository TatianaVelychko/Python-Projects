#1

import string

L = 'Пусть дана строка, состоящая из слов, пробелов и знаков препинания.'
exclude = set(string.punctuation)
K = ''.join(ch for ch in L if ch not in exclude)

S = K.split()

M = ([elem for elem in S if len(elem) > 5])
print('\t'.join(M))

H = ([elem for elem in S if elem.endswith('ов')])
print('\t'.join(H))

#2

my_string = 'Ф;И;О;Возраст;Категория;Иванов;Иван;Иванович;23 года;Студент 3 курса;Петров;Семен;Игоревич;22 года;Студент 2 курса'

M = my_string.split(';')
print(M)

print(''.join(M[0:3]), '\t', '\t'.join(M[3:5]))
print(' '.join(M[5:8]), '\t', '\t'.join(M[8:10]))
print(' '.join(M[-5:-2]), '\t', '\t'.join(M[-2:]))

#3

my_string = 'ФИО;Возраст;Категория;Иванов Иван Иванович;23 года;Студент 3 курса;Петров Семен Игоревич;22 года;Студент 2 курса;Иванов Семен Игоревич;22 года;Студент 2 курса;Акибов Ярослав Наумович;23 года;Студент 3 курса;Борков Станислав Максимович;21 год;Студент 1 курса;Петров Семен Семенович;21 год;Студент 1 курса;Романов Станислав Андреевич;23 года;Студент 3 курса;Петров Всеволод Борисович;21 год;Студент 2 курса'

S = my_string.split(';')
print(S)

n = 3
D = [S[i:i+n] for i in range(0, len(S), n)]
print(D)

for x in D:
    for y in x:
        if y.startswith('Петров'):
            print(' '.join(x))

for z in D:
    if '21 год' in z:
        print(' '.join(z))

#4

L = 'Пусть дана строка произвольной длины. Выведите информацию о том, сколько в ней символов и сколько слов.'

print(len(L))
print(len(L) - L.count(' '))
print(len(L.split(' ')))