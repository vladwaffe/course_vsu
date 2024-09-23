
orientations = ['С', 'З', 'Ю', 'В']  # С - Север, З - Запад, Ю - Юг, В - Восток

initial_orientation = input("Введите исходную ориентацию локатора (С, З, Ю, В): ")

if initial_orientation not in orientations:
    print(f"Ошибка: '{initial_orientation}' не является допустимой ориентацией.")
else:

    index = orientations.index(initial_orientation)


    M1 = int(input("Введите первую команду поворота (1, -1, 2): "))
    M2 = int(input("Введите вторую команду поворота (1, -1, 2): "))
    commands = [M1, M2]


    for command in commands:
        if command == 1:
            index = (index + 1) % 4
        elif command == -1:
            index = (index - 1) % 4
        elif command == 2:
            index = (index + 2) % 4

    new_orientation = orientations[index]

    print(f"Новая ориентация локатора: {new_orientation}")
