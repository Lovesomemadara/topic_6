num: int = int(input("Введите целое число: "))

'''if num > 0:
    print(1)
elif num == 0:
    print(0)
else:
    print(-1)'''

result: int = 1 if num > 0 else 0 if num == 0 else -1

print(result)
