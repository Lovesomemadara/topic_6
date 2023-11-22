num: int = int(input("Введите целое число: "))
fl_num: float = float(input("Введите дробное число: "))
stroke: str = input("Введите строку: ")

'''if num == 0 or fl_num == 0 or stroke == '':
    print("Нет")
else:
    print("Да")'''

'''if all(num):
    print("Нет")
elif not fl_num:
    print("Нет")
elif not stroke:
    print("Нет")
else:
    print("Да")'''

# Использовать встроенную функцию

# -----------------match-case------------------
yeah_tuple: tuple = (num, fl_num, stroke)
false_tuple: bool = all(yeah_tuple)

match yeah_tuple:
    case _ if false_tuple:
        print("Да")
    case _:
        print("Нет")
