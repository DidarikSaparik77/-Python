balanc = 1000

while True:
    print('\n1. Узнать баланс', '2. Снять 100 руб', '3. Положить 100 руб', '4. Выход', sep = '\n')

    komanda = int(input('\nВведите команду 1, 2, 3 или 4: '))

    if komanda == 1:
        print(f'\nВаш баланс {balanc}')

    if komanda == 2:
        if balanc < 100:
            print('\nНедостаточно средств')
        else:
            balanc = balanc - 100
            print(f'\nСнято, ваш баланс - {balanc}')

    if komanda == 3:
        balanc = balanc + 100
        print(f'\nПополнено, ваш баланс - {balanc}')

    if komanda == 4:
        print('\nДо свидания!')
        break

    if komanda < 1 or komanda > 4:
        print('\nОшибка')           