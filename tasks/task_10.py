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

match alph:
    case 1:
        char: str = input("Введите букву латинского алфавита: ")
        if char in ALPHABETS['en_vowels']:
            print(f"{char} - гласная буква!")
        elif char in ALPHABETS['ru_vowels'] \
                or char in ALPHABETS['ru_consonants']:
            print("Упс! Неизвестная буква. Попробуйте другую!")
        else:
            print(f"{char} -  согласная буква!")
    case 2:
        char: str = input("Введите букву кириллицы: ")
        if char in ALPHABETS['ru_vowels']:
            print(f"{char} - гласная буква!")
        elif char in ALPHABETS['en_vowels'] \
                or char in ALPHABETS['en_consonants']:
            print("Упс! Неизвестная буква. Попробуйте другую!")
        else:
            print(f"{char} -  согласная буква!")
    case _:
        print("Упс! Выбран неверный режим. Попробуйте ещё раз ...")
