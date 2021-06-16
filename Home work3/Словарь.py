eng_to_rus = {
    "dog": "собака",
    "cat": "кошка",
    "book": "книга",
    "table": "стол",
    "continue": "продолжить",
    "simple": "простой"
}
rus_to_eng = {
    "собака": "dog",
    "кошка": "cat",
    "книга": "book",
    "стол": "table",
    "продолжить": "continue",
    "простой": "simple"
}
kg_to_uz ={
    "Салам": "Хайр",
    "Кандайсын": "Калайсиз"
}
uz_to_kg ={
    "Хайр": "Салам",
    "Калайсиз": "Кандайсын"
}
while True:
    lang = input("Язык для перевода: ")
    if lang == "eng":
        word = input("Слово для перевода: ")
        try:
            print(eng_to_rus[word])
        except KeyError:
            print("Слова нету в словаре, хотите добавить? ")
            option = input()
            if option == "y":
                eng_to_rus[word] = input(f"Перевод для слова " + word)

    if lang == "rus":
        word = input("Слово для перевода: ")
        try:
            print("Слова нету в словаре, хотите добавить? ")
            option = input()
            if option == "y":
                rus_to_eng[word] = input(f"Перевод для слова " + word)
        except KeyError:
            print("Cлова нету в словаре")

    lang = input("Язык для перевода: ")
    if lang == "kg":
        word = input("Слово для перевода: ")
        try:
            print(kg_to_uz[word])
        except KeyError:
            print("Слова нету в словаре, хотите добавить? ")
            option = input()
            if option == "y":
                kg_to_uz[word] = input(f"Перевод для слова " + word)

    if lang == "uz":
        word = input("Слово для перевода: ")
        try:
            print("Слова нету в словаре, хотите добавить? ")
            option = input()
            if option == "y":
                uz_to_kg[word] = input(f"Перевод для слова " + word)
        except KeyError:
            print("Cлова нету в словаре")