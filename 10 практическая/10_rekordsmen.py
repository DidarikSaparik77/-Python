max_nummber = 0

while True:
    number = int(input('Введите число: '))
    if number == 0:
        break
    if number > max_nummber:
        max_nummber = number

print(f'Максимальное число  - {max_nummber}')