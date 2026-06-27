print("Ejercicio 2 - Diccionarios\n")

dog_data = ['name', 'breed', 'age', 'father_name']
data = ['Onix', 'Labrador', 3, 'Paúl']

my_dog = dict(zip(dog_data, data))

for key, value in my_dog.items():
    print(f"{key.capitalize()}: {value}")

