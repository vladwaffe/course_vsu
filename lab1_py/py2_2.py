number = int(input("Введите целое число: "))

if number == 0:
    description = "нулевое число"
elif number > 0:
    if number % 2 == 0:
        description = "положительное чётное число"
    else:
        description = "положительное нечётное число"
else:
    if number % 2 == 0:
        description = "отрицательное чётное число"
    else:
        description = "отрицательное нечётное число"


print(description)
