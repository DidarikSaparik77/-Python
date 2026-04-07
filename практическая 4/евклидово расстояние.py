from math import *

x1, y1, x2, y2 = map(float, input('введите координаты через пробел:').split())

evklidovo_rastoyanie = sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2))
print(evklidovo_rastoyanie)



