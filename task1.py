print("a=")
a = int(input())

print("b=")
b = int(input())

print("c=")
c = int(input())

print("k=")
k = int(input())

try:
    S = ((a ** 2 / b ** 2 + c ** 2 * a ** 2) / (a + b + c * (k - a / b ** 3)) + c + (k / b - k / a) * c)
    print(abs(S))

except ZeroDivisionError:
    print("Division by zero!")
