for i in  range(1, 13):
    for j in range(1, 13):
        for k in range(1, 13):
            if (31 * i) + (30 * j) + (28 * k) == 365:
                print(i, j, k)