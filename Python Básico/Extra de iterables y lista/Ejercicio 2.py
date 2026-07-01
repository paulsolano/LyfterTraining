print("Ejercicio 2 - Extra de Iterables y Listas")

list_of_numbers = []


how_many_numbers = int(input("¿Cuántos números quieres introducir? (menor a 10) "))
if how_many_numbers > 10:
    print("Son demasiados números. Por favor, introduce un número menor o igual a 10.")
for i in range(how_many_numbers):
    number = int(input("Introduce tu número: "))
    list_of_numbers.append(number)
negative_numbers = [num for num in list_of_numbers if num <= 0]
if negative_numbers:
    print("Hay", len(negative_numbers), "números negativo(s) o ceros.")
else:
    print("Todos los numeros introducidos son positivos.")