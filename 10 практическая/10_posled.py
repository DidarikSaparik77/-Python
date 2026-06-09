max_znach = 0
count = 0

while count != 3:
    chislo = int(input('\nВведите число: '))

    if chislo > max_znach:
        max_znach = chislo
    else:
        print('\nВведите число больше предыдущего')
        continue

    count += 1

print('\nПорядок принят')