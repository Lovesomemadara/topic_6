num_1: int = int(input("Введите первое число: "))
num_2: int = int(input("Введите второе число: "))
operation: str = input("Введите магическую операцию: ")

match operation:
    case "Призыв":
        print("Сумма магических чисел равна:", num_1 + num_2)
    case "Трансформация":
        print("Трансформированное число:", (num_1 * -1) + num_2)
    case "Объединение":
        print("Произведение магических числе равно:", num_1 * num_2)
    case "Исчезновение":
        if num_2 != 0:
            print("Исчезнувшее число:", num_1 == 0, "\n", num_2)
        else:
            print("Ошибка: Второе число равно нулю!")
    case _:
        print("Ошибка: Некорректная операция")
