#1

dic = {'fruit': ['lemon', 'apple'], 'color': ['red', 'green', 'yellow'], 'drink': ['tea', 'coffee']}
print(len(dic.keys()))

#2-4

myf = open('students1.csv', 'w')
myf.write('№;ФИО;Возраст;Группа\n')
myf.write('1;Иванов Иван Иванович;22;БО-111111\n')
myf.write('2;Яшков Илья Петрович;24;БО-222222\n')
myf.write('3;Сидоров Семен Семенович;21;БО-111111\n')
myf.close()

dic = {}

with open('students1.csv', 'r') as myf:
    for line in myf:
        key, *value = line.split(';')
        dic[key] = value

print(dic)

myf2 = open('students2.csv', 'w')

for key, value in sorted(dic.items(), key=lambda value: (value[1])):
    try:
        value[1] = str(int(value[1]) + 1)
        print(key, ':', value)
        myf2.write(';'.join(value))
        myf2.write('\n')

    except ValueError:
        pass

print("Writing complete")
