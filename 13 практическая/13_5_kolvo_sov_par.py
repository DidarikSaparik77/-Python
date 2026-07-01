stroka = input('Введите числа через пробел: ').split()

counter = 0

for i in range(len(stroka)):
    for j in range(i + 1, len(stroka)):
        if stroka[i] == stroka[j]:
            counter += 1

print(f'Количество пар в вашей строке: {counter}')

