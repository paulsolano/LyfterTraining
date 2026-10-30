# Consideremos los siguientes algoritmos

def linear_search(my_list, target):
    for item in my_list:
        if item == target:
            return True
    return False

def binary_search(my_list, target):
    low = 0
    high = len(my_list) - 1
    while low <= high:
        mid = (low + high) // 2
        if my_list[mid] == target:
            return True
        elif my_list[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return False

# Cúal es la complejidad de cada una de las funciones?
# linear_search: O(n) # binary_search: O(log n)

# En qué condiciones conviene usar cada uno?
# linear_search conviene usarlo cuando la lista no está ordenada,
# mientras que binary_search conviene usarlo cuando la lista está ordenada, 
# ya que tiene una complejidad logarítmica y es más eficiente para listas grandes.

# Qué pasa si la lista no está ordenada?
# linear_search sigue funcionando bien, porque revisa elemento por elemento y no
# depende del orden. binary_search puede dar resultados incorrectos: asume que la
# lista está ordenada, así que al comparar con el elemento del medio descarta una
# mitad que quizás sí contenía el valor, y puede devolver False aunque exista.

