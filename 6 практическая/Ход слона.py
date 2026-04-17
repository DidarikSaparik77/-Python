before_1, before_2, after_1, after_2 = int(input('введите первый параметр слона до хода ')), int(input('введите второй параметр слона до хода ')), int(input('введите первый параметр слона после хода ')), int(input('введите второй параметр слона после хода '))
if before_1 + before_2 == after_1 + after_2 or after_1 - before_1 == after_2 - before_2:
    print('YES')
else:
    print('NO')



