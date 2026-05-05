import random

secret_number = random.randint(1, 10)

attempts = 3
guessed = False

for i in range(attempts):   
    guess = int(input())
    
    if guess == secret_number:
        print("Угадали!")
        guessed = True
        break
    else:
        print("Неверно")
        if guess < secret_number:
            print("Загаданное число больше")
        else:
            print("Загаданное число меньше")

if not guessed:
    print(f"Вы не угадали. Загаданное число: {secret_number}")