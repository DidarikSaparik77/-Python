for a in range(1, 145):
    for b in range(a + 1, 145):
        for c in range(b + 1, 145):
            for d in range(c + 1, 151):
                e = int(((a ** 5) + (b ** 5) + (c ** 5) + (d ** 5)) ** 0.2)
                if e ** 5 == int((a ** 5) + (b ** 5) + (c ** 5) + (d ** 5)):
                    print(a + b + c + d + e)
                    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'e =', e)