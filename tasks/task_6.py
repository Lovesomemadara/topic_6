year: int = int(input("Введите год: "))
month: int = int(input("Введите номер месяца: "))

if ((year % 4 == 0 and (year % 100 != 0 or year % 400 == 0))
        and ((month < 8 and month % 2 != 0)
             or (month >= 8 and month % 2 == 0))):
    print("Да")
else:
    print("Нет")
