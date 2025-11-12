questions = [
    "Имя?",
    "Возраст?",
    "Город?",
    "Хобби?"
]

with open("anketa.txt", "w", encoding="utf-8") as f:
    for q in questions:
        a = input(q + " ")
        f.write(f"Вопрос: {q}\nОтвет: {a}\n\n")

print("Анкета сохранена в anketa.txt")