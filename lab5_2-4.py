import csv

myf = open('students.csv', 'w')
myf.write('№;ФИО;Возраст;Группа\n')
myf.write('4;Мамаев Олег Борисович;25;БО-333333\n')
myf.write('2;Сидоров Семен Семенович;23;БО-111111\n')
myf.write('1;Иванов Иван Иванович;23;БО-111111\n')
myf.write('3;Яшков Илья Петрович;24;БО-222222\n')
myf.close()

with open('students.csv', 'r') as myf:
    reader = csv.reader(sorted(myf, key=lambda li: li.split(';')[1]))
    lst = [row for row in reader]

print(lst)

myf = open('students.csv', 'w')
for elem in lst:
    for myst in elem:
        el = myst.split(';')
        try:
            el[2] = str(int(el[2]) + 1)
            myf.write(';'.join(el))
            myf.write('\n')

        except ValueError:
            pass

print("Writing complete")
