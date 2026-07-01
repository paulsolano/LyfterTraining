print("Ejercicio 1 - Funciones") 

def detect_fruits(fruit):
    fruits = ["manzana", "banana", "naranja", "fresa", "uva"]
    if fruit.lower() in fruits:
        print(f"{fruit} es una fruta común.")
    else:
        print(f"{fruit} no es una fruta común.")

def fav_fruit():
    fruit = input("¿Cuál es tu fruta favorita? ")
    print(f"Tu fruta favorita es: {fruit}")
    detect_fruits(fruit)

fav_fruit()
