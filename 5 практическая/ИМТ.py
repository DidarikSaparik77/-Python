weight, height = map(float, input("Введите ваш вес (кг) и рост (м) через пробел: ").split())

imt = weight / (height * height)

print(f'Ваш индекс массы тела: {imt:.1f}')