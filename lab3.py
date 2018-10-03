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

c = [i+j+k for i, j, k in zip(S[::3], S[1::3], S[2::3])]
E = [i for i in c if i.startswith('Петров')]
print(' '.join(S[0:3]), '\n', '\n'.join(E))

#4

L = 'Пусть дана строка произвольной длины. Выведите информацию о том, сколько в ней символов и сколько слов.'

def count_letters(L):
    return len(L) - L.count(' ')


print(count_letters(L))
print(len(L))
print(len(L.split(' ')))
