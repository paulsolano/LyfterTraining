print("Ejercicio 4 - Funciones")

def reverse_string(s):
    return s[::-1]
input_string = input("Ingresa una cadena de texto: ")
reversed_string = reverse_string(input_string)
print(f"La cadena invertida es: {reversed_string}")

