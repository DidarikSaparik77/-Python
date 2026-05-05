m, p, n = int(input()), int(input()), int(input())

cur_population = float(m)

for i in range(n):
    print(i + 1, cur_population)
    cur_population = cur_population * (1 + p / 100)