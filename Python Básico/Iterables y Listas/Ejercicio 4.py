print("Ejercicio 4 - Iterables y Listas")

my_list = [10, 13, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]

pair_numbers = []
for number in my_list:
    if number % 2 == 0:
        pair_numbers.append(number)
print("Números pares:", pair_numbers)