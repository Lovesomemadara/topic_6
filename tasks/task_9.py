num: int = int(input("Введите целое число: "))
fl_num: float = float(input("Введите дробное число: "))
stroke: str = input("Введите строку: ")

'''if num:
    print("Да")
elif fl_num:
    print("Да")
elif stroke:
    print("Да")
else:
    print("Нет")'''

# -----------------match-case------------------

yeah_tuple: tuple = (num, fl_num, stroke)
false_tuple: bool = any(yeah_tuple)

match yeah_tuple:
    case _ if false_tuple == True:
        print("Да")
    case _:
        print("Нет")
