class Counter:
    __value = 0

    def __init__(self, value=0):
        self.__value = value

    def __add__(self, other):
        self.__value += 1
        return self

    def __sub__(self, other):
        self.__value -= 1
        return self

    def __str__(self):
        return str(self.__value)

    value = property(lambda self: self.__value)

c = Counter()
print("Начальное значение:", c)  

c + 1  
c + 1  
print("После +2:", c)

c - 1  
print("После -1:", c)  

c2 = Counter(5)
print("\nСчетчик c2:", c2)  
c2 - 1
print("После -1:", c2)  
