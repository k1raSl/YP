nums = input("Введите числа: ")

numbers = list(map(int, nums.split()))

print(len(nums) != len(set(nums)))
