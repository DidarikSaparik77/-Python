before_1, before_2, after_1, after_2 = int(input('Введите первое значение ферзя до хода ')), int(input('Введите первое значение ферзя до хода ')), int(input('Введите первое значение ферзя после хода ')), int(input('Введите второе значение ферзя после хода '))
if before_1 + before_2 == after_1 + after_2 or after_1 - before_1 == after_2 - before_2 or before_1 == after_1 or before_2 == after_2:
    print('YES')
else:
    print('NO')








