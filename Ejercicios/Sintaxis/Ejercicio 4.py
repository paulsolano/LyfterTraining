# Ejercicio 4 - Mayor de tres números
# Crea un programa que le pida tres números al usuario y muestre el mayor.

while True:
    try:
        num1 = int(input("Ingrese el primer número: "))
        break  # si llegó aquí, el número es válido → sale del loop
    except ValueError:
        print("Eso no es un número válido. Intenta de nuevo.")
while True:
    try:
        num2 = int(input("Ingrese el segundo número: "))
        break  # si llegó aquí, el número es válido → sale del loop
    except ValueError:
        print("Eso no es un número válido. Intenta de nuevo.")

while True:
    try:
        num3 = int(input("Ingrese el tercer número: "))
        break  # si llegó aquí, el número es válido → sale del loop
    except ValueError:
        print("Eso no es un número válido. Intenta de nuevo.")

if num1 == num2 == num3:
    print("Los tres números son iguales.")
elif num1 == num2 and num1 > num3:
    print("Los 2 primeros números son los mayores.")
elif num1 == num3 and num1 > num2:
    print("El primero y el tercer número son los mayores.")
elif num2 == num3 and num2 > num1:
    print("El segundo y el tercer número son los mayores.")
elif num1 > num2 and num1 > num3:
    print(f"El número mayor es: {num1}")
elif num2 > num1 and num2 > num3:
    print(f"El número mayor es: {num2}")
elif num3 > num1 and num3 > num2:
    print(f"El número mayor es: {num3}")