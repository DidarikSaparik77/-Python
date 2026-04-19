name = input('Введите ваше имя: ')
age = int(input('Введите ваш возраст: '))
favourite = list(input('Введите ваши любимые предметы через пробел: ').split())

print('=' * 50)
ank_stud = 'АНКЕТА СТУДЕНТА'
print(f'{ank_stud:^50}')
print('=' * 50)

print(f'Имя: {name}')
print(f'Возраст: {age}')
print(f'Любимые предметы: {favourite}')