import math


rho = float(input("Введите плотность материала (ρ): "))
h = float(input("Введите толщину диска (h): "))
m = float(input("Введите массу диска (m): "))

R = math.sqrt(m / (math.pi * rho * h))

print(f"Радиус диска: {R}")
