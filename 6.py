class Numbers:
    a = 0
    b = 0

nums = Numbers()

nums.a = int(input("Введите первое число: "))
nums.b = int(input("Введите второе число: "))

print("\nРезультаты:")
print(f"Введенные числа: {nums.a} и {nums.b}")
print(f"Сумма чисел: {nums.a + nums.b}")
print(f"Максимальное число: {nums.a if nums.a > nums.b else nums.b}")

print("\nИзменение чисел:")
nums.a = int(input("Введите новое первое число: "))
nums.b = int(input("Введите новое второе число: "))

print("\nОбновленные результаты:")
print(f"Числа: {nums.a} и {nums.b}")
print(f"Сумма: {nums.a + nums.b}")
print(f"Максимальное: {max(nums.a, nums.b)}")
