total_summ = 0

while True:
    cena_tovara = int(input('Введите цену товара: '))

    if cena_tovara == 0:
        break

    if cena_tovara < 0:
        print('Ошибка цены')
        continue

    total_summ += cena_tovara

if total_summ >= 1000:
    total_summ = total_summ - total_summ * 0.1

print(total_summ)
