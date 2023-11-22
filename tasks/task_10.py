ALPHABETS: dict = {
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
    print("Некорректный режим")
else:
    if alph == 1:
        vowels: str = ALPHABETS["en_vowels"]
        consonants: str = ALPHABETS["en_consonants"]
        hints: str = "Введите букву латинского алфавита: "

    elif alph == 2:
        vowels: str = ALPHABETS["ru_vowels"]
        consonants: str = ALPHABETS["ru_consonants"]
        hints: str = "Введите букву кириллицы: "

    char: str = input(hints)

    if char in vowels:
        print(f"{char} - гласная буква!")
    elif char in consonants:
        print(f"{char} - согласная буква!")
    else:
        print("Упс! Неизвестная буква. Попробуйте другую!")
