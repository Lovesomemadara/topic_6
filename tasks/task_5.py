num: int = int(input("Введите целое число: "))

if num % 2 == 0:
    print(f"Число {num} является четным")
elif num % 2 != 0 and num * 3 > 20:
    print(f"Результат умножения {num} на 3 больше 20")
else:
    print(f"Число {num} не соответствует условиям")
