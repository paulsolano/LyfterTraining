print("Ejercicio 4 - Extra de Iterables y Listas")

my_list = []

how_many_numbers = int(input("¿Cuántos números quieres introducir? (menor a 10) "))
if how_many_numbers > 10:
    print("Son demasiados números. Por favor, introduce un número menor o igual a 10.")
else:
    for i in range(how_many_numbers):
        number = int(input("Introduce tu número: "))
        my_list.append(number)
        average = sum(my_list) / len(my_list)
        greater_than_average = [num for num in my_list if num > average]
    print("El promedio de los números introducidos es:", average)
    print("Los números mayores que el promedio son:", greater_than_average)
