pet_name: str = input("Введите имя своего питомца: ")

pet: str = "У вас классное имя для питомца!" \
    if pet_name == "Барсик" or pet_name == "Мурка" \
    else "Это тоже хорошее имя для питомца!"

print(pet)
