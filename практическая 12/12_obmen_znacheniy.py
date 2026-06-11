from random import randint as nigga

numbers = [nigga(1, 100) for _ in range(5)]

print(f'\nДо обмена - {numbers}')

min_index = numbers.index(min(numbers))
numbers[0], numbers[min_index] = numbers[min_index], numbers[0]

print(f'\nПосле обмена - {numbers}')