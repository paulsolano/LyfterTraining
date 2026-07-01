print("Ejercicio 5 - Funciones")

def string_counter(s):
    capital_letters = sum(1 for char in s if char.isupper())
    lowercase_letters = sum(1 for char in s if char.islower())
    return capital_letters, lowercase_letters
input_string = input("Ingresa una cadena de texto: ")
capital_count, lowercase_count = string_counter(input_string)
print(f"Número de letras mayúsculas: {capital_count}")
print(f"Número de letras minúsculas: {lowercase_count}")
