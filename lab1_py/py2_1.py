
A = int(input("Введите число A: "))
B = int(input("Введите число B: "))
C = int(input("Введите число C: "))


is_between = (A < B < C) or (C < B < A)


print(f"Число B находится между числами A и C: {is_between}")
