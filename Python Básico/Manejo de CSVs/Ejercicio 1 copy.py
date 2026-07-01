import csv
import os

print("Ejercicio 2: Manejo de CSVs")

def save_videogames_to_csv(file_path):
    try:
        with open(file_path, 'w', encoding='utf-8', newline='') as csvfile:
            fieldnames = ['name', 'genre', 'developer', 'esrb_rating']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter='\t')
            writer.writeheader()

            while True:
                print("Que juego desea guardar? (deje en blanco para terminar)")
                game_name = input("Nombre del juego: ")
                if not game_name:
                    break
                game_genre = input("Genero del juego: ")
                game_developer = input("Desarrollador del juego: ")
                game_esrb_rating = input("Calificación ESRB del juego: ")
                writer.writerow({
                    'name': game_name,
                    'genre': game_genre,
                    'developer': game_developer,
                    'esrb_rating': game_esrb_rating
                })
    except Exception as e:
        print(f"Error al guardar los datos en {file_path}: {e}")

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, "videogames_tab.csv")
    save_videogames_to_csv(file_path)

if __name__ == "__main__":
    main()