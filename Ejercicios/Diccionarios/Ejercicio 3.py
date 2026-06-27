print("Ejercicio 3 - Diccionarios\n")

my_dict = {"name": "Robert", "lastname": "Oppenheimer", "studies": "nuclear physics", "age": 42, "wife": "Katherine"}
list_of_keys = ["name", "studies", "age"]
print("Diccionario antes de eliminar las keys:", my_dict)
for key in list_of_keys:
    if key in my_dict:
        del my_dict[key]
print("Diccionario después de eliminar las keys:", my_dict)