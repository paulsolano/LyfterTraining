print("Ejercicio 5 - Extra de Iterables y Listas")

print("Introduce 5 palabras")

my_list_of_words = []
for i in range(5):
    word = input("Introduce tu palabra numero " + str(i + 1) + ": ")
    my_list_of_words.append(word)
    if len(my_list_of_words) > 4    :
        print("Has introducido el número máximo de palabras.")
        break
print("Las palabras introducidas son:", my_list_of_words)
print("Las palabras con mas de 4 letras son:", [word for word in my_list_of_words if len(word) > 4])
