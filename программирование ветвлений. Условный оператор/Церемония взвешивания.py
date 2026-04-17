weight = int(input('введите ваш вес'))
if weight < 60:
    print('Легкий вес')
elif 60 <= weight < 64:
    print('Первый полусредний вес')
elif 64 <= weight < 69:
    print('Полусредний вес')
else:
    print('вы не подходите для бокса')