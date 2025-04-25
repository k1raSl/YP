J = str(input("Введите колиичество драгоценностей: "))
S = str(input("Введите количество камней: "))

jewels = set(J)
count = 0
for stone in S:
    if stone in jewels:
        count += 1

print("Количество драгоценных камней в S:", count)
