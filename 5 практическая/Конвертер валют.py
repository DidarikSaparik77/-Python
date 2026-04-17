USD_TO_RUB = 75.85

def convert_usd_to_rub(amount_usd):
    """
    Конвертирует сумму из долларов США в рубли.

    Параметры:
        amount_usd (float): Сумма в долларах.

    Возвращает:
        float: Сумма в рублях, округлённая до двух знаков после запятой.
    """
    amount_rub = amount_usd * USD_TO_RUB
    return round(amount_rub, 2)

amount_usd = float(input('Введите сумму в долларах: '))
amount_rub = convert_usd_to_rub(amount_usd)
print(f'{amount_usd} USD = {amount_rub} RUB')
