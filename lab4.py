#1

a = []
k = 1
for r in range(5):
    a.append([])
    for c in range(5):
        a[r].append(k)
        k += 1

for r in a:
    print(r)
print(sum(sum([i for i in x])for x in a))

#2

L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
del L[:2]
L.extend([11, 12])

del L[1::2]
L.extend([11, 12])

del L[3:8]
L.extend([11, 12])

L.insert(0, [1, 2, 3, 4, 5])
del L[2::2]

print(L)

#3

my_len = [['БО-331101', ['Акулова Алена', 'Бабушкина Ксения', 'Зябликова Анастасия']], ['БВ-421102', ['Громова Евгения', 'Кудрявцева Анна']], ['БО-331103', ['Караваева Светлана']]]

s = my_len.pop(0)
print(s[0], '\n', '\n'.join(s[1]))

K = my_len.pop(0)
print(K[0], ':', ', '.join(K[1]))

for k in my_len:
    print(k[0], '\n', '\n'.join(k[1]))

for S in my_len:
    if S[0].startswith('БО'):
        print(S[0], ':', ', '.join(S[1]))

#4

my_len = [['БО-331101', ['Акулова Алена', 'Бабушкина Ксения', 'Зябликова Анастасия']], ['БВ-421102', ['Громова Евгения', 'Кудрявцева Анна']], ['БО-331103', ['Арнаутова Светлана']]]

G = [j for i in my_len for j in i]
print(G)

S = dict(zip(G[::2], G[1::2]))
print(S)

for key, value in S.items():
    for i in value:
        if i.startswith('А'):
            print(key, ':', ''.join(i))
