class Student:
    def __init__(self, last_name, birth_date, group_number, grades):
        self.last_name = last_name
        self.birth_date = birth_date
        self.group_number = group_number
        self.grades = grades if len(grades) == 5 else [0] * 5

    def change_data(self, new_last_name=None, new_birth_date=None, new_group_number=None):
        if new_last_name: self.last_name = new_last_name
        if new_birth_date: self.birth_date = new_birth_date
        if new_group_number: self.group_number = new_group_number

    def __str__(self):
        return (f"Студент: {self.last_name}\n"
                f"Дата рождения: {self.birth_date}\n"
                f"Группа: {self.group_number}\n"
                f"Успеваемость: {self.grades}\n"
                f"Средний балл: {sum(self.grades) / 5:.1f}")

students = [
    Student("Антонов", "15.05.2000", "101", [4, 5, 4, 5, 4]),
    Student("Дмитрий", "12.11.2001", "102", [5, 5, 4, 5, 5]),
    Student("Александров", "03.03.2002", "101", [3, 4, 4, 3, 4])
]

print("=== Изменение данных студента ===")
print("До изменения:")
print(students[0])
students[0].change_data(new_last_name="Иванов-Петров", new_group_number="103")
print("\nПосле изменения:")
print(students[0])

print("\n=== Поиск студента ===")
search_name = input("Введите фамилию: ")
search_date = input("Введите дату рождения (дд.мм.гггг): ")

found = False
for student in students:
    if student.last_name == search_name and student.birth_date == search_date:
        print("\nНайден студент:")
        print(student)
        found = True
        break

if not found:
    print("\nСтудент не найден!")

print("\n=== Все студенты ===")
for student in students:
    print(student)
    print("-" * 30)
