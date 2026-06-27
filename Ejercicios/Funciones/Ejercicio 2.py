print("Ejercicio 2 - Funciones")

outside_variable = "Soy una variable global"

def my_function():
    global outside_variable  # le digo a Python que vas a modificar la global
    inside_variable = "Soy una variable local"
    outside_variable = "Soy una variable global MODIFICADA"
    print("Dentro de la función: " + outside_variable)

print("Antes de la función: " + outside_variable)  # Accediendo a la variable global antes de la función
my_function()
print("Después de la función: " + outside_variable)  # Accediendo a la variable global fuera de la función

try:
    print("Accediendo a la variable local fuera de la función: " + inside_variable)  # Intentando acceder a la variable local fuera de la función
except NameError as e:
    print("Error de scope:", e)  # Imprimiendo el error que ocurre al intentar acceder a la variable local fuera de la función
