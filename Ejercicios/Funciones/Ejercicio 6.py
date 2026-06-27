# Cree una función que acepte un string con palabras separadas por un guion y retorne un string igual pero ordenado alfabéticamente.
# Hay que convertirlo a lista, ordenarlo, y convertirlo nuevamente a string.

print("Ejercicio 6 - Funciones")

def order_string_alphabetically(s):
    return "-".join(sorted(s.split("-")))
ordered_string = order_string_alphabetically(input("Escribe la cadena de texto: "))
print("La cadena ordenada alfabéticamente es: ", ordered_string)