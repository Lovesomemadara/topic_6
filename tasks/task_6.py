year: int = int(input("Введите год: "))
month: int = int(input("Введите номер месяца: "))

is_leap_year: bool = year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
until_august: bool = month < 8 and month % 2 != 0
after_august: bool = month >= 8 and month % 2 == 0
'''max_days: bool = ((month < 8 and month % 2 != 0)
                  or (month >= 8 and month % 2 == 0))'''

'''if is_leap_year and month:
    print("Да")
else:
    print("Нет")'''

# -----------------match-case------------------

match year, month:
    case _ if ((is_leap_year == True)
               and ((until_august or after_august) == True)):
        print("Да")
    case _:
        print("Нет")
