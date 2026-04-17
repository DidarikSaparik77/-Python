# Определение сезона по номеру месяца

month = int(input("Введите номер месяца (1-12): "))

match month:
    case 12 | 1 | 2:
        season = "зима❄️"
    case 3 | 4 | 5:
        season = "весна🌸"
    case 6 | 7 | 8:
        season = "лето☀️"
    case 9 | 10 | 11:
        season = "осень🍂"
    case _:
        print("Ошибка: введите число от 1 до 12.")
        
if 0 < month < 13:
    print(f"Месяц: {month} Сезон: {season}")