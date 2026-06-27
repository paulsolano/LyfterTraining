import os

print("Ejercicio 1: Manejo de archivos")

def read_songs(base_dir):
    with open(os.path.join(base_dir, "songs.txt"), "r") as file:
        return file.read().splitlines()

def save_songs(songs, base_dir):
    with open(os.path.join(base_dir, "new_songs.txt"), "w") as file:
        for song in songs:
            file.write(f"{song}\n")

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    songs = read_songs(base_dir)
    print("Canciones originales:")
    for i, song in enumerate(songs, start=1):
        print(f"{i}. {song}")
    sorted_songs = sorted(songs)
    save_songs(sorted_songs, base_dir)
    print("\nCanciones ordenadas (guardadas en new_songs.txt):")
    for i, song in enumerate(sorted_songs, start=1):
        print(f"{i}. {song}")

main()