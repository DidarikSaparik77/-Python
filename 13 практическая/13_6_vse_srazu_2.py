numbers = [8, 9, 10, 11]

numbers[1] = 17
numbers.extend(range(4, 7))
numbers.pop(0)
numbers.extend(numbers)
numbers.insert(3, 25)

print(*numbers)