import os

print("Ejercicio 3: Extras de manejo de archivos")

def read_file(base_dir):
    try:
        with open(os.path.join(base_dir, "El principito 2.txt"), "r") as file:
            return file.readlines()
    except FileNotFoundError:
        print(f"Error: El archivo 'El principito 2.txt' no se encontró.")
        return None
    except IOError as e:
        print(f"Error de E/S al leer el archivo: {e}")
        return None

def new_file(base_dir, lines):
    try:
        with open(os.path.join(base_dir, "El principito 2 - copia.txt"), "w") as file:
            for line in lines:
                file.write(line)
        print("Archivo 'El principito 2 - copia.txt' creado exitosamente.")
    except IOError as e:
        print(f"Error de E/S al escribir el archivo: {e}")

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    lines = read_file(base_dir)
    upper_lines = [line.upper() for line in lines] if lines is not None else None
    if upper_lines is not None:
        new_file(base_dir, upper_lines)

if __name__ == "__main__":
    main()
