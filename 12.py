class Student:
    def __init__(self, first_name, last_name, middle_name, group, grades):
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.group = group
        self.grades = grades

    @property
    def average(self):
        return sum(self.grades) / len(self.grades)


students = []


def show_menu():
    print("\n1. Добавить студента")
    print("2. Показать всех студентов")
    print("3. Найти студента")
    print("4. Изменить данные студента")
    print("5. Удалить студента")
    print("6. Средний балл группы")
    print("0. Выход")


def add_student():
    print("\nДобавление нового студента:")
    first = input("Имя: ")
    last = input("Фамилия: ")
    middle = input("Отчество: ")
    group = input("Группа: ")
    grades = [
        int(input("Оценка 1: ")),
        int(input("Оценка 2: ")),
        int(input("Оценка 3: ")),
        int(input("Оценка 4: "))
    ]
    students.append(Student(first, last, middle, group, grades))
    print("Студент добавлен!")


def show_all():
    print("\nСписок всех студентов:")
    for i, student in enumerate(students, 1):
        print(f"{i}. {student.last_name} {student.first_name} {student.middle_name} ({student.group})")


def find_student():
    last = input("\nВведите фамилию: ")
    found = [s for s in students if s.last_name.lower() == last.lower()]

    if not found:
        print("Студент не найден!")
        return

    for student in found:
        print(f"\n{student.last_name} {student.first_name} {student.middle_name}")
        print(f"Группа: {student.group}")
        print(f"Оценки: {student.grades}")
        print(f"Средний балл: {student.average:.2f}")


def update_student():
    show_all()
    try:
        num = int(input("\nВведите номер студента: ")) - 1
        if 0 <= num < len(students):
            student = students[num]
            student.first_name = input(f"Имя ({student.first_name}): ") or student.first_name
            student.last_name = input(f"Фамилия ({student.last_name}): ") or student.last_name
            student.middle_name = input(f"Отчество ({student.middle_name}): ") or student.middle_name
            student.group = input(f"Группа ({student.group}): ") or student.group
            print("Оценки (оставьте пусто для сохранения):")
            for i in range(4):
                new_grade = input(f"Оценка {i + 1} ({student.grades[i]}): ")
                if new_grade:
                    student.grades[i] = int(new_grade)
            print("Данные обновлены!")
        else:
            print("Неверный номер!")
    except:
        print("Ошибка ввода!")


def delete_student():
    show_all()
    try:
        num = int(input("\nВведите номер студента: ")) - 1
        if 0 <= num < len(students):
            del students[num]
            print("Студент удален!")
        else:
            print("Неверный номер!")
    except:
        print("Ошибка ввода!")


def group_average():
    group = input("\nВведите название группы: ")
    group_students = [s for s in students if s.group.lower() == group.lower()]

    if not group_students:
        print("В этой группе нет студентов!")
        return

    avg = sum(s.average for s in group_students) / len(group_students)
    print(f"Средний балл группы {group}: {avg:.2f}")


while True:
    show_menu()
    choice = input("Выберите действие: ")

    if choice == '1':
        add_student()
    elif choice == '2':
        show_all()
    elif choice == '3':
        find_student()
    elif choice == '4':
        update_student()
    elif choice == '5':
        delete_student()
    elif choice == '6':
        group_average()
    elif choice == '0':
        break
    else:
        print("Неверный ввод!")
