pkt = int(input('Введите номер кармана '))
if pkt == 0: print('зеленый')
elif 1 <= pkt <= 10:
    if pkt % 2 == 0: print('черный')
    else: print('красный')
elif 11 <= pkt <= 18:
    if pkt % 2 == 0: print('красный')
    else: print('черный')
elif 19 <= pkt <= 28:
    if pkt % 2 == 0: print('черный')
    else: print('красный')
elif 29 <= pkt <= 36:
    if pkt % 2 == 0: print('красный')
    else: print('черный')
else: print('вне диапозона')

