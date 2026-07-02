print("Ejercicio 3 - Iterables y Listas")

my_list = [1, 2, 3, 4, 5]
reversed_list = my_list.copy()  
reversed_list[0], reversed_list[-1] = reversed_list[-1], reversed_list[0] 

print("Lista original:", my_list)
print("Lista invertida:", reversed_list)

