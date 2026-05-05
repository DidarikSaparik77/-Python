n = int(input('Введите число от 1 до 10: '))
if n > 10 or n < 1:
    print('Ошибка, введите число от 1 до 10: ')
else:
    for i in range(1, 11):
        print(f'{n} * {i} = {n * i}')
