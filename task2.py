L = [1, 2, 4, 'test', 2.2, 6, 4.1, -2]

for i  in L:
    try:
        if i%2 == 0:
            print(i)
    except TypeError:
        continue
