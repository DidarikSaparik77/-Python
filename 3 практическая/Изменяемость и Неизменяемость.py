my_list = [1, 2, 3, 4, 5]
print(f"Изначальный список: {my_list}")

my_list[0] = 100
my_list[1] = 200
my_list[-1] = 500
print(f"После изменения: {my_list}")




my_tuple = (1, 2, 3)
print(f"Изначальный кортеж {my_tuple}")

try:
    my_tuple[0] = 100
    print(f"Кортеж после изменения: {my_tuple}")
except TypeError as error:
    print(f"Ошибка: {error}")




my_string = "cat"
print(f"Начальная строка {my_string}")

try:
    my_string[0] = "b"
    print(f"Строка после изменения: {my_tuple}")
except TypeError as error:
    print(f"Ошибка: {error}")




new_string = "b" + my_string[1:]
print(f"После изменения неизменяемых типов данных(1 способ): {new_string}")

new_string = my_string.replace("t", "r")
print(f"После изменения неизменяемых типов данных(2 способ): {new_string}")

str_list = list(new_string)
str_list[1] = "v"
new_string = "".join(str_list)
print(f"После изменения неизменяемых типов данных(3 способ): {new_string}")




tuple_list = list(my_tuple)
tuple_list[0] = 100
new_tuple = tuple(tuple_list)
print(f"После изменения неизменяемых типов данных: {new_tuple}")
