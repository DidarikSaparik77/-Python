nominaly = [5000, 2000, 1000, 500, 200, 100]

summa = int(input("Введите сумму для снятия (кратную 100): "))

if summa % 100 != 0:
    print("Ошибка! Сумма должна быть кратной 100.")
else:
    
    summa1 = summa

    for nominal in nominaly:
        count = summa1 // nominal

        if count > 0:
            print(f'{nominal} : {count} шт. = {nominal * count}')
            summa1 -= nominal * count
    
    print(f"ИТОГО ВЫДАНО: {summa}")