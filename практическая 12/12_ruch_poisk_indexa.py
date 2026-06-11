x = int(input('Введите число: '))
numbers = [10, 20, 30, 40, 50]
print(numbers.index(x) if x in numbers else 'Нет такого числа')