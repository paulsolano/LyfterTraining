import json
import os

print("Ejercicio de Manejo de JSON")

def read_pokemon_data(file_path):
    with open(file_path, "r") as file:
        return json.load(file)

def request_pokemon_data():
    name = input("Nombre: ")
    type_ = input("Tipo: ")
    level = int(input("Nivel: "))
    weight_kg = float(input("Peso (kg): "))
    is_shiny = input("¿Es shiny? (si/no): ").strip().lower() == "si"
    held_item = input("Objeto sostenido (deja en blanco si ninguno): ").strip() or None
    skills = [s.strip() for s in input("Habilidades (separadas por comas): ").split(",")]
    stats = {
        "hp": int(input("HP: ")),
        "attack": int(input("Ataque: ")),
        "defense": int(input("Defensa: ")),
        "sp_attack": int(input("Ataque especial: ")),
        "sp_defense": int(input("Defensa especial: ")),
        "speed": int(input("Velocidad: "))
    }

    return {
        "name": name,
        "type": type_,
        "level": level,
        "weight_kg": weight_kg,
        "is_shiny": is_shiny,
        "held_item": held_item,
        "skills": skills,
        "stats": stats
    }

def save_pokemon_data(file_path, pokemon_data):
    with open(file_path, "w") as file:
        json.dump(pokemon_data, file, indent=3)

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, "pokemon.json")

    pokemons = read_pokemon_data(file_path)
    print(f"Pokémons existentes: {len(pokemons)}")
    for p in pokemons:
        print(f"  - {p['name']} ({p['type']})")

    print("\nAgrega un nuevo Pokémon:")
    nuevo_pokemon = request_pokemon_data()
    pokemons.append(nuevo_pokemon)

    save_pokemon_data(file_path, pokemons)
    print(f"\n{nuevo_pokemon['name']} fue agregado. Total de Pokémons: {len(pokemons)}")

if __name__ == "__main__":
    main()
