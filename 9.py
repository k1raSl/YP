class Worker:
    def __init__(self, name='', surname='', rate=0, days=0):
        self.name = name
        self.surname = surname
        self.rate = rate
        self.days = days

    GetSalary = lambda self: self.rate * self.days

worker1 = Worker('Иван', 'Иванов', 1000, 20)
worker2 = Worker('Петр', 'Петров', 1500, 15)

print(f"{worker1.name} {worker1.surname}: зарплата = {worker1.GetSalary()} руб.")
print(f"{worker2.name} {worker2.surname}: зарплата = {worker2.GetSalary()} руб.")

worker1.days = 25
worker2.rate = 2000

print("\nПосле изменений:")
print(f"{worker1.name} {worker1.surname}: новая зарплата = {worker1.GetSalary()} руб.")
print(f"{worker2.name} {worker2.surname}: новая зарплата = {worker2.GetSalary()} руб.")
