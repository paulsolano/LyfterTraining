print("Ejercicio 5 - Iterables y Listas")

numbers_list = []
for i in range(10):
    number = int(input("Introduce el número " + str(i + 1) + ": "))
    numbers_list.append(number)

print("Lista de números introducidos:", numbers_list)
greatest_number = max(numbers_list)
print("El número más grande es:", greatest_number)
