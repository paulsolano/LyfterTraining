print("Ejercicio 3 - Extras de funciones")

def vocals_returned(s):
    count = 0
    for letter in s:
        if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
            count += 1
    return count

word = input("Ingrese una palabra: ")

resultado = vocals_returned(word)
if resultado > 0:
    print("La palabra contiene", resultado, "vocales")
else:
    print("La palabra no contiene vocales")
          
    

