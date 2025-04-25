numbers = [10, 1, 2, 7, 6, 1, 5]  # Данные числа
target = 8  # Нужная сумма
numbers.sort()  # Сортируем для удобства
result = []  # Сюда будем записывать ответы

# Перебираем все возможные комбинации
for i in range(len(numbers)):
    # Пропускаем повторяющиеся числа
    if i > 0 and numbers[i] == numbers[i - 1]:
        continue

    # Первое число в комбинации
    first = numbers[i]
    if first > target:
        continue

    # Ищем второе число
    for j in range(i + 1, len(numbers)):
        # Пропускаем повторы
        if j > i + 1 and numbers[j] == numbers[j - 1]:
            continue

        # Второе число
        second = numbers[j]
        if first + second > target:
            break

        # Ищем третье число
        for k in range(j + 1, len(numbers)):
            # Пропускаем повторы
            if k > j + 1 and numbers[k] == numbers[k - 1]:
                continue

            # Третье число
            third = numbers[k]
            total = first + second + third

            if total == target:
                combo = [first, second, third]
                if combo not in result:
                    result.append(combo)
            elif total > target:
                break

    # Проверяем пары (комбинации из 2 чисел)
    if first in numbers[i + 1:]:
        if first * 2 == target:
            combo = [first, first]
            if combo not in result:
                result.append(combo)

    # Проверяем одиночные числа
    if first == target and [first] not in result:
        result.append([first])

# Выводим результат
print("Найденные комбинации:", result)