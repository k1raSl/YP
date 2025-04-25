import sqlite3

conn = sqlite3.connect('bar.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS drinks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    alcohol_percent REAL NOT NULL,
    volume INTEGER NOT NULL,
    price REAL NOT NULL,
    quantity INTEGER NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS ingredients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    quantity INTEGER NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS cocktails (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price REAL NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS cocktail_components (
    cocktail_id INTEGER,
    drink_id INTEGER,
    amount INTEGER,
    FOREIGN KEY(cocktail_id) REFERENCES cocktails(id),
    FOREIGN KEY(drink_id) REFERENCES drinks(id)
)
''')

conn.commit()

while True:
    print("\n=== I Love Drink ===")
    print("1. Управление напитками")
    print("2. Управление ингредиентами")
    print("3. Управление коктейлями")
    print("4. Операции продажи")
    print("5. Пополнение запасов")
    print("6. Просмотр остатков")
    print("0. Выход")

    main_choice = input("Выберите раздел: ")

    if main_choice == '1':
        while True:
            print("\n--- Управление напитками ---")
            print("1. Добавить напиток")
            print("2. Просмотреть все напитки")
            print("3. Назад")

            choice = input("Выберите действие: ")

            if choice == '1':
                name = input("Название напитка: ")
                alcohol = float(input("Процент алкоголя: "))
                volume = int(input("Объем (мл): "))
                price = float(input("Цена: "))
                quantity = int(input("Количество: "))

                cursor.execute('''
                INSERT INTO drinks (name
