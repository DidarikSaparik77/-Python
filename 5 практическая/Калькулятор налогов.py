NALOG_STAVKA = 0.13

godovoy_dohod = float(input('Введите ваш годовой доход: '))

nalog_summa = godovoy_dohod * NALOG_STAVKA 
dohod_posle_naloga = godovoy_dohod - nalog_summa 

formatted_dohod = f"{godovoy_dohod:,.2f}".replace(',', ' ')
formatted_nalog = f"{nalog_summa:,.2f}".replace(',', ' ')
formated_posle_naloga = f'{dohod_posle_naloga:,.2f}'.replace(',', ' ')

print(f"Общая сумма дохода: {formatted_dohod} руб.")
print(f"Сумма рассчитанного налога: {formatted_nalog} руб.")
print(f"Сумма «на руки» после вычета налога: {formated_posle_naloga} руб.")
