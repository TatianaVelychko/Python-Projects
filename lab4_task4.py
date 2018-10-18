#4.2

my_len = [['БО-331101', ['Акулова Алена', 'Бабушкина Ксения', 'Зотова Анастасия']], ['БВ-421102', ['Громова Евгения', 'Панина Анна']], ['БО-331103', ['Арнаутова Светлана']]]

G = [j for i in my_len for j in i]
print(G)

S = dict(zip(G[::2], G[1::2]))
print(S)

for key, value in S.items():
    for k in value:
        c = k.split(' ')
        if len(c[0]) < 7:
            print(key, ':', ''.join(k))

#4.1, 4.3

my_len = [['БО-331101', ['Акулова Алена', 'Бабушкина Ксения', 'Зотова Анастасия']], ['БВ-421102', ['Громова Евгения', 'Панина Анна']], ['БО-331103', ['Арнаутова Светлана']]]

G = [j for i in my_len for j in i]
print(G)

S = dict(zip(G[::2], G[1::2]))
print(S)

for key, value in S.items():
    for k in value:
        c = k.split(' ')
        if c[0].startswith('П') and c[1].startswith('А'):
            print(key, ':', ''.join(k))
