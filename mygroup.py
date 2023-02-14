groupmates = [
    {
        "name": "Кирилл",
        "surname": "Клестов",
        "exams": ["Информатика", "ЭЭиС", "Web"],
        "marks": [4, 4, 5]
    },
    {
        "name": "Ирина",
        "surname": "Смирнова",
        "exams": ["История", "АиГ", "КТП"],
        "marks": [5, 4, 4]
    },
    {
        "name": "Анастасия",
        "surname": "Груздева",
        "exams": ["Философия", "ИС", "КТП"],
        "marks": [5, 5, 5]
    }
]


def print_students(students):
    mark = int(input("Введите оценку: "))
    if mark > 0:
        print(u"Имя".ljust(15), u"Фамилия".ljust(10), u"Экзамены".ljust(35), u"Оценки".ljust(15))
        for student in students:
            if sum(student["marks"])/len(student["marks"]) > mark:
                print(student["name"].ljust(15), student["surname"].ljust(10), str(student["exams"]).ljust(35), str(student["marks"]).ljust(15))

print_students(groupmates)