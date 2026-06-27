import os

print("Ejercicio 1: Extras de manejo de archivos")

def read_file(base_dir):
    try:
        with open(os.path.join(base_dir, "text.txt"), "r") as file:
            return file.readlines()
    except FileNotFoundError:
        print(f"Error: El archivo 'text.txt' no se encontró.")
        return None
    except IOError as e:
        print(f"Error de E/S al leer el archivo: {e}")
        return None

def new_file(base_dir, lines):
    try:
        with open(os.path.join(base_dir, "new_text.txt"), "w") as file:
            file.write(" ".join(lines))
    except IOError as e:
        print(f"Error de E/S al escribir el archivo: {e}")

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    lines = read_file(base_dir)
    if lines is not None:
        new_file(base_dir, [line.strip() for line in lines])

if __name__ == "__main__":
    main()
