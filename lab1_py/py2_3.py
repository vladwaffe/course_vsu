import math

def f(x, a, b, c):
    if a < 0 and c != 0:
        return (a**2 + b*x + c) / x
    elif a > 0 and c == 0:
        return -a / (x - c)
    else:
        return a * (math.exp(x) - c)


a = float(input("Введите значение a: "))
b = float(input("Введите значение b: "))
c = float(input("Введите значение c: "))
x = float(input("Введите значение x: "))

result = f(x, a, b, c)
print(f"f({x}) = {result}")
