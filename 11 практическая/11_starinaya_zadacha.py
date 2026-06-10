na_balike, byk, korova, telonok = 100, 10, 5, 0.5

for i in range(1, 2):
    for j in range(1, 10):
        for k in range(1, 100):
            if i * byk + j * korova + k * telonok == 100:
                print(f'Быков - {i}, коров - {j}, телёнок - {k}')