1 скрипт

names = [
    "Алексей", "Борис", "Анна", 
    "Дмитрий", "Алиса", "Сергей", 
    "Артём", "Мария", "Андрей", 
    "Елена"
]

print("Имена, начинающиеся на 'А':")
for name in names:
    if name.startswith('А') or name.startswith('A'):  
        print(name)



2 скрипт

class User:
    def __init__(self, login, password):
        self.Login = login
        self.Password = password

    def __str__(self):
        return f"Login: {self.Login}, Password: {self.Password}"


users = [
    User("admin", "qwerty123"),
    User("alice", "password1"),
    User("bob", "bob123"),
    User("john", "john2024"),
    User("emma", "emma555")
]

target_login = "bob"
target_password = "bob123"

found_user = None
for user in users:
    if user.Login == target_login and user.Password == target_password:
        found_user = user
        break

if found_user:
    print("Найден пользователь:")
    print(found_user)
else:
    print(f"Пользователь с логином '{target_login}' и паролем '{target_password}' не найден.")



3 скрипт

class Task:
    def __init__(self, date_start, date_finish, description):
        self.DateStart = date_start    # Дата начала (строка или datetime)
        self.DateFinish = date_finish  # Дата окончания (строка или datetime)
        self.Description = description # Описание занятия

    def __str__(self):
        return f"Начало: {self.DateStart}, Окончание: {self.DateFinish}, Описание: {self.Description}"


tasks = [
    Task("2023-10-01 09:00", "2023-10-01 10:30", "Лекция по Python"),
    Task("2023-10-01 10:00", "2023-10-01 12:00", "Практика по алгоритмам"),
    Task("2023-10-02 14:00", "2023-10-02 15:30", "Семинар по ООП"),
    Task("2023-10-03 11:00", "2023-10-03 13:00", "Встреча с командой"),
    Task("2023-10-01 12:00", "2023-10-01 14:00", "Разбор домашних заданий")
]

latest_task = tasks[0]

for task in tasks[1:]:  # Проверяем остальные занятия
    if task.DateFinish > latest_task.DateFinish:
        latest_task = task

print("Занятие, которое заканчивается позже всех:")
print(latest_task)



4 скрпит 

sequence = list(map(int, input().split()))

first_positive = next((x for x in sequence if x > 0), None)

last_negative = next((x for x in reversed(sequence) if x < 0), None)

print(f"Первый положительный: {first_positive}")
print(f"Последний отрицательный: {last_negative}")



5 скрпит

C = input("Введите символ C: ")  
A = input("Введите последовательность A через пробел: ").split()  

count = 0  

for element in A:
    if len(element) > 1 and element.startswith(C) and element.endswith(C):
        count += 1

print(f"Количество подходящих элементов: {count}")
