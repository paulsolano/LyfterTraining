# Analicemos la siguiente función:

def print_all_pairs(my_dict):
    for key1 in my_dict:
        for key2 in my_dict:
            print(f"{key1}-{key2}")

# ¿Cuál es la complejidad temporal?
# La complejidad temporal de la función de print_all_pairs es O(n^2) ya que hay dos bucles anidados que recorren el diccionario, lo que significa que el tiempo de ejecución crece cuadráticamente con el tamaño del diccionario.

# Cuánto dura si hay 1 millón de claves?
# Si hay 1 millón de claves, la función tendría que realizar 1 millón * 1 millón = 1 billón (10^12) de iteraciones. Eso quiere decir que la función tardaría un tiempo considerable en ejecutarse, dependiendo de la velocidad del procesador y otros factores, pero en general sería muy lento y poco práctico para un diccionario de ese tamaño