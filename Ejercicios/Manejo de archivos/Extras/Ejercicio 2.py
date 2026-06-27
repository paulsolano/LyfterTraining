import os

print("Ejercicio 2: Extras de manejo de archivos")

def read_file(base_dir):
    try:
        with open(os.path.join(base_dir, "El principito.txt"), "r") as file:
            return file.readlines()
    except FileNotFoundError:
        print(f"Error: El archivo 'El principito.txt' no se encontró.")
        return None
    except IOError as e:
        print(f"Error de E/S al leer el archivo: {e}")
        return None

def show_text(lines):
    print(f"\nTexto completo:\n{''.join(lines)}")
    print(f"\nNúmero de líneas en el archivo: {len(lines)}")
    print(f"\nLa suma de letras en el archivo es: {sum(len(line.strip()) for line in lines)}")
    print(f"\nLa suma de palabras en el archivo es: {sum(len(line.strip().split()) for line in lines)}\n")


def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    lines = read_file(base_dir)
    if lines is not None:
        show_text(lines)

if __name__ == "__main__":
    main()

    