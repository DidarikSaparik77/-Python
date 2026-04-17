# Простой калькулятор

num1 = float(input("Введите первое число: "))
operator = input("Введите операцию (+, -, *, /): ")
num2 = float(input("Введите второе число: "))

match operator:
    case "+":
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")
    case "-":
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")
    case "*":
        result = num1 * num2
        print(f"{num1} * {num2} = {result}")
    case "/":
        if num2 == 0:
            print("Ошибка: деление на ноль.")
        else:
            result = num1 / num2
            print(f"{num1} / {num2} = {result}")
    case _:
        print("Неизвестная операция.")