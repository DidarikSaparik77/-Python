m, n = int(input('Введите число m: ')), int(input('Введите число n: '))
if m < n:
    for i in range(m, n + 1):
        print(i)
elif m > n:
    for i in range(m, n - 1, -1):
        print(i)
else:
    (f'Чисчла равны')
