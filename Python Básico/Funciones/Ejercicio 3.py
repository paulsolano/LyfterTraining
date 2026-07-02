print("Ejercicio 3 - Funciones")

def sum_of_numbers(numbers):
    return sum(numbers)

how_many = int(input("Cuantos numeros en la lista deseas sumar? "))
numbers = []
for _ in range(how_many):
    numbers.append(int(input("Ingresa un numero: ")))

result = sum_of_numbers(numbers)
print("La suma de los números es:", result)

print("La suma de [1, 2, 3, 4, 5] es:", sum_of_numbers([1, 2, 3, 4, 5]))
