import os

print("Ejercicio 4: Extras de manejo de archivos")

def append_to_file(base_dir):
    try:
        new_text = input("Ingrese el nuevo texto para añadir en el archivo (deje en blanco para cancelar): ")
        if new_text.strip():
            with open(os.path.join(base_dir, "El principito 3.txt"), "a") as file:
                file.write("\n" + new_text)
            print("Texto añadido exitosamente.")
    except IOError as e:
        print(f"Error de E/S al escribir el archivo: {e}")

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    append_to_file(base_dir)   

if __name__ == "__main__":
    main()