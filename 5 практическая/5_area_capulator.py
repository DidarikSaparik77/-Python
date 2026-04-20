def calculate_rectangle_area(width, height):
    return width * height

def calculate_circle_area(radius):
    pi = 3.14159
    return pi * radius * radius


width, height = float(input('Введите ширину прямоугольника: ')), int(input('Введите высоту прямоугольника: '))

rectangle_area = calculate_rectangle_area(width, height)
print(f'Плошадь вашего прямоугольника равна: {rectangle_area}')


radius = float(input('Введите ваш радиус: '))

circle_area = calculate_circle_area(radius)
print(f'Площадь вшего круга равна: {circle_area}')