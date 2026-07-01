print("Ejercicio 2 - Extra de funciones")

def find_minimum_of_leters_in_a_word(list, n):
    resultado = []
    for word in list:
        if len(word) >= int(n):
            resultado.append(word)
    return resultado
    
how_many_words = int(input("Ingrese cuantas palabras desea ingresar: "))
list = []

for i in range(how_many_words):
    list_of_words = input("Ingrese su palabra: ")
    list.append(list_of_words)
        
min_letter_to_find = input("Ingrese cual es el minimo de letras que debe tener la palabra a buscar: ")

resultado = find_minimum_of_leters_in_a_word(list, min_letter_to_find)
if resultado: 
    print(resultado)
else:
    print("No hay palabras con esa cantidad de letras")

  

