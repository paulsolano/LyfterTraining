def string_counter(s):
    capital_letters = sum(1 for char in s if char.isupper())
    lowercase_letters = sum(1 for char in s if char.islower())
    return capital_letters, lowercase_letters


if __name__ == "__main__":
    print("Ejercicio 5 - Funciones")
    input_string = input("Ingresa una cadena de texto: ")
    capital_count, lowercase_count = string_counter(input_string)
    print(f"Número de letras mayúsculas: {capital_count}")
    print(f"Número de letras minúsculas: {lowercase_count}")


def test_string_counter_with_mixed_case_text():
    assert string_counter("Hola Mundo") == (2, 7)


def test_string_counter_with_only_uppercase_text():
    assert string_counter("HOLA") == (4, 0)


def test_string_counter_with_numbers_symbols_and_spaces():
    assert string_counter("Hi 5!") == (1, 1)
