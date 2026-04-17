a = int(input('Введите сторону a: '))
b = int(input('Введите сторону b: '))
c = int(input('Введите сторону c: '))

if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print('Равносторонний')
    elif a == b or a == c or b == c:
        print('Равнобедренный')
    else:
        print('Разносторонний')
else:
    print('Треугольник не существует')