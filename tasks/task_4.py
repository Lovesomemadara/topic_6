num_1: int = int(input("Введите первое целое число: "))
num_2: int = int(input("Введите второе целое число: "))
num_3: int = int(input("Введите третье целое число: "))

if num_1 > num_2 and num_1 > num_3:
    print(f"Наибольшее число: {num_1}")
elif num_2 > num_1 and num_2 > num_3:
    print(f"Наибольшее число: {num_2}")
elif num_1 == num_2 == num_3:
    print(f"Все числа равны")
else:
    print(f"Наибольшее число: {num_3}")
