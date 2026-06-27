# Cree un programa que cuente cuántas veces aparece un número específico en una lista. Pida al usuario una lista de números y otro número a buscar

print("Ejercicio 1 - Extra de Iterables y Listas")

my_list = []

def pedir_numero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Entrada no válida. Por favor, introduce un número entero.")

while True:
    how_many_numbers = pedir_numero("¿Cuántos números quieres introducir? (menor a 10) ")
    if how_many_numbers > 10:
        print("Son demasiados números. Por favor, introduce un número menor o igual a 10.")
    else:
        break

for i in range(how_many_numbers):
    while True:
        number = pedir_numero("Introduce tu número: ")
        if number < 0:
            print("No se permiten números negativos. Por favor, introduce un número positivo.")
        else:
            my_list.append(number)
            break

find_number = pedir_numero("¿Qué número quieres buscar en la lista? ")

while True:
    if find_number in my_list:
        print("El número", find_number, "se repite", my_list.count(find_number), "veces en la lista.")
    else:
        print("El número", find_number, "no se encuentra en la lista.")
    continue_search = input("¿Quieres buscar otro número? (sí/no) ").lower()
    if continue_search == "sí":
        find_number = pedir_numero("¿Qué número quieres buscar en la lista? ")
    else:
        print("Gracias por usar el programa.")
        break
