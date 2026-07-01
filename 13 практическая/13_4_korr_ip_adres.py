ip_adres = list(map(int, (input('Введите корректный IP_адрес: ')).split('.')))
if len(ip_adres) == 4:
    for i in ip_adres:
        if 0 <= i <= 225:
            continue
        print('NO')
        break
    else:
        print('YES')