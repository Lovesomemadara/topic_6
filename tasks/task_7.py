num: int = int(input("Введите целое число: "))
fl_num: float = float(input("Введите дробное число: "))
stroke: str = input("Введите строку: ")

'''if num == 0 or fl_num == 0 or stroke == '':
    print("Нет")
else:
    print("Да")'''

if not num:
    print("Нет")
elif not fl_num:
    print("Нет")
elif not stroke:
    print("Нет")
else:
    print("Да")
