def sum_of_numbers(numbers):
    return sum(numbers)


def test_sum_of_numbers_with_positive_numbers():
    assert sum_of_numbers([1, 2, 3, 4, 5]) == 15


def test_sum_of_numbers_with_negative_numbers():
    assert sum_of_numbers([-1, -2, 3]) == 0


def test_sum_of_numbers_with_single_element():
    assert sum_of_numbers([7]) == 7


if __name__ == "__main__":
    print("Ejercicio 3 - Funciones")
    how_many = int(input("Cuantos numeros en la lista deseas sumar? "))
    numbers = []
    for _ in range(how_many):
        numbers.append(int(input("Ingresa un numero: ")))

    result = sum_of_numbers(numbers)
    print("La suma de los números es:", result)

    print("La suma de [1, 2, 3, 4, 5] es:", sum_of_numbers([1, 2, 3, 4, 5]))
