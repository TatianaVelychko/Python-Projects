# task 1

import random

my_number = random.randint(5, 15)

while True:
    print('Enter user number')
    user_number = int(input())
    if user_number >= my_number:
        print('Try again')
    else:
        print('Great!')
        break

# task 2

L = ['repeat', 'retest', 'hello', '', '1234567890']
S = ([elem for elem in L if 5 < len(elem) < 10])
print('\n'.join(S))

# task 4

S = 'repeat retest 6.2 hello 5 1234567890 0.1 -4'
print('\a'.join(x for x in S if x.isdigit()))
