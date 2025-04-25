class Train:
    def __init__(self, destination, number, departure_time):
        self.destination = destination
        self.number = number
        self.departure_time = departure_time

    def __str__(self):
        return f"Поезд №{self.number} в {self.destination}, отправление в {self.departure_time}"


# Создаем список поездов
trains = [
    Train("Севастополь", "123А", "06:00"),
    Train("Ялта", "456Б", "8:30"),
    Train("Крым", "789В", "15:15"),
    Train("Москву", "321Г", "23:45")
]

print("=== Список всех поездов ===")
for train in trains:
    print(train)

print("\n=== Поиск поезда по номеру ===")
search_number = input("Введите номер поезда: ")

found = False
for train in trains:
    if train.number == search_number:
        print("\nНайден поезд:")
        print(train)
        found = True
        break

if not found:
    print("\nПоезд с таким номером не найден!")

print("\n=== Изменение данных поезда ===")
trains[0].destination = "Москва (Ленинградский вокзал)"
trains[0].departure_time = "09:00"
print("После изменения:")
print(trains[0])
