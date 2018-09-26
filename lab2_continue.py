# 2.4

L = ['repeat', 'retest', 'hello', '', '1234567890']
S = ([elem for elem in L if elem.startswith('r')])
print('\n'.join(S))

# 3.2

print('enter S')
S = int(input())
L = 'R' * S

print(L)

# 3.3

import string
import random

S = ''.join(random.choice(string.digits) for _ in range(6))

if '3' in S:
    print(S)
else:
    print("S doesn't continue 3")

# 3.4

import string
import random

S = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))

if S.isalpha():
    print('digit is not in S')
else:
    print(S)
