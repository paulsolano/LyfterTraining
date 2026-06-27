# Ejercicio 2 - Condicionales y entrada de usuario
# Crea un programa que le pida al usuario su nombre, apellido y edad,
# y muestre si es un:
#   - Bebé
#   - Niño
#   - Preadolescente
#   - Adolescente
#   - Adulto joven
#   - Adulto
#   - Adulto mayor

# Tu código aquí
name = input("Ingrese su nombre: ")
lastname = input("Ingrese su apellido: ")
age = int(input("Ingrese su edad: "))

if age < 2: 
    print(f"{name} {lastname} es un bebé.")
elif age < 12:
    print(f"{name} {lastname} es un niño.")
elif age < 14: 
    print(f"{name} {lastname} es un preadolescente.")
elif age < 18:
    print(f"{name} {lastname} es un adolescente.")
elif age < 30:
    print(f"{name} {lastname} es un adulto joven.") 
elif age < 60:
    print(f"{name} {lastname} es un adulto.")
else: print(f"{name} {lastname} es un adulto mayor.")

