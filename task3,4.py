b = [12, 3, 10, 14.2, 2.1, -10]

a = sum(i for i in b if i>10)
print(a)

c = max(b)
print(c)

d = sum(b)/len(b)
print(d)

from functools import reduce

print(reduce(lambda x, y: x * y, b))