temperatura, davlenie, puls = int(input('Введите вашу температуру ')), int(input('Введите ваше давление ')), int(input('Введите ваш пульс '))
if 36 <= temperatura <= 37 and 110 <= davlenie <= 130 and 60 <= puls <= 100:
    print('Нормальное состояние')
elif (35 <= temperatura <= 36 or 37 <= temperatura <= 38) or (105 <= davlenie <= 110 or 130 <= davlenie <= 140) or (55 <= puls <= 60 or 100 <= puls <= 110):
    print('Легкое недомогание')
elif (temperatura < 35 or temperatura > 38) or (davlenie < 105 or davlenie > 140) or (puls < 55 or puls > 110):
    print('Требуется врач')