print("Bienvenido a la calculadora por linea de comandos")

def number1():
    input1 = input("Ingrese el primer número: ")
    try:
        input1 = float(input1)
    except ValueError as e:
        print("El primer número ingresado no es un número. Error:", e)
        exit()
    return input1

def number2():
    input2 = input("Ingrese el segundo número: ")
    try:
        input2 = float(input2)
    except ValueError as e:
        print("El segundo número ingresado no es un número. Error:", e)
        exit()
    return input2

def sum(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def mul(num1, num2):
    return num1 * num2

def div(num1, num2):
    if num2 == 0:
        try:
            raise ZeroDivisionError("No se puede dividir por cero")
        except ZeroDivisionError as e:
            print(f"Error: {e}")
            return None
    return num1 / num2

def menu():
    input1 = number1()

    while True:
        print(f"\nNúmero actual: {input1}")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Salir")
        print("6. Borrar y empezar de nuevo")

        operation = input("Seleccione su opción (1-6): ")
        try:
            operation = int(operation)
        except ValueError:
            print("La opción ingresada no es válida, ingrese un número del 1 al 6")
            continue

        if operation == 5:
            print("Saliendo de la calculadora...")
            break
        elif operation == 6:
            input1 = number1()
            continue
        elif operation in [1, 2, 3, 4]:
            input2 = number2()
            if operation == 1:
                input1 = sum(input1, input2)
            elif operation == 2:
                input1 = sub(input1, input2)
            elif operation == 3:
                input1 = mul(input1, input2)
            elif operation == 4:
                result = div(input1, input2)
                if result is not None:
                    input1 = result
            print(f"Resultado: {input1}")
        else:
            print("La opción ingresada no es válida, ingrese un número del 1 al 6")

menu()

#Fin
