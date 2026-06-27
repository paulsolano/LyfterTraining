first_list = ['Hay', 'en', 'que', 'iteracion', 'indices', 'muy']
second_list = ['casos', 'los', 'la', 'por', 'es', 'util']  

print("Ejercicio 1 - Iterables y Listas")

result_list = [first_list[i] + " " + second_list[i] for i in range(len(first_list))]
print("Lista resultante:", result_list)

how_many_numbers = int(input("¿Cuántos números quieres introducir? (menor a 10)"))
if how_many_numbers <= 11:
    print("Son demasiados números. Por favor, introduce un número menor o igual a 10.")

my_list = []



for i in range(how_many_numbers):
    print("Se repetirá el proceso", how_many_numbers, "veces.")
    my_list.append(int(input("Introduce tu numero: ")))
    if my_list[i] < 0:
        print("No se permiten números negativos. Por favor, introduce un número positivo.")
        my_list.pop()  
        i -= 1

find_numbers = int(input("¿Qué número quieres buscar en la lista? "))
if find_numbers in my_list:
    print("El número", find_numbers, "se repite", my_list.count(find_numbers), "veces en la lista.")
