import math

d = float(input("Введите диаметр окружности: "))
L = math.pi * d
R = d / 2
S = math.pi * (R ** 2)

print(f"Длина окружности: {L}")
print(f"Радиус окружности: {R}")
print(f"Площадь круга: {S}")
