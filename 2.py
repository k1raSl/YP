target = int(input("Нужная сумма: "))
input_str = input("Введите числа через пробел: ")

numbers = list(map(int, input_str.split()))

result = []
numbers.sort()

for i in range(len(numbers)):
    if i > 0 and numbers[i] == numbers[i - 1]:
        continue

    first = numbers[i]
    if first > target:
        continue

    for j in range(i + 1, len(numbers)):
        if j > i + 1 and numbers[j] == numbers[j - 1]:
            continue

        second = numbers[j]
        if first + second > target:
            break

        for k in range(j + 1, len(numbers)):
            if k > j + 1 and numbers[k] == numbers[k - 1]:
                continue

            third = numbers[k]
            total = first + second + third

            if total == target:
                combo = [first, second, third]
                if combo not in result:
                    result.append(combo)
            elif total > target:
                break

    if first in numbers[i + 1:]:
        if first * 2 == target:
            combo = [first, first]
            if combo not in result:
                result.append(combo)

    if first == target and [first] not in result:
        result.append([first])

print("Найденные комбинации:", result)
