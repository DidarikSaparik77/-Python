m, n = int(input('Введите число m: ')), int(input('Введите число n: '))
for i in range(m, n):
    if i == 17 or i % 10 == 9 or (i % 3 == 0 and i % 5 == 0):
        print(i)