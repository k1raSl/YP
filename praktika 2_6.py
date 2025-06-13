1 скрипт

a = input("Введите строку: ")

words = a.split()
summ_str = sum(len(word) for word in words)

print("Сумма длин всех строк:", summ_str)



2 скрипт

numbers = list(map(int, input("Введите целочисленную последователность:").split()))

positive_numbers = []

for number in numbers:  
    if number > 0:  
        positive_numbers.append(number)  

print(positive_numbers)  



3 cкрипт

sequence = list(map(int, input("Введите последовательность чисел через пробел: ").split()))

result = [num for num in sequence if 10 <= num <= 99]

result.sort()

print("Положительные двузначные числа, отсортированные по возрастанию:", result)



скрипт 4

class FitnessCenter:
    def __init__(self, client_code, year, month, duration):
        self.client_code = client_code
        self.year = year
        self.month = month
        self.duration = duration

    def __str__(self):
        return f"Клиент: {self.client_code}, Год: {self.year}, Месяц: {self.month}, Продолжительность: {self.duration} мин."

    def __lt__(self, other):
        return self.duration < other.duration


fitness_sessions = [
    FitnessCenter("A001", 2023, 5, 60),
    FitnessCenter("B002", 2023, 6, 45),
    FitnessCenter("C003", 2023, 7, 90),
    FitnessCenter("D004", 2023, 8, 30),
    FitnessCenter("E005", 2023, 9, 120)
]

longest = max(fitness_sessions)
shortest = min(fitness_sessions)

print("Самое продолжительное занятие:")
print(longest)
print("\nСамое короткое занятие:")
print(shortest)



скрипт 5

class FitnessCenter:
    def __init__(self, client_code, year, month, duration):
        self.client_code = client_code  
        self.year = year                
        self.month = month              
        self.duration = duration        

    def __str__(self):
        return f"Клиент: {self.client_code}, Год: {self.year}, Месяц: {self.month}, Продолжительность: {self.duration} мин."

fitness_sessions = [
    FitnessCenter("A001", 2022, 5, 60),
    FitnessCenter("B002", 2022, 6, 45),
    FitnessCenter("C003", 2023, 7, 90),
    FitnessCenter("D004", 2023, 8, 30),
    FitnessCenter("E005", 2023, 9, 120),
    FitnessCenter("F006", 2023, 10, 60),
    FitnessCenter("G007", 2024, 1, 45),
    FitnessCenter("H008", 2024, 2, 90),
    FitnessCenter("I009", 2024, 3, 30),
    FitnessCenter("J010", 2024, 4, 120)
]

yearly_duration = {}

for session in fitness_sessions:
    if session.year in yearly_duration:
        yearly_duration[session.year] += session.duration
    else:
        yearly_duration[session.year] = session.duration

max_duration = max(yearly_duration.values())

max_years = [year for year, duration in yearly_duration.items() if duration == max_duration]

result_year = min(max_years)

print(f"Год с наибольшей суммарной продолжительностью занятий: {result_year}")
print(f"Суммарная продолжительность: {max_duration} мин.")

























скрипт 5
class FitnessCenter:
    def __init__(self, client_code, year, month, duration):
        self.client_code = client_code  
        self.year = year                
        self.month = month              
        self.duration = duration        

    def __str__(self):
        return f"Клиент: {self.client_code}, Год: {self.year}, Месяц: {self.month}, Продолжительность: {self.duration} мин."

fitness_sessions = [
    FitnessCenter("A001", 2022, 5, 60),
    FitnessCenter("B002", 2022, 6, 45),
    FitnessCenter("C003", 2023, 7, 90),
    FitnessCenter("D004", 2023, 8, 30),
    FitnessCenter("E005", 2023, 9, 120),
    FitnessCenter("F006", 2023, 10, 60),
    FitnessCenter("G007", 2024, 1, 45),
    FitnessCenter("H008", 2024, 2, 90),
    FitnessCenter("I009", 2024, 3, 30),
    FitnessCenter("J010", 2024, 4, 120)
]

yearly_duration = {}

for session in fitness_sessions:
    if session.year in yearly_duration:
        yearly_duration[session.year] += session.duration
    else:
        yearly_duration[session.year] = session.duration

max_duration = max(yearly_duration.values())
# Находим все годы с максимальной продолжительностью
max_years = [year for year, duration in yearly_duration.items() if duration == max_duration]
# Выбираем наименьший год из них
result_year = min(max_years)

print(f"Год с наибольшей суммарной продолжительностью занятий: {result_year}")
print(f"Суммарная продолжительность
