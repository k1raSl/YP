class Worker:
    def __init__(self, name='', surname='', rate=0, days=0):
        self.__name = name
        self.__surname = surname
        self.__rate = rate
        self.__days = days

    GetName = property(lambda self: self.__name)
    GetSurname = property(lambda self: self.__surname)
    GetRate = property(lambda self: self.__rate)
    GetDays = property(lambda self: self.__days)

    GetSalary = lambda self: self.__rate * self.__days

worker = Worker('Сергей', 'Сергеев', 1500, 20)

print("Данные работника:")
print(f"Имя: {worker.GetName}")
print(f"Фамилия: {worker.GetSurname}")
print(f"Ставка: {worker.GetRate} руб/день")
print(f"Отработано дней: {worker.GetDays}")
print(f"Зарплата: {worker.GetSalary()} руб.")

worker.__name = "Петр"
print("\nПосле попытки изменения напрямую:")
print(f"Имя (через геттер): {worker.GetName}")
