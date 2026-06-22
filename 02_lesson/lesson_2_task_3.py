import math


def square(side):
    return math.ceil(side * side)


user_side = float(input("Введите длину стороны квадрата: "))
print(f"Площадь квадрата: {square(user_side)}")
