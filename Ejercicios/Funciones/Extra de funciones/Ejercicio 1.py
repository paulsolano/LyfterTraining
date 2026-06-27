print("Ejercicio 1 - Extra de funciones")

def count_character(s, c):
    count = 0
    for char in s:
        if char == c:
            count += 1
    return count

s = input("Escribe la cadena de texto: ")
c = input("Escribe el caracter: ")

print("El caracter", c, "aparece ", count_character(), "veces.")
