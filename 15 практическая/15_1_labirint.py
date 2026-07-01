# Входная строка лабиринта (пример)
# 0 0 0 0 0
# 0 1 1 1 0
# 0 н м 1 0
# 0 1 ф 1 0
# 0 0 0 0 0
labirint = "00000111000нм1001ф100000"

def print_labirint(labirint_str):
    """Задание 1.1: Вывести лабиринт в виде 5 строк по 5 символов"""
    print("Задание 1.1: Лабиринт")
    for i in range(0, 25, 5):
        print(labirint_str[i:i+5])
    print()

def find_coordinates(labirint_str, symbol):
    """Найти координаты символа в лабиринте"""
    index = labirint_str.find(symbol)
    if index == -1:
        return -1, -1  # возвращаем -1, если символ не найден
    row = index // 5
    col = index % 5
    return row, col

def task_1_2(labirint_str):
    """Задание 1.2: Найти координаты входа"""
    row, col = find_coordinates(labirint_str, 'н')
    if row == -1 and col == -1:
        print("Задание 1.2: Вход (н) не найден в лабиринте")
    else:
        print(f"Задание 1.2: Координаты входа (н): строка {row}, столбец {col}")
    return row, col

def task_1_3(labirint_str):
    """Задание 1.3: Найти координаты выхода"""
    row, col = find_coordinates(labirint_str, 'ф')
    if row == -1 and col == -1:
        print("Задание 1.3: Выход (ф) не найден в лабиринте")
    else:
        print(f"Задание 1.3: Координаты выхода (ф): строка {row}, столбец {col}")
    return row, col

def task_1_4(entry_row, entry_col, exit_row, exit_col):
    """Задание 1.4: Вычислить Манхэттенское расстояние"""
    if entry_row == -1 or exit_row == -1:
        print("Задание 1.4: Невозможно вычислить расстояние - вход или выход не найдены")
        return 0
    distance = abs(entry_row - exit_row) + abs(entry_col - exit_col)
    print(f"Задание 1.4: Манхэттенское расстояние между входом и выходом: {distance} шагов")
    return distance

def task_1_5(labirint_str):
    """Задание 1.5: Подсчитать количество монет"""
    count = labirint_str.count('м')
    print(f"Задание 1.5: Количество монет: {count}")
    if count == 0:
        print("🟡x0 (монет нет)")
    else:
        print(f"🟡x{count} или {'🟡' * count}")
    return count

def task_1_6(labirint_str):
    """Задание 1.6: Подсчитать оставшееся здоровье"""
    initial_hp = 100
    traps = labirint_str.count('л') * 10
    enemies = labirint_str.count('з') * 50
    total_damage = traps + enemies
    remaining_hp = initial_hp - total_damage
    
    # Если здоровье упало ниже 0, устанавливаем 0
    if remaining_hp < 0:
        remaining_hp = 0
    
    hearts = remaining_hp // 10
    empty_hearts = (initial_hp - remaining_hp) // 10
    
    print(f"Задание 1.6: Оставшееся здоровье: {remaining_hp} HP")
    if remaining_hp == 0:
        print("💀 Игрок погиб!")
    else:
        print(f"♥ * {hearts} + ♡ * {empty_hearts}")
        print("♥" * hearts + "♡" * empty_hearts)
    return remaining_hp

def task_1_7(labirint_str):
    """Задание 1.7: Заменить символы на эмодзи"""
    emoji_map = {
        '0': '⬜',
        '1': '⬛',
        'л': '🔷',
        'м': '🟡',
        'ф': '🟫',
        'з': '🐷',
        'н': '⭐'
    }
    
    print("Задание 1.7: Лабиринт в эмодзи")
    for i in range(0, 25, 5):
        row = labirint_str[i:i+5]
        emoji_row = ''.join(emoji_map.get(char, char) for char in row)
        print(emoji_row)

# Выполнение всех заданий
print("=" * 50)
print("РЕШЕНИЕ ЗАДАЧИ 'ЛАБИРИНТ'")
print("=" * 50)

# Задание 1.1
print_labirint(labirint)

# Задание 1.2
entry_row, entry_col = task_1_2(labirint)

# Задание 1.3
exit_row, exit_col = task_1_3(labirint)

# Задание 1.4
task_1_4(entry_row, entry_col, exit_row, exit_col)

# Задание 1.5
task_1_5(labirint)

# Задание 1.6
task_1_6(labirint)

# Задание 1.7
print()
task_1_7(labirint)