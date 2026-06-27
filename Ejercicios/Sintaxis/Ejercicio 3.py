import random

print("Adivina el número secreto entre 1 y 10")

secret_num = random.randint(1,10)

guess = input("Cuál es tu take?: ")

for i in range(10):
    if guess.isdigit():
        guess = int(guess)
        if guess == secret_num:
            print("¡Correcto! Has adivinado el número secreto.")
            break
        else:
            print("Incorrecto. Intenta de nuevo.")
            guess = input("Cuál es tu take? ")
    else:
        print("Por favor, ingresa un número válido.")
        guess = input("Cuál es tu take? ")