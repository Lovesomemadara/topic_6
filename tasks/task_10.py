ALPHABETS = {
    "en_vowels": "AEIOU",
    "en_consonants": "BCDFGHJKLMNPQRSTVWXYZ",
    "ru_vowels": "АЕЁИОУЫЭЮЯ",
    "ru_consonants": "БВГДЖЗЙКЛМНПРСТФХЦЧШЩЪЬ",
}

print("Добро пожаловать в программу \"Буква-Детектив\"!", end="\n\n")

print("Выберите алфавит: \n"
      "1. Латинский\n"
      "2. Кириллица")

alph: int = int(input("Введите номер алфавита: "))

if alph not in (1, 2):
    print("Упс! Выбран неверный режим. Попробуйте ещё раз ...")
else:
    char: str = input("Введите букву: ")
    if alph == 1:
        if (char not in ALPHABETS['en_vowels']
                and char not in ALPHABETS['en_consonants']):
            print("Упс! Неизвестная буква. Попробуйте другую!")
        else:
            if char in ALPHABETS['en_vowels']:
                print(f"{char} - гласная буква!")
            elif char in ALPHABETS['en_consonants']:
                print(f"{char} -  согласная буква!")
    elif alph == 2:
        if (char not in ALPHABETS['ru_vowels']
                and char not in ALPHABETS['ru_consonants']):
            print("Упс! Неизвестная буква. Попробуйте другую!")
        else:
            if char in ALPHABETS['ru_vowels']:
                print(f"{char} - гласная буква!")
            elif char in ALPHABETS['ru_consonants']:
                print(f"{char} -  согласная буква!")
