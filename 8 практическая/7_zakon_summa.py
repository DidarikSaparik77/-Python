n = int(input())

total = 0

flag = True

for i in range(1, n + 1):
    if flag == True:
        total += i
        flag = False
    else:
        total -= i
        flag = True

print(total)




