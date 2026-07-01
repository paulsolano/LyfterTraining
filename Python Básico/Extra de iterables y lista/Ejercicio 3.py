print("Ejercicio 3 - Extra de Iterables y Listas")

my_list = []

how_many_numbers = int(input("¿Cuántos números quieres introducir? (menor a 10) "))
if how_many_numbers > 10:
    print("Son demasiados números. Por favor, introduce un número menor o igual a 10.")
else:
    for i in range(how_many_numbers):
        number = int(input("Introduce tu número: "))
        my_list.append(number)
        lowest = my_list[0]
        for num in my_list:
            if num < lowest:
                lowest = num
    print("El número más bajo de la lista es:", lowest)