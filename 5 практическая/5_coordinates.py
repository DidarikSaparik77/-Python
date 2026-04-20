from math import *

def calculate_distance(x1, y1, x2, y2):
    distance = sqrt(pow((x2 - x1), 2) + pow((y2 - y1), 2))
    return distance

def calculate_triangle_area(a, b, c):
    p = (a + b + c) / 2
    area = sqrt(p * (p - a) * (p - b) * (p - c))
    return area

x1 = float(input('Введите коордиданты точки A x1 = '))
y1 = float(input('Введите коордиданты точки A y1 = '))
x2 = float(input('Введите коордиданты точки B x2 = '))
y2 = float(input('Введите коордиданты точки B y2 = '))
x3 = float(input('Введите коордиданты точки C x3 = '))
y3 = float(input('Введите коордиданты точки C y3 = '))

side_ab = calculate_distance(x1, y1, x2, y2)
print(f"Сторона AB = {side_ab:.2f}")

side_bc = calculate_distance(x2, y2, x3, y3)
print(f"Сторона BC = {side_bc:.2f}")

side_ca = calculate_distance(x3, y3, x1, y1)
print(f"Сторона CA = {side_ca:.2f}")

area = calculate_triangle_area(side_ab, side_bc, side_ca)

print(f"Площадь треугольника = {area:.2f} квадратных единиц")