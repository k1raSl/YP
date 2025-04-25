class MyClass:
    a = 0
    b = 0

    __init__ = lambda self, a=0, b=0: (setattr(self, 'a', a), setattr(self, 'b', b))
    __del__ = lambda self: print(f"Удален объект со значениями: {self.a}, {self.b}")

obj1 = MyClass()
print(f"Объект 1: a={obj1.a}, b={obj1.b}")

obj2 = MyClass(10, 20)
print(f"Объект 2: a={obj2.a}, b={obj2.b}")

obj1.a = 5
obj1.b = 15
print(f"Измененный объект 1: a={obj1.a}, b={obj1.b}")

del obj1
del obj2
